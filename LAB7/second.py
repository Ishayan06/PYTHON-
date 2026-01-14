word = input("Enter word to search: ")

with open("file.txt", "r") as f:
    found = False
    for line_no, line in enumerate(f, start=1):
        if word in line:
            print(f"Word found at line {line_no}: {line.strip()}")
            found = True

if not found:
    print("Word not found.")
