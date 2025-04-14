import sys
from stats import get_word_count, get_characters_count, sort_character_count_dictionary

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        books = sys.argv[1:]
        for book in books:
            analyze_book(book)


def analyze_book(book_path):   
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters_count = get_characters_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_character_count_dictionary = sort_character_count_dictionary(characters_count)

    for item in sorted_character_count_dictionary:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()
