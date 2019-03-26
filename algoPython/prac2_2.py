
'''
def swap (a, b) :
    temp = a
    a = b
    b = temp
    '''
    
def iterativeBubbleSort(Array) :
    sorted = False
    count = 0
    while not sorted :
        sorted = True
        for i in range (1, len(Array)) :
            if (Array[i-1] > Array[i]) :
                Array[i-1], Array[i] = Array[i], Array[i-1]
                #swap(Array[i-1], Array[i])
                sorted = False
        print("iterative    "+str(count)+str(Array))
        count +=1
def recursiveBubbleSort(ArrayRe, index) :
    global sortedRe
    if index == len(ArrayRe) :
        return
    if (ArrayRe[index-1] > ArrayRe[index]) :
        sortedRe = False
        ArrayRe[index -1], ArrayRe[index] = ArrayRe[index], ArrayRe[index -1]
    recursiveBubbleSort(ArrayRe, index+1)

Array = [30, 20, 40, 10, 5, 10, 30, 15]
ArrayRe = [30, 20, 40, 10, 5, 10, 30, 15]
print("Array(Before)"+str(ArrayRe))
sortedRe = False
countRe = 0
while not sortedRe :
    #for i in range(1, len(Array)) :
    sortedRe = True
    recursiveBubbleSort(ArrayRe, 1)
    print("recursive    "+ str(countRe) + str(ArrayRe))
    countRe +=1

iterativeBubbleSort(Array)
print(Array)
print(ArrayRe)
