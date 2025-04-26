n = int(input().strip())

kids = [i for i in range(1, n+1)]

sequences = []
for _ in range(n-1):
    sequences.append(int(input()))

move_right = True
holds_ball = 0

for move in sequences:
    if move_right:
        holds_ball += move
        holds_ball %= n
        kids.pop(holds_ball)
        n -= 1
        holds_ball -= 1
        move_right = False

    else:
        holds_ball -= move
        holds_ball %= n
        kids.pop(holds_ball)
        n -= 1
        move_right = True

print(kids[0])
