def is_armstrong(num):
    temp = num
    n = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10

    return total == num

num = int(input("Enter a number: "))
print("Armstrong number" if is_armstrong(num) else "Not an Armstrong number")
