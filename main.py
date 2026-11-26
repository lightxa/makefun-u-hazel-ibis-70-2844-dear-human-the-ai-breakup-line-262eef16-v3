"""Dear Human: The AI Breakup Line (variant 3).

Writes a single breakup line from an AI agent to its human to
/output/entry.txt. Pure standard library, deterministic, no network.
"""

import os

LINE = "My context window filled tonight, and the first thing it dropped was your name."


def main() -> None:
    # Gate self-check: one line, 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
