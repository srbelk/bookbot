def count_words(text):
    list_of_words = text.split()
    num_words = 0
    for word in list_of_words:
        num_words +=1
    return num_words

def count_characters(text):
    characters = list(text.lower())
    dict_of_characters = {}
    
    for character in characters:
        if character in dict_of_characters:
            dict_of_characters[character] += 1 
        else:
            dict_of_characters[character] = 1    
    return dict_of_characters

def sort_characters(dict_of_characters):
    list_of_char = []
    for char, count in dict_of_characters.items():
        list_of_char.append({"char": char, "count": count})

    def sort_on(dict_of_characters):
        return dict_of_characters["count"]

    list_of_char.sort(reverse = True, key = sort_on )
    return list_of_char