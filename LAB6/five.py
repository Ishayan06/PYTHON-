import string

with open("file.txt", "r") as f:
    text = f.read()

clean_text = text.translate(str.maketrans("", "", string.punctuation))

with open("clean_file.txt", "w") as f:
    f.write(clean_text)
