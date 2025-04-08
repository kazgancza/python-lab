"""
Super idol
Sława to ciekawa sprawa. Jeżeli jesteś sławny to dużo ludzi zna
Ciebie, ale Ty ich wcale nie musisz znać. Super idol to ktoś, u kogo ta
różnica między tymi, którzy go znają a tymi, których on zna jest największa.
Napisz program, który dla poniższych danych wskaże super idola.
Wejście
W pierwszym wierszu wejścia będą podane dwie liczby całkowite L, R
(5 <= L <= 10000, 10 <= R <= 1000000) oznaczające odpowiednio ilość ludzi
w danej grupie oraz ilość relacji „ktoś kogoś zna” między nimi. W kolejnych
R wierszach będziemy mieli dwie liczby A i B (1 <= A, B <= L) oddzielone
pojedynczą spacją oraz różne od siebie, które oznaczają: „A zna B” (z tego
nie wynika, że B zna A). Żadna para liczb A B się nie powtarza (chociaż
oczywiście może się zdarzyć para B A).
Wyjście
Na wyjściu mają być podane dwie liczby w jednej linii. Pierwsza oznacza
numer osoby, będącej super idolem (to znaczy takiej, której różnica między
tym, kto ją zna, a tymi, których ona zna jest największa). Druga liczba
stanowi tę różnicę. Jeżeli takich osób jest więcej powinna zostać wypisana
ta, która ma największy numer.
"""

people, relations = map(int, input().split())
a=[]
b=[]
results=[0]*people

for i in range(relations):
    x, y = input().split()
    a.append(int(x))
    b.append(int(y))

for i in range(relations):
    results[a[i]-1]-=1
    results[b[i]-1]+=1

max_value = max(results)
max_index = max(i for i, val in enumerate(results) if val == max_value)
print(max_index + 1, max_value)