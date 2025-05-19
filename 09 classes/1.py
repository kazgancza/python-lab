"""
Zdefiniuj klasę Point, przechowującą współrzędne punktu na płaszczyźnie. W klasie zaimplementuj:

konstruktor przyjmujący jako parametry współrzędne punktu,
przeciążenie metody __str__, tak żeby punkt został wypisany w postaci "(x, y)", np. "(3, 4)",
przeciążenie metody __add__, aby suma dwóch punktów zwracała nowy punkt o sumie współrzędnych tych punktów,
metodę statyczną (bez self) distance obliczającą odległość pomiędzy dwoma podanymi punktami.
Zaprezentuj działanie klasy i zaimplementowanych metod w kodzie globalnym w sekcji if __name__=="__main__"
"""

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"({self.x},{self.y})")

    def __add__(self, point2):
        self.x += point2.x
        self.y += point2.y

    def distance(point1, point2):
        a = abs(point1.x - point2.x)
        b = abs(point1.y - point2.y)

        distance = sqrt(pow(a, 2) + pow(b, 2))

        return distance



if __name__ == "__main__":

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(5, 4)
    print(Point.distance(p1, p2))

    p3.__add__(p2)
    p3.__str__()