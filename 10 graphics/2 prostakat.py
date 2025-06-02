import tkinter

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


window = tkinter.Tk()
screen = tkinter.Canvas(window, width=400, height=300)
screen.pack()

screen.create_line(10, 10, 390, 290)
screen.create_line(10, 10, 200, 200, fill="green")
screen.create_text(50, 50, text="Test")

screen.mainloop()