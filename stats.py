#Calculates the total number of words in a given text.
def word_count(book_text):
    words = book_text.split()
    w_count = len(words)
    print(f"Found {w_count} total words")

# Counts the characters in a text and stores it in a dictionary
def letter_count(book_text):
    letters = {}
    book_text = book_text.lower()

    for letter in book_text:
        letters[letter] = letters.get(letter, 0) + 1
    return letters

# Takes a dictionary as input. Sorts it by value then prints the letters
def sorted_letter_count(letters):
    sorted_letters = {k:v for k, v in sorted(letters.items(), key=lambda item:item[1], reverse=True)}

    for key, value in sorted_letters.items():
        if key.isalpha():
            print(f"{key}: {value}")
