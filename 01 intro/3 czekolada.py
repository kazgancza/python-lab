m, n = map(int, input().split())
k = int(input())
if (k%m == 0 or k%n == 0) and k<=m*n:
    print("TAK")
else:
    print("NIE")
