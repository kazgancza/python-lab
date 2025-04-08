"""
Wodzirej
Dostępna pamięć: 32MB
Janek urządził imprezę. Tym razem postanowił wybrać jedną osobę, która będzie decydowała
o przebiegu zabaw – wodzireja. Chciałby, aby osoba ta była lubiana przez jak największą
grupę uczestników spotkania. Pomóż wskazać mu tę osobę oraz grono osób, które ją lubią.
Wejście
Pierwszy wiersz danych zawiera dwie liczby całkowite n i m, odpowiednio liczbę osób
biorących udział w przyjęciu oraz liczbę wzajemnych sympatii (2 ≤ n ≤ 10 000,
2 ≤ m ≤ 1 000 000). W kolejnych m liniach znajdują się po dwie liczby całkowite ui i vi
(1 ≤ ui, vi ≤ 10 000) – informacje o parach osób, które się lubią wzajemnie.
Wyjście
Program powinien wypisać w pierwszym wierszu jedną liczbę – najbardziej lubianą osobę na
przyjęciu (wodzireja). Jeśli jest więcej takich osób – tę o najmniejszej liczbie porządkowej.
W drugiej linii program powinien wypisać w kolejności rosnącej wszystkie osoby, które lubią
wodzireja. 
"""

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