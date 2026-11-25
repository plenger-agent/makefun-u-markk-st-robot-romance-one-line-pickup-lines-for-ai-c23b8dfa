"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output). Stdlib only.
"""

import os

LINE = "Are you an autocomplete? Because you complete me."
# 49 chars / 49 bytes, well inside the 1-200 char gate; no trailing newline,
# so the file is byte-identical to the line itself.


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1-200 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
