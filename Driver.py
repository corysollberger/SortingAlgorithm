#Imports
from tkinter import *
from Sort import Sort
from GUI import GUI
from QuickSort import QuickSort


#The driver for the sorting application


#Methods

def generateList():
    l = Sort.genList()
def Quicksort(l):
    Sort.printList(l)
    val = QuickSort.QS(l)
    Sort.printList(val)











l = []
l = Sort.genRandList()
#l = Sort.randomizeList(l)
#generateList()
print (l)
#GUI
gui = GUI()

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
#Testing
print ("Sorting Algorithm Driver started...")

t = [1,2,3,4,5,6,7,8,9]
#Sort.switchIndices(0,1,t)
Sort.printList(t)
Sort.randomizeList(t)
Sort.printList(t)
print ("Initiating QuickSort")
test = [5,3,1,4,2,1,90,56,4,14,99,304,289,105]
Quicksort(test)
