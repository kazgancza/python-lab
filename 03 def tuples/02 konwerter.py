def convert(x, y, z):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y=int(y)
    z=int(z)

    if y!=10:
        dec=0
        j=0
        for i in range(len(x)-1, -1, -1):
            if x[i].upper() in letters:
                temp=letters.find(x[i].upper())+10
            else:
                temp=int(x[i])
            dec+=temp*(pow(y, j))
            j+=1
    else:
        dec=int(x)

    if z!=10:
        result=""
        while dec:
            temp=dec%z
            if temp>=10:
                result+=letters[temp-10]
            else:
                result+=str(temp)
            dec//=z
        return result[::-1]
    else:
        return dec

a, b, c = input().split()

print(convert(a, b, c))