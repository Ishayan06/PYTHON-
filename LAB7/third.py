with open("source.txt", "r") as src:
    with open("destination.txt", "w") as dest:
        dest.write(src.read())

print("File copied successfully.")
