import math


def isprime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False
            return True

inputnumber=int(input("Enter the Number : "))

if isprime(inputnumber):
    print(f"{inputnumber} is the prime number")
else:
    print(f"{inputnumber} is a composite number")
