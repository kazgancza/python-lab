n = int(input())

logins = {}
output = ""

for _ in range(n):
    login = input().strip()
    
    if login not in logins.keys():
        output += "OK\n"
        logins[login] = 1
    else:
        output += login + str(logins[login]) + "\n"
        logins[login] += 1

""" Wynik można wyślwietlać od razu w pętli,
celem zaoszczędzenia pamięci,
ale wtedy wejście miesza się z wyjściem"""
print(output)

"""
Pan Integer pracuje nad otwarciem nowego portalu internetowego.
Jednym z elementów systemu jest poczta elektroniczna.
Pan Integer rozdzielił już pracę pomiędzy zespoły.
Twoim zadaniem będzie opracowanie modułu rejestracji loginów.
Moduł rejestracji otrzymuje proponowany login.
Jeśli taka nazwa jeszcze nie wystąpiła w bazie,
moduł wysyła informację OK do użytkownika i zapisuje go w bazie. Jeśli podana nazwa już występuje w bazie, wówczas tworzony jest nowy login, system wysyła go do użytkownika i zapisuje w bazie. Nowy login tworzony jest przez dodanie kolejnego jak najmniejszego numeru do proponowanej przez użytkownika nazwy.

Wejście
W pierwszej linii wejścia znajduje się jedna liczba całkowita n
(1 n 5-105), oznaczająca liczbę rozpatrywanych loginów.
W kolejnych n liniach znajdują się rozpatrywane loginy.
Każdy login składa się wyłącznie z małych liter alfabetu
łacińskiego i jest nie dłuższy niż 30 znaków.

Wyjście
Na wyjściu dla każdego loginu wypisywana jest odpowiedź wysyłana dla użytkownika: OK - w przypadku udanej rejestracji, lub nowy login dla już istniejącej nazwy."""