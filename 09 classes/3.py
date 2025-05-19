"""
Mały Jaś ma kilka koleżanek, każdego dnia spędza miło czas u jednej z nich. Mama Jasia, aby
zawsze wiedzieć gdzie jest, wyposażyła go w odbiornik GPS.
Koleżanki Jasia mieszkają na działkach o współrzędnych całkowitych (od do ). Mając do
dyspozycji dane o położeniu działek, napisz, u której koleżanki przebywa Jaś.
Uwaga: Brzegi działki należą do działki, wszystkie działki są rozłączne. Koleżanki numerujemy
kolejnymi liczbami całkowitymi od .
Wejście
W pierwszym wierszu wejścia znajduje się liczba całkowita (od do ), oznaczająca liczbę
koleżanek Jasia. W następnych wierszach są podane współrzędne lewego dolnego rogu oraz
prawego górnego oddzielone spacją. W ostatnim wierszu jest podana pozycja Jasia.
Wyjście
Wypisz numer koleżanki, u której przebywa Jaś.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.bl = Point(x1, y1)
        self.tr = Point(x2, y2)
    
    def point_in_rectange(self, point):
        in_x = self.bl.x <= point.x and self.tr.x >= point.x
        in_y = self.bl.y <= point.y and self.tr.y >= point.y

        return in_x and in_y
    
def find_point(lots, point):
    for i, lot in enumerate(lots):
        if lot.point_in_rectange(point):
            return i


# input
n = int(input().strip())

lots = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lots.append(Rectangle(x1, y1, x2, y2))

x, y = map(int, input().split())
john_pos = Point(x, y)

# output
print(find_point(lots, john_pos) + 1)




