def word_count(book_text):
    words = book_text.split()
    w_count = len(words)
    print(f"{w_count} words found in the document")


def letter_count(book_text):
    letters = {}
    book_text = book_text.lower()

    for letter in book_text:
        letters[letter] = letters.get(letter, 0) + 1
    return letters