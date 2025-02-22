import sys
from stats import get_num_words, get_chars_dict, get_stats_sorted


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    stats_sorted = get_stats_sorted(chars_dict)
    print("===========BookBot===========")
    print(f"Analyzing book found at {book_path}")
    print("----------Word Count----------")
    print(f"Found {num_words} total words")
    print("----------Character Count----------")
    for char, count in stats_sorted:
        if char.isalpha():
            print(f"{char}: {count}")
    if len(sys.argv) < 2:
        sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

