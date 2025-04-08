"""
Zadanie: PRZ
Przedziały – zadanie prostsze
Dostępna pamieć: 64 MB.
Dane jest n przedziałów domkniętych [ai, bi]. Jaka jest minimalna wartość bezwzględna różnicy dwóch liczb należących do
dwóch różnych przedziałów? Formalnie, chcemy obliczyć
min{|x − y| : x ∈ [ai, bi], y ∈ [a j, b j], 1 ≤ i < j ≤ n}.
Wejście
W pierwszym wierszu standardowego wejścia znajduje się liczba całkowita n (2 ≤ n ≤ 500 000) – liczba przedziałów. Każdy
z kolejnych n wierszy zawiera dwie liczby całkowite ai oraz bi (0 ≤ ai ≤ bi ≤ 109), oddzielone pojedynczym odstępem i repre-
zentujące końce i-tego przedziału domkniętego [ai, bi]. Można założyć,  ̇ze wszystkie pary (ai, bi) są różne.
Wyjście
Twój program powinien wypisać na standardowe wyjście jeden wiersz zawierający liczbę całkowitą zdefiniowaną w treści zada-
nia.
"""

n = int(input())
disp = [list(map(int, input().split())) for _ in range(n)]

disp.sort()

min_diff = float('inf')

for i in range(1, n):
    diff = max(0, disp[i][0] - disp[i - 1][1])

    if diff < min_diff:
        min_diff = diff

print(min_diff)