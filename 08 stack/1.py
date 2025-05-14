def is_bracket_ok(text):
    
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    stack = []

    for letter in text:
        if letter in brackets.values():
            stack.append(letter)
        else:
            if not stack or not stack.pop() == brackets[letter]:
                return False
    
    return not stack # for True stack has to be empty

        
            




n = int(input())
checks = []
for _ in range(n):
    checks.append(input().strip())

for check in checks:
    print("T") if is_bracket_ok(check) else print("N")

"""
Kiedy czasem dostaniemy do obliczenia wartość wyrażenia arytmetycznego, już sam pierwszy
rzut oka sprawia, że mamy ochotę rozwiązać to zadanie pojutrze i mieć dzięki temu dwa dni
wolnego. Najgorsze są jednak przypadki takie, w których po długich i wyczerpujących
obliczeniach dowiadujesz się, że otrzymałeś błędny zapis wyrażenia!
Napisz program, który sprawdzi, czy dla podanego zapisu użyte w nim nawiasy umieszczone
są w możliwy do przyjęcia sposób (zachowana jest właściwa kolejność nawiasów
otwierających i zamykających, każdy nawias musi być sparowany z nawiasem tego samego
typu).
Wejście
W pierwszym wierszu wejścia znajduje się jedna liczba n (1 ≤ n ≤ 10). W kolejnych n wierszach
znajduje się po jednym wyrażeniu złożonym z nie więcej niż 1 000 000 znaków. Wyrażenie
składa się z nawiasów: (, ), { ,}, [, ], <, >.
Wyjście
W n wierszach standardowego wyjścia Twój program powinien zapisać jedną literę ‘T’ lub ‘N’,
oznaczającą poprawność zapisu nawiasów w wyrażeniu arytmetycznym. 
"""