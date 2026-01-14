from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().lower().split()

word_count = Counter(words)

with open("word_count.txt", "w") as f:
    for word, count in word_count.items():
        f.write(f"{word}: {count}\n")
