dec = int(input(""))
validate = 0

while dec:
    temp=dec%16
    dec//=16
    if(temp>=10):
        print("TAK")
        validate=1
        break
if(validate==0):
    print("NIE")