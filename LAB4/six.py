d = {3: 40, 1: 20, 2: 10}

print("Sorted by keys:")
for k in sorted(d):
    print(k, d[k])

print("Sorted by values:")
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)
