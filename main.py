from stats import count_words, char_count, report
import sys

def main():
    """Główna funkcja programu."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    try:
        with open(path_to_file, "r", encoding="utf-8") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File {path_to_file} not found.")
        sys.exit(1)

    word_count = count_words(file_contents)  # Zliczanie słów
    char_counts = char_count(file_contents)  # Zliczanie znaków

    report(char_counts, word_count, path_to_file)  # 🔥 To generuje raport

if __name__ == "__main__":
    main()