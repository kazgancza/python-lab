def longest_decreasing_subsequence(arr):
    import bisect
    tails = []
    indices = []
    parent = []
    
    for i, num in enumerate(arr):
        idx = bisect.bisect_left(tails, -num)
        if idx == len(tails):
            tails.append(-num)
            indices.append(i)
        else:
            tails[idx] = -num
            indices[idx] = i
        parent.append(indices[idx-1] if idx > 0 else -1)

    result = []
    k = indices[-1] if indices else -1
    while k >= 0:
        result.append(arr[k])
        k = parent[k]
    return result[::-1]

# Sprawdzenie na przykładowych danych
example = [9, 4, 2, 5, 4, 3]
result = longest_decreasing_subsequence(example)
print(f"Długość: {len(result)}\n{result}")


