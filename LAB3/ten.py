def factorial (n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans
n=int(input("enter the number "))
result=factorial(n)
print(result)