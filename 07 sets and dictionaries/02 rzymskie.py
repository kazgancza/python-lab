"""
Na rzymskie
Dostępna pamięć: 32MB
Wczytaj liczbę zapisaną w systemie dziesiętnym i wypisz jej wartość zapisaną cyframi
rzymskimi. Wartości cyfr pojawiających się w testach przedstawione są w tabelce poniżej.
I 1
IV 4
V 5
IX 9
X 10
L 50
C 100
D 500
M 1000
Wejście
Liczba arabska n (1 ≤ n ≤ 3000).
Wyjście
Pierwszy i jedyny wiersz wyjścia powinien wypisać jedno słowo – wartość n w zapisie
rzymskim. 
"""

n = int(input())
out = ""

roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
    }

while n:
    for key in roman:
        while key <= n:
            out += roman[key]
            n -= key
            
print(out)
