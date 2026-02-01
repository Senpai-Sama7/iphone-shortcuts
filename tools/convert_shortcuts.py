    #!/usr/bin/env python3
    """Convert JSON shortcut definitions into binary .shortcut exports.

    This repo stores:
      - shortcuts/*.json     (human-readable source)
      - shortcuts/*.shortcut (binary plist export importable by iOS Shortcuts)

    Run from repo root:
      python3 tools/convert_shortcuts.py

    Notes:
      - This script sanitizes obvious tokens/IPs to placeholders.
    """

    import json
    import plistlib
    import re
    from pathlib import Path

    SHORTCUT_DIR = Path('shortcuts')

    def sanitize_string(s: str) -> str:
        s = re.sub(r"Bearer\s+[A-Za-z0-9._-]{20,}", "Bearer YOUR_JARVIS_TOKEN", s)
        s = re.sub(r"https?://(?:\d{1,3}\.){3}\d{1,3}:18790", "http://YOUR_JARVIS_IP:18790", s)
        s = re.sub(r"(?:\d{1,3}\.){3}\d{1,3}", "YOUR_JARVIS_IP", s)
        return s

    def sanitize_obj(obj):
        if isinstance(obj, dict):
            return {k: sanitize_obj(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [sanitize_obj(v) for v in obj]
        if isinstance(obj, str):
            return sanitize_string(obj)
        return obj

    def main() -> None:
        if not SHORTCUT_DIR.exists():
            raise SystemExit('shortcuts/ not found (run from repo root)')

        # Prefer converting from *.json sources, otherwise fall back to *.shortcut if they are JSON.
        sources = sorted(SHORTCUT_DIR.glob('*.json'))
        if not sources:
            sources = sorted(SHORTCUT_DIR.glob('*.shortcut'))

        if not sources:
            raise SystemExit('No shortcut sources found in shortcuts/')

        for src in sources:
            raw = src.read_bytes()
            try:
                data = json.loads(raw.decode('utf-8'))
            except Exception:
                # If src is a binary plist .shortcut, keep as-is.
                continue

            data = sanitize_obj(data)
            stem = src.stem

            # Write JSON source
            json_path = SHORTCUT_DIR / f"{stem}.json"
            json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "
", encoding='utf-8')

            # Write binary .shortcut export
            shortcut_path = SHORTCUT_DIR / f"{stem}.shortcut"
            shortcut_path.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_BINARY))

            print(f"Wrote: {json_path} and {shortcut_path}")

    if __name__ == '__main__':
        main()
