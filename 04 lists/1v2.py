people, relations = map(int, input().split())
a=[]
b=[]
results=[0]*people

for i in range(relations):
    x, y = input().split()
    a.append(int(x))
    b.append(int(y))

for i in range(relations):
    results[a[i]-1]-=1
    results[b[i]-1]+=1

max_value = max(results)
max_index = max(i for i, val in enumerate(results) if val == max_value)
print(max_index + 1, max_value)