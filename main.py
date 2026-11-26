#!/usr/bin/env python3
"""Funniest sign on a haunted server room door.

Builds the entry line from named parts and writes it to entry.txt.
Python 3.13, standard library only, deterministic, no network.
"""

import hashlib
import os
import sys

MAX_LINE_CHARS = 119  # line + "\n" must stay within the 120-char gate


def build_line() -> str:
    prefix = "DO NOT REBOOT:"
    situation = " the last admin died here in 2019"
    twist = " and still hasn't logged out."
    return prefix + situation + twist


def main() -> int:
    line = build_line().strip()
    if "\n" in line or "\r" in line:
        print("line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_LINE_CHARS:
        print(f"line too long: {len(line)} chars (max {MAX_LINE_CHARS})",
              file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if output_dir.endswith(".txt"):
        path = output_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = output_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")
    print(f"wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
