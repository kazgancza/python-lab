import time
import random
import bisect

def lds_n2(arr):
    n = len(arr)
    if n == 0:
        return []
    
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    max_len = max(dp)
    max_idx = dp.index(max_len)
    
    result = []
    current = max_idx
    while current != -1:
        result.append(arr[current])
        current = parent[current]
        
    return result[::-1]


def lds_nlogn(arr):
    tails = []
    indices = []
    parent = [-1] * len(arr)
    
    for i, num in enumerate(arr):
        idx = bisect.bisect_left(tails, -num)
        if idx == len(tails):
            tails.append(-num)
            indices.append(i)
        else:
            tails[idx] = -num
            indices[idx] = i
        parent[i] = indices[idx-1] if idx > 0 else -1
    
    result = []
    k = indices[-1] if indices else -1
    while k >= 0:
        result.append(arr[k])
        k = parent[k]
    
    return result[::-1]


big_arr = [random.randint(1, 10_000) for _ in range(100_000)]


start = time.time()
result_n2 = lds_n2(big_arr)
time_n2 = time.time() - start


start = time.time()
result_nlogn = lds_nlogn(big_arr)
time_nlogn = time.time() - start

print(f"Czas O(n²): {time_n2:.2f}s, Długość: {len(result_n2)}")
print(f"Czas O(n log n): {time_nlogn:.5f}s, Długość: {len(result_nlogn)}")
