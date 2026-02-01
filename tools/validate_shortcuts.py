#!/usr/bin/env python3
"""Validate that shortcuts/*.shortcut are importable binary plist exports.

Fails if:
  - file is not a plist
  - required top-level keys are missing
  - obvious secrets appear in strings
"""

import plistlib
import re
from pathlib import Path

SHORTCUT_DIR = Path('shortcuts')

def walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)
    elif isinstance(obj, str):
        yield obj

def main() -> None:
    if not SHORTCUT_DIR.exists():
        raise SystemExit('shortcuts/ not found (run from repo root)')

    files = sorted(SHORTCUT_DIR.glob('*.shortcut'))
    if not files:
        raise SystemExit('No .shortcut files found')

    secret_like = re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}")
    bad_ip = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")

    for f in files:
        raw = f.read_bytes()
        try:
            data = plistlib.loads(raw)
        except Exception as e:
            raise SystemExit(f"{f}: not a plist: {e}")

        # Required-ish keys for shortcut export
        for k in ("WFWorkflowActions", "WFWorkflowClientVersion", "WFWorkflowName"):
            if k not in data:
                raise SystemExit(f"{f}: missing key {k}")

        # Ensure no obvious secrets shipped
        for s in walk(data):
            if isinstance(s, str) and secret_like.search(s):
                raise SystemExit(f"{f}: appears to contain a bearer token")
            # We allow placeholder YOUR_JARVIS_IP, but not literal IPs.
            if isinstance(s, str) and bad_ip.search(s) and "YOUR_JARVIS_IP" not in s:
                raise SystemExit(f"{f}: appears to contain a literal IP address")

    print(f"OK: {len(files)} shortcut(s) validated")

if __name__ == '__main__':
    main()
