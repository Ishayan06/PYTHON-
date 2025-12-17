arr = list(map(int, input("Enter list elements: ").split()))
unique = []

for x in arr:
    if x not in unique:
        unique.append(x)

print("Without duplicates:", unique)
