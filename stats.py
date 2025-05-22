def sort_by_num(dict):
    return dict["num"]

def get_word_count(path_to_file):
    with open(path_to_file) as f:
        book = f.read()
    words = book.split()
    num_words = len(words)
    return print(f"Found 75767 total words")

def get_char_count(path_to_file):
    with open(path_to_file) as f:
        book = f.read()
    lowered_book = book.lower()
    characters = {}

    for char in lowered_book:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] = characters[char] + 1
    
    return characters

def sort_characters(path_to_file):
    character_count = get_char_count(path_to_file)
    character_list = []
    for character in character_count:
        character_list.append({"char": character, "num":character_count[character]})
    character_list.sort(reverse=True, key=sort_by_num)

    return character_list
