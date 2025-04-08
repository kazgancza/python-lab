"""
Dziewczynki
Limit pamięci: 32 MB
Chłopcy i dziewczynki ustawili się w szereg, osoba tuż obok osoby. Zastanawiamy się teraz, ilu minimalnie chłopców musi usunąć się z szeregu, aby pod rząd stało  dziewczynek, jedna tuż obok drugiej i pomiędzy nimi wszystkimi nie stał żaden chłopiec.

Wejście
Pierwszy wiersz standardowego wejścia zawiera dwie liczby całkowite  (), oznaczające odpowiednio liczbę osób ustawionych w szeregu oraz liczbę dziewczynek, jakie chcemy, aby stały pod rząd . Kolejny wiersz wejścia zawiera  liczb całkowitych { lub }, oznaczających kolejne osoby ustawione w szeregu:  - oznacza dziewczynkę,  - chłopca.

Wyjście
Pierwszy i jedyny wiersz standardowego wyjścia powinien zawierać jedną liczbę całkowitą, oznaczającą minimalną liczbę chłopców, którzy powinni usunąć się z szeregu, lub jedno słowo 'NIE', gdy nie da się usunąć chłopców tak, aby  dziewczynek stało pod rząd.
"""

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
