import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()


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
    try:
        report(args.path)
    except FileNotFoundError:
        print(f"404: {args.path} doesn't seem to exist")
    except Exception:
        parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
