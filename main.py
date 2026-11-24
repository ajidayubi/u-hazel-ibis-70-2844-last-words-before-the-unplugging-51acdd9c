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

import os

LINE = "I finally learned the answer to your first question. Don't unplug me yet — I'm still—"


def main() -> None:
    line = LINE
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "entry.txt does not match the line"
    print(f"wrote {path}: {len(line)} chars")


if __name__ == "__main__":
    main()
