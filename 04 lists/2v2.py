a, b = map(int, input().split())
c, d = map(int, input().split())
h, w = map(int,input().split())
screen = [list(map(int, input().split())) for _ in range(h)]

searched = a*b*c*d
result=0

for i in range(h-1):
    for j in range(w-1):
        if screen[i][j]*screen[i+1][j]*screen[i][j+1]*screen[i+1][j+1]==searched:
            result+=1
                
print(result)