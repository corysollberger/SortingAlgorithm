from Sort import Sort

items = [3,2,1]
iteml = [2,1]
test = [3,7,8,5,2,1,9,5,4]

class QuickSort():
    def __init__(self):
        moves = []
    def QS(l):
        pivot = len(l)-1
        lo = 0
        if(lo == pivot or pivot < 0):
            return l
        else:
            lo = QuickSort.findGreaterValue(lo,pivot,l)
            while(pivot != lo):
                Sort.switchIndices(pivot-1,lo,l)
                lo = QuickSort.findGreaterValue(lo,pivot,l)
                Sort.switchIndices(pivot,pivot-1,l)
                pivot-=1
            temp = []
            temp.append(l[pivot])
            pList = QuickSort.partitionList(l,pivot)
            return (QuickSort.QS(pList[0]) + temp + QuickSort.QS(pList[1]))
        
    def printCurrentList(l):
        print ("Current List: " + str(l))
    
    def partitionList(l, pivot):
        l1 = l[:pivot]
        l2 = l[pivot+1:]
        l3 = []
        l3.append(l1)
        l3.append(l2)
        return l3

    def findGreaterValue(a,b,l):
        while (l[a] <= l[b] and a!=b):
            a+=1
        return a

'''
def printCurrentList(l):
    print ("Current List: " + str(l))

def partitionList(l, pivot):
    l1 = l[:pivot]
    l2 = l[pivot+1:]
    l3 = []
    l3.append(l1)
    l3.append(l2)
    return l3

def findGreaterValue(a,b,l):
    while (l[a] <= l[b] and a!=b):
        a+=1
    return a

def QS(l):
    pivot = len(l)-1
    lo = 0
    if(lo == pivot or pivot < 0):
        return l
    else:
        lo = findGreaterValue(lo,pivot,l)
        while(pivot != lo):
            Sort.switchIndices(pivot-1,lo,l)
            lo = findGreaterValue(lo,pivot,l)
            Sort.switchIndices(pivot,pivot-1,l)
            pivot-=1
        temp = []
        temp.append(l[pivot])
        pList = partitionList(l,pivot)
        return (QS(pList[0]) + temp + QS(pList[1]))
'''                


'''
#Test lists to be quicksorted
t = [3,7,8,5,2,1,9,5,4]
test = [5,3,1,4,2,1,90,56,4,14,99,304,289,105]
t1=[3,1,2,1]
t2=[9,8]

#Evaluate the given list using QuickSort
val = QuickSort.QS(test)
print (str(val))
'''




