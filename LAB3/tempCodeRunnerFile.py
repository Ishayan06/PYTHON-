arr = list(map(int, input("Enter list elements: ").split()))

print("Ascending:", sorted(arr))
print("Descending:", sorted(arr, reverse=True))
