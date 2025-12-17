arr = list(map(int, input("Enter list elements: ").split()))
key = int(input("Enter element to count: "))

count = 0
for x in arr:
    if x == key:
        count += 1

print("Occurrences:", count)
