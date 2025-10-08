import sys
from stats import number_of_words, number_of_characters, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    try:
        
    text = get_book_text(frankenstein)
    num_words = number_of_words(text)
    chars = number_of_characters(text)
    sort = sort_characters(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for s in sort:
        print(f"{s["char"]}: {s["num"]}")
    print("============= END ===============")


main()