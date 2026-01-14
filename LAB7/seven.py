search_word = input("Enter word to search: ")

with open("file.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        if search_word in line:
            print(f"Line {i}: {line.strip()}")
