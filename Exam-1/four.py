lst = list(map(int, input("Enter list elements: ").split()))
result = []

for i in lst:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)
