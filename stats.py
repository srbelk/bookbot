def count_words(text):
    list_of_words = text.split()
    num_words = 0
    for word in list_of_words:
        num_words +=1
    print(f"{num_words} words found in the document")