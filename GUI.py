#GUI for Sorting Algorithms | Created by: Cory Sollberger
#Imports
from tkinter import *
from Controller import Controller
import time

class GUI():
    def __init__(self):
        self.controller = Controller()
        self.frameList = []
        self.root = Tk()
        self.root.title("Sorting Algorithms")
        self.root.configure(bg="white")
        self.canvas_width = 1200
        self.canvas_height = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.configure(background="black")
        self.canvas.pack()
        self.goButton = Button(self.root, text="GO", command=self.reDraw)
        self.goButton.pack()
        self.root.after(0, self.Animate())
        self.root.mainloop()

    #Perform InsertionSort on list
    def callInsertionSort(self):
        self.controller.InsertionSort()

    def getFrameList():
        self.controller.getFrameList()
        
    #Begin Sorting Animation
    def Animate(self):
        self.callInsertionSort()
        self.frameList = self.controller.getFrameList()
        GUI.draw(self)

    #Draw the current frame of the graph
    def draw(self):
        l = self.controller.getCurrentList()
        for x in range(240):
            self.canvas.create_rectangle((5*x),self.canvas_height,(5*(x+1)),(self.canvas_height-(l[x])),fill="white")

    #Draw the current frame of the graph
    def draw2(self):
        self.canvas.delete("all")
        l = self.controller.getCurrentList()
        for x in range(240):
            self.canvas.create_rectangle((5*x),self.canvas_height,(5*(x+1)),(self.canvas_height-(x*1.5)),fill="white")

    #Draw the current frame of the graph
    def draw3(self):
        self.canvas.delete("all")
        self.callInsertionSort()
        l = self.controller.getFrameList()
        a = 1
        #print (len(l))
        for x in range(240):
            self.canvas.create_rectangle((5*x),self.canvas_height,(5*(x+1)),(self.canvas_height-(l[a][x])),fill="white")
        a += 1

    #ActionListener for Button Press for Button (GO)
    def reDraw(self):
        print ("CLICK")
        self.root.after(0, self.draw3())
