def program(n, solutions=[]):
    if n == 0:
        results.append(solutions)
        return
    if n >= 1:
        program(n - 1, solutions + [1])
    if n >= 2:
        program(n - 2, solutions + [2])


global results
results = []

N = int(input())
program(N)

print(len(results))
for way in results:
    print(" ".join(map(str, way)))

