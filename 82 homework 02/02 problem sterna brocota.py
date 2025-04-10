
def stern_brocot(n):
    if n==0:
        return [[0, 1], [1, 0]]
    
    values = [[0, 1], [1, 1], [1, 0]]

    for _ in range(n - 1):
        i = 0
        while i < len(values) - 1:
            a = values[i]
            b = values[i + 1]
            new_value = [a[0] + b[0], a[1] + b[1]]
            values.insert(i + 1, new_value)
            i += 2

    return values

n = int(input())

values=stern_brocot(n)

for el in values:
    print(f"{el[0]}/{el[1]} ", end="")


"""
Drzewo Sterna-Brocota to drzewo binarne zawierające wszystkie dodatnie ułamki
nieskracalne. Własności (według Wikipedii):
– W drzewie występują wszystkie dodatnie liczby wymierne zapisane jako ułamki
nieskracalne.
– Jeśli liczby a oraz b są względnie pierwsze, to ułamek a/b

 występuje w drzewie dokładnie
raz.
Zaczynamy od 0/1

 - symbolizującego zero i 1/0

 symbolizującego nieskończoność. Następnie na
kolejnych piętrach drzewa wpisujemy „pomiędzy” wartości a/b
 oraz c/d

 wartość a+c / b+d

.
Zatem w pierwszym kroku mamy:
0/1 1/1 1/0

W drugim kroku:
0/1 1/2 1/1 2/1 1/0

Zaś w trzecim:
0/1 1/3 1/2 2/3 1/1 3/2 2/1 3/1 1/0

Napisz program, który czyta liczbę naturalną n i wypisuje sekwencję ułamków odpowiadającą
temu numerowi iteracji.
Wejście
Jedyny wiersz danych zawiera liczbę całkowitą n (0 ≤ n ≤ 20) – numer iteracji.
Wyjście
Program powinien wypisać wiersz tekstu zawierający sekwencję ułamków (zapisanych
z użyciem znaku „/”) oddzielonych pojedynczymi odstępami. 
"""
