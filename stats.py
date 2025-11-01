def count_words(text_string):
    split_text = text_string.split()
    return len(split_text)

def count_characters(text_string):
    low = text_string.lower()
    counts = {}

    for character in low:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1
    return counts

def sort_on(items):
    return items["num"]

def sorted_list_of_dictionaries(character_dictionary):
    character_counts = []
    for key in character_dictionary:
        temp_dict = {}
        temp_dict["name"] = key
        temp_dict["num"] = character_dictionary[key]
        character_counts.append(temp_dict)
    
    character_counts.sort(reverse=True, key=sort_on)
    return character_counts
    