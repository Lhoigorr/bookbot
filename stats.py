def count_words(text):
    """Zlicza słowa w tekście."""
    words = text.split()
    return len(words)

def char_count(text):
    """Zlicza wystąpienia każdego znaku."""
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def report(chars, word_count, path_to_file):
    """Generuje i drukuje raport dla podanej książki."""
    print(f"\n--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    char_list = []  # Lista dla liter alfabetu

    for char, count in chars.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=lambda d: d["num"])  # Sortowanie malejące
    
    for item in char_list:
        print(f"{item['char']}: {item['num']}")

    print("--- End report ---\n")