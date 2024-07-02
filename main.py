import sys


def get_text(path) -> str:
    with open(path) as file:
        return file.read()


def count_words(text) -> int:
    words = text.split()
    return len(words)


def main() -> int:
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = count_words(text)
    print(text)
    print(word_count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
