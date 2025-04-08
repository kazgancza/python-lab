x = int(input(""))
a = 0

while(x):
    x//=2
    a+=1
    if(x==0):
        break

print(a)
