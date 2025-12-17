a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

merged = []
for x in a:
    merged.append(x)
for x in b:
    merged.append(x)

print("Merged list:", merged)
