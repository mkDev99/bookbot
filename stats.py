def get_word_count(text: str):
    words = text.split()
    return len(words)

def get_characters_count(text: str):
    words = text.split()
    unique_characters = set()
    characters_count = {}

    for word in words:
        for character in word:
            character = character.lower()
            if character not in unique_characters:
                unique_characters.add(character)
                characters_count[character] = 1
            else:
                characters_count[character] += 1

    return characters_count

def sort_character_count_dictionary(characters_count: dict):
    unsorted_list = []

    for key, value in characters_count.items():
        unsorted_list.append({"character": key, "num": value})
    
    

    def sort_on(dict):
        return dict["num"]

    unsorted_list.sort(reverse=True, key=sort_on)
    sorted_list = unsorted_list
    del unsorted_list
    
    return sorted_list
