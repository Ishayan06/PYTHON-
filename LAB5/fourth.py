nums = list(map(int, input("Enter numbers separated by space: ").split()))

def stats(nums):
    total = sum(nums)
    avg = total / len(nums)
    return total, avg, max(nums), min(nums)

print("Sum, Avg, Max, Min:", stats(nums))
