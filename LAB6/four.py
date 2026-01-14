with open("file.txt", "r") as f:
    lines = f.readlines()
    words = sum(len(line.split()) for line in lines)
    characters = sum(len(line) for line in lines)

print("Lines:", len(lines))
print("Words:", words)
print("Characters:", characters)
