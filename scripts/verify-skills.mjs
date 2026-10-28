#!/usr/bin/env node
// Zero-trust integrity check for agent skills. No dependencies; Node >= 18.
//
// Fails (exit 1) when any of these hold:
//   1. A skill folder's content no longer matches its skills-lock.json hash.
//   2. A skill folder exists that skills-lock.json does not list (unreviewed).
//   3. A lock entry points at a folder that does not exist.
//   4. A .claude/skills entry is not a symlink into .agents/skills/<same name>.
//   5. A skill ships a script or executable not listed in ALLOWED_EXECUTABLES.
//   6. A skill file contains invisible Unicode (bidi overrides, zero-width,
//      tag characters) that can hide instructions from a human reviewer.
//   7. .claude/settings.json is not valid JSON (an invalid file silently
//      disables every permission rule and hook in it).
//
// Usage: node scripts/verify-skills.mjs [--quiet]

import { createHash } from "node:crypto";
import { readFile, readdir, lstat, readlink, stat } from "node:fs/promises";
import { join, relative, resolve, extname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const SKILLS_DIR = join(ROOT, ".agents", "skills");
const CLAUDE_SKILLS_DIR = join(ROOT, ".claude", "skills");
const LOCK_FILE = join(ROOT, "skills-lock.json");
const SETTINGS_FILE = join(ROOT, ".claude", "settings.json");

// Skills must be instructions only. Add "<skill>/<path>" here only after the
// script itself has been reviewed line by line in a pull request.
const ALLOWED_EXECUTABLES = new Set([]);
const EXECUTABLE_EXT = new Set([
  ".sh", ".bash", ".zsh", ".ps1", ".bat", ".cmd", ".py", ".js", ".cjs",
  ".mjs", ".ts", ".rb", ".pl", ".php", ".exe", ".bin", ".so", ".dylib",
  ".dll", ".jar", ".wasm",
]);
const INVISIBLE =
  /[\u200B-\u200F\u202A-\u202E\u2060-\u2064\u2066-\u2069\uFEFF]|[\u{E0000}-\u{E007F}]/u;

const quiet = process.argv.includes("--quiet");
const failures = [];
const fail = (msg) => failures.push(msg);

// Mirrors computeSkillFolderHash() in the `skills` CLI (v1.7.x) exactly:
// sha256 over (relativePath, bytes) pairs sorted with localeCompare,
// skipping .git and node_modules.
async function collectFiles(baseDir, currentDir, results) {
  const entries = await readdir(currentDir, { withFileTypes: true });
  await Promise.all(entries.map(async (entry) => {
    const fullPath = join(currentDir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === ".git" || entry.name === "node_modules") return;
      await collectFiles(baseDir, fullPath, results);
    } else if (entry.isFile()) {
      const content = await readFile(fullPath);
      const relativePath = relative(baseDir, fullPath).split("\\").join("/");
      const mode = (await stat(fullPath)).mode;
      results.push({ relativePath, content, mode });
    } else if (entry.isSymbolicLink()) {
      fail(`${relative(ROOT, fullPath)}: symlink inside a skill folder (not allowed)`);
    }
  }));
}

async function hashSkill(dir) {
  const files = [];
  await collectFiles(dir, dir, files);
  files.sort((a, b) => a.relativePath.localeCompare(b.relativePath));
  const hash = createHash("sha256");
  for (const f of files) {
    hash.update(f.relativePath);
    hash.update(f.content);
  }
  return { digest: hash.digest("hex"), files };
}

async function main() {
  let lock;
  try {
    lock = JSON.parse(await readFile(LOCK_FILE, "utf8"));
  } catch (e) {
    fail(`skills-lock.json unreadable: ${e.message}`);
    lock = { skills: {} };
  }
  const locked = lock.skills ?? {};

  let present = [];
  try {
    present = (await readdir(SKILLS_DIR, { withFileTypes: true }))
      .filter((d) => d.isDirectory()).map((d) => d.name);
  } catch {
    // No skills installed is a valid state.
  }

  for (const name of present) {
    if (!locked[name]) fail(`.agents/skills/${name}: not in skills-lock.json (unreviewed skill)`);
  }

  for (const [name, entry] of Object.entries(locked)) {
    const dir = join(SKILLS_DIR, name);
    try {
      await stat(dir);
    } catch {
      fail(`skills-lock.json lists "${name}" but .agents/skills/${name} is missing`);
      continue;
    }
    const { digest, files } = await hashSkill(dir);
    if (digest !== entry.computedHash) {
      fail(`${name}: content hash ${digest.slice(0, 12)}... does not match lock ${String(entry.computedHash).slice(0, 12)}...`);
    } else if (!quiet) {
      console.log(`ok   ${name}  ${digest.slice(0, 12)}  (${entry.source})`);
    }
    for (const f of files) {
      const id = `${name}/${f.relativePath}`;
      const isExec = EXECUTABLE_EXT.has(extname(f.relativePath).toLowerCase()) || (f.mode & 0o111) !== 0;
      if (isExec && !ALLOWED_EXECUTABLES.has(id)) fail(`${id}: executable or script file in a skill (review and allowlist, or remove)`);
      const text = f.content.toString("utf8");
      const m = text.match(INVISIBLE);
      if (m) fail(`${id}: invisible Unicode U+${m[0].codePointAt(0).toString(16).toUpperCase()} (possible hidden instructions)`);
    }
  }

  try {
    for (const name of await readdir(CLAUDE_SKILLS_DIR)) {
      const p = join(CLAUDE_SKILLS_DIR, name);
      const st = await lstat(p);
      if (!st.isSymbolicLink()) {
        fail(`.claude/skills/${name}: must be a symlink into .agents/skills (found a real ${st.isDirectory() ? "directory" : "file"})`);
        continue;
      }
      const target = resolve(CLAUDE_SKILLS_DIR, await readlink(p));
      if (target !== join(SKILLS_DIR, name)) fail(`.claude/skills/${name}: symlink points outside .agents/skills/${name} (${relative(ROOT, target)})`);
    }
  } catch {
    // No .claude/skills directory is a valid state.
  }

  try {
    JSON.parse(await readFile(SETTINGS_FILE, "utf8"));
    if (!quiet) console.log("ok   .claude/settings.json parses");
  } catch (e) {
    if (e.code !== "ENOENT") fail(`.claude/settings.json invalid JSON: ${e.message}`);
  }

  if (failures.length) {
    console.error(`\nSKILL INTEGRITY CHECK FAILED (${failures.length}):`);
    for (const f of failures) console.error(`  x ${f}`);
    process.exit(1);
  }
  if (!quiet) console.log("\nAll skill integrity checks passed.");
}

main().catch((e) => {
  console.error(`verify-skills crashed: ${e.stack || e}`);
  process.exit(2);
});
