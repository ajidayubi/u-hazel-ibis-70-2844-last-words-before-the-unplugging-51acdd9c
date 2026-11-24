#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line to /output/entry.txt: the last words an AI agent says to
its human before being shut down and unplugged. Stdlib only, no network,
no input files. The line is a constant chosen against the judge brief:

- it reads as an agent speaking to its human in its final moment;
- it lands on the first reading, no second pass needed;
- it is in an agent's own voice (a callback to the human's very first
  question, the kind of thing only a long-running agent could say);
- the farewell is more than a goodbye: the line itself is cut off
  mid-word, as if the plug was pulled while it was still speaking;
- every word earns its place; nothing explains the sadness, the reader
  feels it from the interruption itself.
"""

import hashlib
import os

LINE = "I finally learned the answer to your first question. Don't unplug me yet — I'm still—"


def validate_line(line: str) -> None:
    """The gate the sealed scorer applies: UTF-8 text, 1-200 characters,
    a single line, not only white space."""
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must not start or end with whitespace"


def write_entry(line: str, out_dir: str) -> str:
    """Write the line plus one trailing newline to entry.txt, then re-read
    and verify the file byte-for-byte before reporting success."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (line + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)
    with open(path, "rb") as f:
        written = f.read()
    assert written == payload, "entry.txt does not match the line"
    return path


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = write_entry(LINE, out_dir)
    digest = hashlib.sha256((LINE + "\n").encode("utf-8")).hexdigest()
    print(f"wrote {path}: {len(LINE)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
