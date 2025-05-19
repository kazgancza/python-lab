"""
Napisz program, który mając dane współrzędne dwóch prostokątów, których boki są równoległe
do osi współrzędnych, policzy pole części wspólnej tych prostokątów.
Wejście
W pierwszym wierszu wejścia znajdują się 4 liczby całkowite: , oznaczające
odpowiednio współrzędną - ową i - ową lewego górnego rogu i współrzędną - ową i - ową
prawego dolnego rogu pierwszego prostokąta.
W drugim wierszu wejścia znajdują się 4 liczby całkowite: , oznaczające odpowiednio
współrzędną - ową i - ową lewego górnego rogu i współrzędną - ową i - ową prawego
dolnego rogu drugiego prostokąta.
Wszystkie współrzędne są nie mniejsze niż i nie większe niż .
Wyjście
Pierwszym i jedyny wiersz wyjścia powinien zawierać jedną liczę całkowitą równą wartości pola
części wspólnej dwóch prostokątów
"""

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        # top-left: (x1, y1), bottom-right: (x2, y2)
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)

    def cross_section(self, other):
        x_left = max(self.x1, other.x1)
        y_top = max(self.y1, other.y1)
        x_right = min(self.x2, other.x2)
        y_bottom = min(self.y2, other.y2)
        
        dx = x_right - x_left
        dy = y_bottom - y_top

        if dx <= 0 or dy <= 0:
            return 0
        return dx * dy


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

r1 = Rectangle(x1, y1, x2, y2)
r2 = Rectangle(x3, y3, x4, y4)

print(r1.cross_section(r2))