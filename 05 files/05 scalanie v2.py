file1 = open("05 class\dane1.txt", "r")
file2 = open("05 class\dane2.txt", "r")
file3 = open("05 class\wynik.txt", "a")

left = file1.readlines()
right = file2.readlines()

i=0
j=0
output=""


while i<len(left) and j<len(right):
    if int(left[i])<int(right[j]):
        output+=left[i].strip()+" "
        i+=1
    elif int(left[i])>int(right[j]):
        output+=right[j].strip()+" "
        j+=1
    else:
        output+=left[i].strip() + " " + right[j].strip() + " "
        i+=1
        j+=1        

while i<len(left):
    output+=left[i].strip() + " "
    i+=1
while j<len(right):
    output+=right[j].strip() + " "
    j+=1

file3.write(output)


file1.close()
file2.close()
file3.close()
