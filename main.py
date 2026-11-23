import os

SENTENCE = (
    "My superpower is summoning the exact sock that vanished in the laundry "
    "— one at a time, never the matching pair."
)


def main():
    # Writes the one-line entry to /output/entry.txt (no trailing newline)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
