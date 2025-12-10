s = input("Enter a string: ")

rev = ""
for ch in s:
    rev = ch + rev   # prepend each character

print("Reversed string:", rev)
