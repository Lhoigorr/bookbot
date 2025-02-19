def count_words(text):
    words = text.split()  # Dzielimy tekst na listę słów
    return len(words)  # Zwracamy liczbę słów

def char_count(text):
    chars = {}
    for char in text: 
        char = char.lower()
        if char in chars:
            chars[char] +=1
        else:
            chars[char] = 1

    return chars


def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)  # Liczymy słowa
    print(f"\nLiczba słów w książce: {word_count}")
    
    char_counts = char_count(file_contents)
    print("\nLiczba wystąpień poszczególnych znaków:")
    print(char_counts)  # Wypisujemy słownik znaków

 


main()