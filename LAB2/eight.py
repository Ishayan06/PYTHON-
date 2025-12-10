start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers:")

for num in range(start, end + 1):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)

    if total == num:
        print(num)
