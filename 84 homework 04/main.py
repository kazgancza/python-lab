def find_alphabet_order(words):
    letters = set()
    for word in words:
        for c in word:
            letters.add(c)

    graph = {}
    in_degree = {}
    for c in letters:
        graph[c] = []
        in_degree[c] = 0

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                break

    queue = []
    for c in in_degree:
        if in_degree[c] == 0:
            queue.append(c)

    order = []
    while queue:
        current = queue.pop(0)
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(order)


words = []
while True:
    line = input().strip()
    if line == '#':
        break
    words.append(line)

print(find_alphabet_order(words))
