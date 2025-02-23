from stats import count_words
from stats import char_count
from stats import report

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)  # Liczymy słowa
    char_counts = char_count(file_contents)  # Liczymy znaki

    report(char_counts, word_count, path_to_file)


main()