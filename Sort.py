from random import randint

class Sort():
    def __init__(self):
        pass
    
    #Switches the given indices within a list
    #Pre: none
    #Post: Values at index 1 and index2 are switched within l
    def switchIndices(index1, index2, l):
        l[index1], l[index2] = l[index2], l[index1]
        return l

    def printList(l):
        print ("L = " + str(l))

    def genRandList():
        l = []
        for x in range(240):
            l.append(x*1.5)
        Sort.randomizeList(l)
        return l
    def randomizeList(l):
        for x in range(0,len(l)):
            index1 = randint(0,len(l)-1)
            index2 = randint(0,len(l)-1)
            while (index2 == index1):
                index2 = randint(0,len(l)-1)
            Sort.switchIndices(index1, index2, l)
            #print (str(index1))
            #print (str(index2))
        
#li = [1,2,3]
#print (li)
#switchIndices(0,1,li)
#print(li)
    
