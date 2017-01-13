#Insertion Sort | by Cory Sollberger
from Sort import Sort

class InsertionSort():
    def __init__(self):
        pass
    #Insertion Sort Implementation
    def IS(l):
        frameList = []
        frameList.append(l[:])
        x = 1
        #While there exists unordered list elements
        while(x < len(l)):
            tempx = x
            a = x-1
            #Move elements left-to-right to find sorted place for current index
            while(l[tempx] < l[a] and a >= 0):
                Sort.switchIndices(tempx,a,l)
                tempx = a
                a -= 1
                frameList.append(l[:])
            x+=1 #next index
        return frameList

#test    
'''l = [9,8,7,6,5,4,3,2,1]
l2 = [9,8]
print (l)
val = InsertionSort.IS(l)
print (l)
print (val)
'''
