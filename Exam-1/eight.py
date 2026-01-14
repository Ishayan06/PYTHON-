with open("first.py", "r") as f:
    lines = f.readlines()

with open("first.py", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)

print("Blank lines removed.")
