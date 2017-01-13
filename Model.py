#Model for Sorting Algorithms | Created by Cory Sollberger
#Import
from Sort import Sort
from InsertionSort import InsertionSort
class Model(object):
    def __init__(self):
        self.list = Sort.genRandList()
        #self.list = [3,2,1]
        self.frameList = []

    def insertionSort(self):
        self.frameList = InsertionSort.IS(self.list)

    def getList(self):
        return self.list

    def getFrameList(self):
        return self.frameList

'''
m = Model()
print (m.list)
m.insertionSort()
fl = m.getFrameList()
print (fl[1])
'''
