n = int(input())
rocks=set()


for i in range(n):
    rock = int(input())
    if rock in rocks:
        print("N")
    else:
        print("T")
    rocks.add(rock)

