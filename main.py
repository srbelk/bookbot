from stats import count_words
from stats import count_characters

filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read() 

def main():
    text = get_book_text(filepath)
    count_words(text)    
    char = count_characters(text)
    print(char)
main()