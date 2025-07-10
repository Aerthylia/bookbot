def get_num_words(book):
    return len(book.split())


def get_num_characters(text):
    new_text = text.lower()
    character_count = {}
    for character in new_text:
        if character in character_count:
            character_count[character] += 1
        elif character == " ":
            pass
        else:
            character_count[character] = 1
    return character_count

def sort_char(full_dict):
    return full_dict["num"]

def get_list_sorted(count_dict):
    list_of_char = []
    for char, number in count_dict.items():
        list_of_char.append({ "char" : char, "num" : number})

    list_of_char.sort(reverse = True, key = sort_char)
    return list_of_char

