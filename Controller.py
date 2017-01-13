#Controller
#Imports
from Model import Model
class Controller(object):
    def __init__(self):
        self.model = Model()

    def InsertionSort(self):
        self.model.insertionSort()
        
    def getCurrentList(self):
        return self.model.getList()

    def getFrameList(self):
        return self.model.getFrameList()
