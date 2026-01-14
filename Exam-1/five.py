t = tuple(map(int, input("Enter tuple elements: ").split()))

even_tuple = tuple(x for x in t if x % 2 == 0)
print("Tuple of even numbers:", even_tuple)
