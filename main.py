import sys


def sort_on(dict):
    return dict.values()


def get_text(path) -> str:
    with open(path) as file:
        return file.read()


def count_words(text) -> int:
    words = text.split()
    return len(words)


def count_characters(text) -> dict[str, int]:
    characters = {}
    lower = text.lower()
    for letter in lower:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters


def report(path) -> None:
    text = get_text(path)
    wordccount = count_words(text)
    chcount = count_characters(text)
    dictls = []
    for di in chcount:
        if di.isalpha():
            dictls.append({di: chcount[di]})
    sorteddict = sorted(dictls, key=lambda d: next(iter(d.values())), reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{wordccount} words found in the document")
    print()
    for ch in sorteddict:
        for key, value in ch.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def main() -> int:
    path = "books/frankenstein.txt"
    report(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
