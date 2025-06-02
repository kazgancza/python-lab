import turtle
from math import sqrt
import random

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a}, {self.b})"

    def distance(self, other):
        pit_a = abs(self.a - other.a)
        pit_b = abs(self.b - other.b)

        c = sqrt(pow(pit_a, 2) + pow(pit_b, 2))

        return c

points = []

for _ in range(10):
    p = Point(random.randint(-100, 100), random.randint(-100, 100))
    points.append(p)

shortest_distance = float('inf')
shortest_point = [None, None]

for i, p1 in enumerate(points):
    for j, p2 in enumerate(points):
        if i == j:
            continue
        d = p1.distance(p2)
        if d < shortest_distance:
            shortest_distance = d
            shortest_point[0] = p1
            shortest_point[1] = p2

print(shortest_distance)
print(shortest_point[0])
print(shortest_point[1])
