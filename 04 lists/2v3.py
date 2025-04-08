"""
Odciski palca
Dostępna pamięć: 32MB
Pan Integer pracuje nad programem do odczytywania odcisków palców. Najwięcej uwagi
poświęca modułowi odpowiedzialnemu za sprawdzanie, czy pewien kwadratowy
czteroelementowy fragment odnalezionego obrazu (zdjęty z przedmiotu odcisk) może być
jakąś częścią dużego obrazu (pełnego wzoru). Zastanawia się przy tym, ile razy fragment
pojawił się w jakiejkolwiek formie na dużym obrazie. Pomóż mu to obliczyć!
Wejście
W pierwszej i drugiej linii wejścia znajdują się po dwie dwucyfrowe liczby pierwsze –
odnaleziony fragment obrazu. W drugiej linii wejścia znajdują się dwie liczby całkowite h oraz
w (1 ≤ h, w ≤ 1000), odpowiednio wysokość i szerokość dużego obrazu.
W kolejnych h liniach znajduje się po w rozdzielonych spacją dwucyfrowych liczb pierwszych.
Wyjście
Liczba wystąpień dowolnej permutacji fragmentu obrazu we wzorze. 
"""

a, b = map(int, input().split())
c, d = map(int, input().split())
h, w = map(int,input().split())
screen = [list(map(int, input().split())) for _ in range(h)]

searched = a*b*c*d
result=0

for i in range(h-1):
    for j in range(w-1):
        if searched%screen[i][j]!=0:
            continue
        if searched%screen[i+1][j]!=0:
            continue
        if searched%screen[i][j+1]!=0:
            continue
        if searched%screen[i+1][j+1]!=0:
            continue
        result+=1
                
print(result)