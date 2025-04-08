from math import sqrt

def is_prime(n):
    if(n<2):
        return False
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True



n = int(input(""))
result=0

if(n<4):
    print(1)
elif(is_prime(n)):
    print(1)
elif(n%2==0 and n>=4):
    print(2)
elif(n%2!=0 and is_prime(n-2)):
    print(2)
else:
    print(3)