from pathlib import Path
import string
from collections import Counter

print("\n--- Word Counter ---")

filename = input("Enter the file name: ")
file_path = Path(__file__).parent / filename

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    text = text.lower()

    for symbol in string.punctuation:
        text = text.replace(symbol, "")

    words = text.split()
    word_count = Counter(words)

    print("\nTotal words:", len(words))
    print("\nWord Frequency:")

    if not words:
        print("The file is empty.")
    else:
        for word, count in word_count.most_common():
            print(word, ":", count)

except FileNotFoundError:
    print("File not found. Please check the file name.")

except OSError:
    print("Unable to read the file.")
