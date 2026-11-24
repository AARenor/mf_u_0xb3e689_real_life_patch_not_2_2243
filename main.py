#!/usr/bin/env python3
"""Write one short patch note for make.fun bounty u-0xb3e689."""

import os
import sys
from pathlib import Path

TEXT = (
    "v0.8 \u2014 Hiccups patched. Diaphragm no longer accepts spontaneous "
    "spams from the stomach."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text out of range"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
