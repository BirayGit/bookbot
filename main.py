from stats import word_count, letter_count

def get_book_text(f_path):
    with open(f_path) as file:
        file_contents = file.read()
        return file_contents 
    
def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count(book_text)
    letters = letter_count(book_text)

    for key, value in letters.items():
        print(f"'{key}': {value}")

main()