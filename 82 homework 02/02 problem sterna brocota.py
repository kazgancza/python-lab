n = int(input())

values = ["0/1", "1/1", "1/0"]



for i in range((n-1)*2):


    a = int(values[i].split("/")[0])
    b = int(values[i].split("/")[1])
    c = int(values[i+1].split("/")[0])
    d = int(values[i+1].split("/")[1])

    values.insert(i*2+1, str(a+c)+"/"+str(b+d))

print(values)