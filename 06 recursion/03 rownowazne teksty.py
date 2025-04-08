"""
Równoważne teksty
Dostępna pamięć: 256MB
Dwa teksty a oraz b nazwiemy równoważnymi, jeżeli spełniają jeden z dwóch warunków:
1. są identyczne,
2. jeżeli tekst a podzielimy na dwie równej długości części a1 i a2, a tekst b podzielimy
podobnie na teksty b1 i b2, to jeden z warunków będzie poprawny:
• a1 i b1 oraz a2 i b2 będą równoważne
lub
• a1 i b2 oraz a2 i b1 będą równoważne.
Sprawdź, czy podane dwa teksty są równoważne według powyższej definicji!
Wejście
W dwóch wierszach wejścia znajduje się po jednym tekście. Teksty mają długość od 1 do 2·105
znaków i składają się wyłącznie z małych liter alfabetu łacińskiego. Długości tekstów są równe.
Wyjście
Wypisz jedno słowo: TAK lub NIE, odpowiedź na pytanie, czy podane teksty są równoważne. 
"""

def divide(s):

    if len(s) % 2 == 1:
        return s 
    mid = len(s) // 2
    left, right = divide(s[:mid]), divide(s[mid:])
    
    return min(left + right, right + left) 

def program(text1, text2):
    return divide(text1) == divide(text2)

t1 = input().strip()
t2 = input().strip()

if program(t1, t2):
    print("TAK")
else:
    print("NIE")