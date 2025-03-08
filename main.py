filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read() 

   

def main():
    text = get_book_text(filepath)

    def count_words(text):
        list_of_words = text.split()
        num_words = 0
        for word in list_of_words:
            num_words +=1
        print(f"{num_words} words found in the document")
    
    count_words(text)    
main()