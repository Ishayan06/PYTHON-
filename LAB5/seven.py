from functools import reduce

nums = list(map(int, input("Enter numbers separated by space: ").split()))

product = reduce(lambda x, y: x * y, nums)
print("Product:", product)
