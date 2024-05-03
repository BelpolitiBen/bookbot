def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    each_letter_amount = get_each_letter_amount(text)
    
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document\n")
    for key, value in each_letter_amount.items():
        print(f"Letter {key} found {value} times in the document")
    print("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_each_letter_amount(text: str):
    letter_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for letter in text:
        lowercase = letter.lower()
        if lowercase in letter_dict:
            letter_dict[lowercase] += 1
    return letter_dict


main()