from random import randint
from tkinter import *
import time

class Sort(object):

    DEFAULT_NUMS = 100
    DEFAULT_MIN = 1
    DEFAULT_MAX = 100
    Width = 600
    Height = 600
    Padding = 50
    list=[]

    def __init__(self):
        self.root = Tk()

        self.nums_button = Scale(self.root, from_=2, to=100, orient=HORIZONTAL)
        self.nums_button.set(self.DEFAULT_NUMS)
        self.nums_button.grid(row=0, column=0)

        self.min_button = Scale(self.root, from_=1, to=99, orient=HORIZONTAL)
        self.min_button.set(self.DEFAULT_MIN)
        self.min_button.grid(row=0, column=1)

        self.max_button = Scale(self.root, from_=2, to=100, orient=HORIZONTAL)
        self.max_button.set(self.DEFAULT_MAX)
        self.max_button.grid(row=0, column=2)

        self.start_button = Button(self.root, text='start', command=lambda: self.start(self.list))
        self.start_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=self.Width, height=self.Height)
        self.c.grid(row=1, columnspan=4)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.nums = self.nums_button.get()
        self.min = self.min_button.get()
        self.max = self.max_button.get()
        for i in range(self.nums):
            value = randint(self.min, self.max)
            self.list.append(value)

        self.x_span = (self.Width - (self.Padding * 2)) / self.nums
        self.y_tick = (self.Height - (self.Padding * 2)) / self.max
        self.draw(self.list)

    def start(self, list):
        x = self.nums_button.get() - 2
        print(x)
        while x > 0:
            for i in range(x + 1):
                if list[i] > list[i+1]:
                    small = list[i+1]
                    large = list[i]
                    list[i], list[i+1] = small, large
            x = x - 1
        self.draw(list)
        

    def draw(self, list):
        self.c.delete('all')
        for x in range(self.nums_button.get()):
            self.c.create_line(self.Padding + self.x_span * x, self.Padding, self.Padding + self.x_span * x, self.Padding + list[x] * self.y_tick)


if __name__ == '__main__':
    Sort()