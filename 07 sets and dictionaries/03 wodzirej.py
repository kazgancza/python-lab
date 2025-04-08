n, m = map(int, input().split())

relations = {i: [] for i in range(1, n + 1)}
likes = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())

    relations[u].append(v)
    relations[v].append(u)

    likes[u] += 1
    likes[v] += 1


max_likes = -1
leader = -1

for i in range(1, n + 1):
    if likes[i] > max_likes or (likes[i] == max_likes and i < leader):
        max_likes = likes[i]
        leader = i


print(leader)
print(" ".join(map(str, sorted(relations[leader]))))