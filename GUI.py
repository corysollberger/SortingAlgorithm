#GUI for Sorting Algorithms | Created by: Cory Sollberger
#Imports
from tkinter import *
from Controller import Controller
import time

class GUI():
    def __init__(self):
        self.controller = Controller()
        self.root = Tk()
        self.root.title("Sorting Algorithms")
        self.root.configure(bg="white")
        self.canvas_width = 1200
        self.canvas_height = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.configure(background="black")
        self.canvas.pack()
        self.goButton = Button(self.root, text="GO")
        self.goButton.pack()
        self.root.after(0, self.Animate)
        self.root.mainloop()

    def Animate(self):
        for x in range(240):
            self.canvas.create_rectangle((5*x),self.canvas_height,(5*(x+1)),(self.canvas_height-(x*1.5)),fill="white")

'''
root = Tk()
root.title("SortingAlgorithms")
#root["title"] = "SortingAlgorithms"
root.configure(bg="white")
canvas_width = 1200
canvas_height = 400
w = Canvas(root, width=canvas_width, height=canvas_height)
w.configure(background="black")
w.pack()
b = Button(root, text="GO")
b.pack()
for x in range(240):
    #print(l[x])
    w.create_rectangle((5*x),canvas_height,(5*(x+1)),(canvas_height-(l[x])),fill="white")
#w.create_rectangle(5,400,10,300,fill="white")

root.mainloop()
'''
