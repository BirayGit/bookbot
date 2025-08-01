def get_book_text(f_path):
    with open(f_path) as file:
        file_contents = file.read()
        return file_contents
    
def main():
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    print(book)

main()