n = int(input())
rocks=set()

"""
Kamienie
Dostępna pamięć: 64MB
Janek jest kolekcjonerem kamieni. Zbiera je i kataloguje, nadając każdemu unikatowy numer.
Dba o to, by każdy kamień był inny i nie pozwala, aby w kolekcji znalazły się dwa takie same.
Kiedy chodzi plażą, gdzie może znaleźć nowe okazy do swoich zbiorów, podnosi każdy
napotkany kamień, ocenia go, nadaje mu numer katalogowy i – jeśli jeszcze takiego w kolekcji
nie posiada – zabiera go. Trudno jest mu jednak szybko ocenić, czy kolejny znaleziony kamień
jest potrzebny. Pomóż mu!
Wejście
W pierwszym wierszu standardowego wejścia zapisana jest jedna liczba całkowita n
(2 ≤ n ≤ 1 000 000) oznaczająca liczbę kamieni. Kolejne n wierszy zawiera po jednej liczbie
całkowitej ki (0 ≤ ki ≤ 109
) oznaczającej numer katalogowy i-tego kamienia.
Wyjście
W n wierszach standardowego wyjścia Twój program powinien zapisać po jednej literze ‘T’ lub
‘N’, oznaczającą przydatność kamienia w kolekcji Janka.
"""

for i in range(n):
    rock = int(input())
    if rock in rocks:
        print("N")
    else:
        print("T")
    rocks.add(rock)

