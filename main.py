import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read() 

def main():
    text = get_book_text(filepath)
    word_count = count_words(text)    
    char = count_characters(text)
    sorted_chars = sort_characters(char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():  
            print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")
main()