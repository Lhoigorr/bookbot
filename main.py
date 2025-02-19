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

def report(chars, word_count, path_to_file):
    print(f"\n--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    char_list = []  # # Tworzymy pustą listę słowników tylko dla liter alfabetu

    for char, count in chars.items(): # Pętla po każdym elemencie w słowniku chars
        if char.isalpha():   # Sprawdzamy, czy znak 'char' jest literą alfabetu
            char_list.append({"char": char, "num": count}) # Jeśli tak, dodajemy słownik do char_list
    
    
    char_list.sort(reverse=True, key=lambda d: d["num"]) # Sortujemy listę malejąco według liczby wystąpień

    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times") # Drukujemy wyniki w odpowiednim formacie

    print("--- End report ---\n")
    

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)  # Liczymy słowa
    char_counts = char_count(file_contents)  # Liczymy znaki

    report(char_counts, word_count, path_to_file)


main()