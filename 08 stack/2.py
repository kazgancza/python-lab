def RPN(text): # reversed polish notation
    stack = []

    for action in text.split():
        try:
            stack.append(int(action))
        except ValueError:
            temp = stack.pop()
            if action == 'M':   # mnożenie (multiplication)
                stack[-1] *= temp
            elif action == 'D': # dodawanie (adding)
                stack[-1] += temp
            else:               # odejmowanie (subtracting)
                stack[-1] -= temp

    return stack[0] # returns result


n = int(input())
checks = []
for _ in range(n):
    checks.append(input().strip())

for check in checks:
    print(RPN(check))

"""Czy dodawanie, odejmowanie i mnożenie może sprawiać kłopoty? Oczywiście że nie! Dlatego
mam dla ciebie proste zadanie: dla podanego w specjalnym zapisie wyrażenia arytmetycznego
oblicz jego wartość! Specjalność tego zapisu polega na tym, że najpierw zawsze pojawiają się
argumenty, a dopiero później działania M, O lub D (mnożenie, odejmowanie lub dodawanie).
W wyrażeniu tym jednak nie musisz się martwić kolejnością działań arytmetycznych – po
prostu wykonuj je zgodnie z wejściem!
Wejście
W pierwszym wierszu wejścia znajduje się jedna liczba N (1 ≤ N ≤ 10) – liczba wyrażeń do
rozpatrzenia. W kolejnych N liniach znajdują się krótkie wyrażenia arytmetyczne. Długość
żadnego z nich nie przekracza 1000 znaków. Wyrażenia składają się wyłącznie z wartości xi
(0 ≤ xi ≤ 1015) oraz działań opisanych odpowiednimi literami.
Wyjście
W oddzielnych liniach należy wypisać N liczb całkowitych – wyniki obliczeń. Możesz założyć,
że końcowy wynik nigdy nie przekroczy |1015|. """