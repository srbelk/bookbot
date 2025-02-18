def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()

    print("--- Begin report of books/frankenstein.txt ---") 

    def count_words():
        num = 0
        for word in words:
            num += 1 
        print(f"{num} words found in the document")
    count_words()

    def count_characters():
        letters = {}
        count = 1
        franken_str = file_contents.lower()
        for chtr in franken_str:
            if chtr not in letters:
                letters[chtr] = count
            else:
                letters[chtr] += 1         
        print(letters)    
    count_characters()
    
    
                     
main() 