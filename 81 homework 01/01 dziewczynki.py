def boys_to_remove(n, k, row):

    result=1000001 # >10^6
    girl_pos=[i for i in range(n) if row[i] == 0]

    if len(girl_pos) < k:
        return "NIE"

    for i in range(len(girl_pos)-k+1):
        boys=girl_pos[i+k-1]-girl_pos[i]+1-k
        if boys<result:
            result=boys

    if result>=1000001:
        return "NIE"
    return result


n, k = map(int, input().split())
row = list(map(int, input().split()))

print(boys_to_remove(n, k, row))
