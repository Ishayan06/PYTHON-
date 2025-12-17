a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

common = []
for x in a:
    if x in b and x not in common:
        common.append(x)

print("Common elements:", common)
