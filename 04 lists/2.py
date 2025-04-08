a, b = input().split()
a=int(a)
b=int(b)

c, d = input().split()
c=int(c)
d=int(d)

total=a*b*c*d

height, width = input().split()
height=int(height)
width=int(width)

image=[[0]*width]*height

for i in range(height):
    image[i]=input().split()
    
result=0

for i in range(height-1):
    for j in range(width-1):
        if image[i][j]==a or image[i][j]==b or image[i][j]==c or image[i][j]==d:
            if image[i][j]*image[i+1][j]*image[i][j+1]*image[i+1][j+1]==total:
                result+=1

print(result)
