def fib(n):
    n = int(n)
    a=0
    b=1
    if n==a:
        return a
    if n==b:
        return b
    
    while n>=2:
        temp=b
        b+=a
        a=temp
        n-=1
    return b


number = input()
print(fib(number))