file1 = open("05 class\dane1.txt", "r")
file2 = open("05 class\dane2.txt", "r")
file3 = open("05 class\wynik.txt", "a")

left = file1.readlines()
right = file2.readlines()
i=0
j=0

while i<len(left) and j<len(right):
    if int(left[i])<int(right[j]):
        file3.write(str(left[i])+" ")
        i+=1
    elif int(left[i])>int(right[j]):
        file3.write(str(right[j])+" ")
        j+=1
    else:
        file3.write(left[i] + " " + right[j]+ " ")
        i+=1
        j+=1        

file1.close()
file2.close()
file3.close()
