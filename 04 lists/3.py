n = int(input())
disp = [list(map(int, input().split())) for _ in range(n)]

disp.sort()

min_diff = float('inf')

for i in range(1, n):
    diff = max(0, disp[i][0] - disp[i - 1][1])

    if diff < min_diff:
        min_diff = diff

print(min_diff)