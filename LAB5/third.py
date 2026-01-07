nums = list(map(int, input("Enter numbers separated by space: ").split()))

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_nums)
