import sys
from stats import word_count, letter_count, sorted_letter_count

def get_book_text(f_path):
    with open(f_path) as file:
        file_contents = file.read()
        return file_contents

def print_book(book_text, file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print(f"----------- Word Count ----------")
    word_count(book_text)
    letters = letter_count(book_text)
    print(f"--------- Character Count -------")
    sorted_letter_count(letters)
    print("============= END ===============")

# Make sure the user provided a path for the text book.
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    print_book(book_text, file_path)


main()