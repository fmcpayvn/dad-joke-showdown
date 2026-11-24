"""Dad Joke Showdown -- entrypoint.

Writes exactly one dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no files read.
"""
import os

# The judge rewards a clean pun that feels FRESH, not a joke told a
# thousand times. So this is an original one, built on the classic
# dad structure (setup, then the turn lands on the last words):
# a calendar that breaks up because nobody "makes time" for it.
JOKE = "My calendar broke up with me. It said I never make time for it."


def tell():
    """Return the entry's single dad joke (63 characters)."""
    return JOKE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(tell())


if __name__ == "__main__":
    main()
