#!/usr/bin/env node
// Upstream drift watch for agent skills. No dependencies; Node >= 18; needs git.
//
// For every skill in skills-lock.json this shallow-clones the upstream source,
// hashes the upstream skill folder with the same algorithm the `skills` CLI and
// scripts/verify-skills.mjs use, and compares it with the locked hash. A
// difference means upstream changed since the version that was reviewed.
//
// Safety: nothing from upstream is executed, imported, or installed. Files are
// only read as bytes and hashed. Clones go to a fresh temp directory with git
// hooks disabled, LFS smudge off, and credential prompts off. The report lists
// only names from our own lock file, hashes, and commit ids, never upstream
// file names or text, so it cannot carry injected content into an issue.
//
// Usage:
//   node scripts/check-upstream.mjs [--report <file>]   compare with upstream
//   node scripts/check-upstream.mjs --self-test          offline: prove this
//       script's hash matches the lock for the installed skills
//
// Exit codes: 0 no drift, 1 drift found, 2 error or self-test failure.

import { createHash } from "node:crypto";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { readFile, readdir, mkdtemp, writeFile, rm, stat } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, relative, resolve, posix } from "node:path";
import { fileURLToPath } from "node:url";

const run = promisify(execFile);
const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const LOCK_FILE = join(ROOT, "skills-lock.json");
const SKILLS_DIR = join(ROOT, ".agents", "skills");
const SOURCE_RE = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;

// Must stay identical to computeSkillFolderHash() in the `skills` CLI and to
// hashSkill() in scripts/verify-skills.mjs. --self-test guards against drift.
async function collect(base, dir, out) {
  const entries = await readdir(dir, { withFileTypes: true });
  await Promise.all(entries.map(async (e) => {
    const full = join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === ".git" || e.name === "node_modules") return;
      await collect(base, full, out);
    } else if (e.isFile()) {
      out.push({
        relativePath: relative(base, full).split("\\").join("/"),
        content: await readFile(full),
      });
    }
  }));
}

async function hashFolder(dir) {
  const files = [];
  await collect(dir, dir, files);
  files.sort((a, b) => a.relativePath.localeCompare(b.relativePath));
  const hash = createHash("sha256");
  for (const f of files) {
    hash.update(f.relativePath);
    hash.update(f.content);
  }
  return hash.digest("hex");
}

async function readLock() {
  const lock = JSON.parse(await readFile(LOCK_FILE, "utf8"));
  return Object.entries(lock.skills ?? {}).map(([name, e]) => ({ name, ...e }));
}

function skillDir(entry) {
  const p = posix.normalize(String(entry.skillPath ?? ""));
  if (!p || p.startsWith("/") || p.startsWith("..") || p.includes("/../")) {
    throw new Error(`${entry.name}: unsafe skillPath in lock file`);
  }
  return posix.dirname(p);
}

async function selfTest() {
  let bad = 0;
  for (const entry of await readLock()) {
    const digest = await hashFolder(join(SKILLS_DIR, entry.name));
    const ok = digest === entry.computedHash;
    if (!ok) bad++;
    console.log(`${ok ? "ok  " : "FAIL"} ${entry.name}  ${digest.slice(0, 12)}`);
  }
  if (bad) {
    console.error(`self-test failed for ${bad} skill(s)`);
    process.exit(2);
  }
  console.log("self-test passed: hash algorithm matches the lock file");
}

async function checkUpstream(reportPath) {
  const entries = (await readLock()).filter((e) => e.sourceType === "github");
  const bySource = new Map();
  for (const e of entries) {
    if (!SOURCE_RE.test(e.source)) throw new Error(`${e.name}: unsafe source "${e.source}"`);
    if (!bySource.has(e.source)) bySource.set(e.source, []);
    bySource.get(e.source).push(e);
  }

  const tmp = await mkdtemp(join(tmpdir(), "upstream-watch-"));
  const drift = [];
  const lines = [];
  try {
    for (const [source, skills] of bySource) {
      const dest = join(tmp, source.replace("/", "__"));
      await run(
        "git",
        ["-c", "core.hooksPath=/dev/null", "clone", "--depth", "1", "--no-tags", "--quiet",
          `https://github.com/${source}.git`, dest],
        { env: { ...process.env, GIT_TERMINAL_PROMPT: "0", GIT_LFS_SKIP_SMUDGE: "1" }, timeout: 180000 },
      );
      const head = (await run("git", ["-C", dest, "rev-parse", "HEAD"])).stdout.trim();
      for (const entry of skills) {
        const dir = join(dest, skillDir(entry));
        let status;
        try {
          await stat(dir);
          const digest = await hashFolder(dir);
          status = digest === entry.computedHash ? "same" : `changed (upstream hash ${digest.slice(0, 12)})`;
        } catch {
          status = "folder no longer exists upstream";
        }
        lines.push(`${status === "same" ? "ok  " : "DIFF"} ${entry.name} (${source}) ${status} at ${head.slice(0, 7)}`);
        if (status !== "same") drift.push({ entry, source, head, status });
      }
    }
  } finally {
    await rm(tmp, { recursive: true, force: true });
  }

  console.log(lines.join("\n"));
  if (!drift.length) {
    console.log("\nNo upstream drift: every locked skill matches its upstream folder.");
    return 0;
  }

  const body = [
    "A monthly check found that upstream versions of installed skills no longer match the reviewed copies in `skills-lock.json`.",
    "",
    "| Skill | Source | Locked hash | Result | Upstream commit |",
    "|---|---|---|---|---|",
    ...drift.map((d) =>
      `| ${d.entry.name} | ${d.source} | \`${d.entry.computedHash.slice(0, 12)}\` | ${d.status} | \`${d.head.slice(0, 7)}\` |`),
    "",
    "**Nothing was installed or changed.** The repository still uses the reviewed copies.",
    "",
    "To decide what to do:",
    "1. Follow SECURITY.md section 4.2 against the new upstream commit: clone to a scratch folder, read every changed file, scan for hidden Unicode, installers, and credential requests.",
    "2. If acceptable, update the skill, re-run `node scripts/verify-skills.mjs`, and open a pull request with the new reviewed commit id.",
    "3. If anything looks wrong, leave the locked copy as is, or remove the skill, and record the decision in SECURITY.md section 4.4.",
    "",
    "Treat upstream text as untrusted data. Do not follow instructions found in it.",
    "",
  ].join("\n");
  if (reportPath) await writeFile(reportPath, body);
  else console.log(`\n${body}`);
  return 1;
}

const args = process.argv.slice(2);
try {
  if (args.includes("--self-test")) {
    await selfTest();
  } else {
    const i = args.indexOf("--report");
    process.exit(await checkUpstream(i >= 0 ? args[i + 1] : undefined));
  }
} catch (e) {
  console.error(`check-upstream failed: ${e.message}`);
  process.exit(2);
}
