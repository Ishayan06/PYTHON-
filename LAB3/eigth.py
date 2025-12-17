arr = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter rotation value: "))

k = k % len(arr)  # handle large k

left = arr[k:] + arr[:k]
right = arr[-k:] + arr[:-k]

print("Left rotation:", left)
print("Right rotation:", right)
