"""Build a multi-interpreter hash lock and verify every digest against PyPI.

Usage: python3 -I tools/build-lint-lock.py <pins.txt> <current_lock> <out_lock> <wheel_dir>...
Fails (exit 1) on any digest that PyPI does not publish for that file, or on a
digest for an unchanged pin that differs from the current lock.
"""
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

pins_path, old_lock_path, out_path, *wheel_dirs = sys.argv[1:]
pins = [l.strip() for l in Path(pins_path).read_text().splitlines() if l.strip()]
old = {}
for line in Path(old_lock_path).read_text().splitlines():
    if line.strip():
        name_ver, *hashes = line.split(" --hash=sha256:")
        old[name_ver.strip()] = {h.strip() for h in hashes}

def norm(n):
    return re.sub(r"[-_.]+", "-", n).lower()

wheels = {}
for d in wheel_dirs:
    for w in Path(d).glob("*.whl"):
        dist = norm(w.name.split("-")[0])
        wheels.setdefault(dist, {})[w.name] = hashlib.sha256(w.read_bytes()).hexdigest()

errors, out = [], []
for pin in pins:
    name, ver = pin.split("==")
    files = wheels.get(norm(name), {})
    if not files:
        errors.append(f"{pin}: no wheel downloaded")
        continue
    with urllib.request.urlopen(f"https://pypi.org/pypi/{name}/{ver}/json", timeout=30) as r:
        published = {u["filename"]: u["digests"]["sha256"] for u in json.load(r)["urls"]}
    for fname, digest in sorted(files.items()):
        if published.get(fname) != digest:
            errors.append(f"{fname}: local {digest[:12]} != PyPI {str(published.get(fname))[:12]}")
    digests = sorted(set(files.values()))
    if pin in old and not old[pin] <= set(digests):
        errors.append(f"{pin}: a digest in the current lock is not among the downloaded wheels")
    out.append(pin + "".join(f" --hash=sha256:{d}" for d in digests))

if errors:
    print("\n".join(errors))
    sys.exit(1)
Path(out_path).write_text("\n".join(out) + "\n")
print(f"verified {sum(len(f) for f in wheels.values())} wheels against PyPI; wrote {len(out)} pins")
