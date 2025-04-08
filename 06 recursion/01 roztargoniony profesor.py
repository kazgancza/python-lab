"""
Roztargniony profesor
Dostępna pamięć: 64MB
Pewien profesor, aby dostać się do swego gabinetu, musi pokonać N schodów. Profesor
pokonuje zazwyczaj jeden lub dwa schody na raz. Oblicz, na ile różnych sposobów profesor
może pokonać schody. Podaj te sposoby.
Wejście
Jedna liczba całkowita N (1 ≤ N ≤ 25) - liczba schodów.
Wyjście
Wyjście zawiera w pierwszym wierszu liczbę możliwych kombinacji, w kolejnych wierszach
wszystkie możliwe kombinacje w porządku leksykograficznym. 
"""

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

