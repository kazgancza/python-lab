import turtle
import random

def a(t, n, r):
    t.speed(0)
    n2 = n*r
    current_r = n2
    y_move = 0
    while current_r > 0:
        t.color(random.choice(["red", "blue", "green"]))
        
        t.penup()
        t.goto(0, y_move)
        t.pendown()
        t.circle(current_r)
        current_r -= r
        y_move += r

def b(t, n, r):
    t.speed(0)
    for i in range(n):
        t.penup()
        t.goto(0, 2*i*r)
        t.pendown()
        t.circle(r)

def c(t, n, r):
    a, b = 0, 0
    for i in range(n):
        
        for _ in range(4):
            t.forward(r)
            t.left(90)
        t.penup()
        t.forward(r)
        t.left(90)
        t.forward(r/2)
        t.right(90)
        t.pendown()
        


n = 5
r = 20
t = turtle.Turtle()


# a(t, n, r)
# b(t, n, r)
c(t, n, r)

turtle.mainloop()


"""
Dane są dwie liczby naturalne n, r. Narysuj na ekranie, przy wykorzystaniu modułu turtle:

a) n współśrodkowych okręgów o środku w środku ekranu, o długości promienia malejącym o wartość r i w losowym kolorze.
b) n zewnętrznie stycznych okręgów o promieniu r, o współliniowych środkach.
c) n kwadratów: pierwszy o bokach długości r równoległych do osi, wierzchołki każdego następnego kwadratu leżą na środku boków kwadratu poprzedniego.
"""