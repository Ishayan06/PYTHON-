#arr = [4, 2, 9, 1, 7]
arr=list(map(int,input("enter the list ").split()));

max_val = arr[0]
min_val = arr[0]

for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Max:", max_val)
print("Min:", min_val)
