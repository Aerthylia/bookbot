import sys

chosen_book = ""
num_words = 0

def get_book_text(book_path):
    with open(book_path) as book :
        book_contents = book.read()
        return book_contents

from stats import get_num_words
from stats import get_num_characters
from stats import get_list_sorted

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        chosen_book = sys.argv[1]


    chosen_book_content = get_book_text(chosen_book)
    num_words = get_num_words(chosen_book_content)
    final_character_count = get_num_characters(chosen_book_content)
    list_to_display = get_list_sorted(final_character_count)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {chosen_book}" )
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ( "--------- Character Count -------")
    for dictionnary in list_to_display:
        print (f"{dictionnary["char"]}: {dictionnary["num"]}")
    print ("============= END ===============")


main()
