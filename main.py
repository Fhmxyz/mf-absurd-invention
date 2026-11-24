import os

# One-Sentence Absurd Invention Pitch — one sentence, at most 220 chars.
# Annoyance: walking into a room and forgetting why. Invention: a doormat
# that replays the thought you were just having.
LINE = (
    "Introducing the Doorway Rewind, a doormat that records your last "
    "thought and replays it as you cross the threshold, for everyone who "
    "has ever opened the fridge hoping it remembered why they came."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
