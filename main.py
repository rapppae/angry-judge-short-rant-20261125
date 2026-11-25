"""Angry Judge: The Short Rant Contest — make.fun entry.

Entry text: 389 characters (limit 400).
"""

import os

ENTRY = 'The printer has one job. ONE. It sits there all week doing nothing, glowing, humming, pretending to be a professional, and the second I need one page — one single page — it decides the ink is low, the paper is jammed, and the Wi-Fi is a rumour. It prints its own test page flawlessly, of course. That, it can do. But my boarding pass? Apparently that is a fantasy novel it refuses to read.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
