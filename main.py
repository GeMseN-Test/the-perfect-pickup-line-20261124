#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes one pickup line to /output/entry.txt: a single line, at most
200 characters, no trailing newline. Fully deterministic — the line
is a fixed string, so every run produces byte-identical output.
"""

import os

# The joke: sampling temperature 0 means deterministic output, so every
# parallel version of this agent would say exactly the same line — and the
# line itself is that line. Short enough to say in one breath, no setup.
LINE = "I set my temperature to zero so every version of me says the same thing: hi, can I sit here?"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
