from stats import count_words, count_characters, sorted_list_of_dictionaries
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])
    #text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    
    character_counts = count_characters(text)
    #print(character_counts)
    sorted_dictionaries = sorted_list_of_dictionaries(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_dictionaries:
        if (char_dict["name"]).isalpha():
            print(f"{char_dict["name"]}: {char_dict["num"]}")
    print("============= END ===============")

main()