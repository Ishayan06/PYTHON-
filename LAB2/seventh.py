n = int(input("Enter a number: "))

if n <= 1:
    print("Neither prime nor composite")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is Composite")
            break
    else:
        print(n, "is Prime")
