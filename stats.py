def count_words(text):
    list_of_words = text.split()
    num_words = 0
    for word in list_of_words:
        num_words +=1
    print(f"{num_words} words found in the document")

def count_characters(text):
    characters = list(text.lower())
    dict_of_characters = {}
    
    for character in characters:
        if character in dict_of_characters:
            dict_of_characters[character] += 1 
        else:
            dict_of_characters[character] = 1    
    return dict_of_characters