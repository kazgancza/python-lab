from math import gcd

def lcm(a, b):
    return int((a*b)/gcd(a, b))

crossroads = int(input(""))
times=[]

for i in range(crossroads):
    times.append(int(input()))

temp=lcm(times[0]+1,times[1]+1)
for i in range(2, crossroads):
    temp=lcm(temp, times[i]+1)

print(temp-1)

