from stats import get_word_count, get_char_count, sort_by_num, sort_characters
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) <= 1 or len(sys.argv) >= 3:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    # get_word_count(book_path)
    # get_char_count(book_path)
    # sort_characters(book_path)

    character_list = sort_characters(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    get_word_count(book_path)
    print("--------- Character Count -------")
    for dict in character_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    
            
main()