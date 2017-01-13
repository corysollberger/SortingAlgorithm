#GUI for Sorting Algorithms | Created by: Cory Sollberger
#Imports
from tkinter import *
from Controller import Controller
import time

class GUI():
    def __init__(self):
        self.controller = Controller()
        self.frameList = []
        self.current = 0
        self.root = Tk()
        self.root.title("Sorting Algorithms")
        self.root.configure(bg="white")
        self.canvas_width = 1200
        self.canvas_height = 400
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.configure(background="black")
        self.canvas.pack()
        self.goButton = Button(self.root, text="GO", command=self.Animate)
        self.goButton.pack()
        self.root.after(0, self.initAnimate())
        self.root.mainloop()

    #Perform InsertionSort on list
    def callInsertionSort(self):
        self.controller.InsertionSort()

    def getFrameList():
        self.controller.getFrameList()
        
    #Begin Sorting Animation
    def initAnimate(self):
        self.callInsertionSort()
        self.frameList = self.controller.getFrameList()
        #print (self.frameList[0])
        #GUI.draw3(self)

    def Animate(self):
        #self.frameList = self.controller.getFrameList()
        if(self.current < len(self.frameList)):
            self.reDraw()
            self.root.after(1,self.Animate)
        
    #Draw the current frame of the graph
    def draw(self):
        #l = self.controller.getCurrentList()
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
        #l = self.controller.getFrameList()
        #print (len(l))
        for x in range(240):
            self.canvas.create_rectangle((5*x),self.canvas_height,(5*(x+1)),(self.canvas_height-(self.frameList[self.current][x])),fill="white")
        self.current += 1


    #ActionListener for Button Press for Button (GO)
    def reDraw(self):
        #print ("CLICK")
        #self.callInsertionSort()
        run = len(self.frameList)
        #print (run)
        print ("running")
        self.draw3()
        #self.root.after(10, self.draw3())
        #time.sleep(.5)
