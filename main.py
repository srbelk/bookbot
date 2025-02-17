def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)

    words = file_contents.split() 

    def count_words():
        num = 0
        for word in words:
            num += 1 
        print(num)
    count_words()

    def count_characters():
        franken_str = file_contents.lower()
        
    count_characters()                     
main() 