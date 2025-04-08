people, relations = input().split()

a=[]
b=[]

for i in range(int(relations)):
    x, y = input().split()
    a.append(int(x))
    b.append(int(y))

knows=[0]*int(people)

for i in range(int(people)):
    if a[i]==i+1:
        knows[i]+=1

is_known=[0]*int(people)

for i in range(int(people)):
    if b[i]==i+1:
        is_known+=1

diff=[0]*int(people)

for i in range(int(people)):
    diff[i]=knows[i]-is_known[i]

print(diff.index(max(diff))+1, max(diff))
