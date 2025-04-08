from stats import get_num_words, get_letter_count
import sys


def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_name = sys.argv[1]
    text = get_book_text(book_name)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    letter_cnt = get_letter_count(text)
    print("--------- Character Count -------")
    for letter in letter_cnt:
        print(f"{letter}: {letter_cnt[letter]}")


if __name__ == "__main__":
    main()
