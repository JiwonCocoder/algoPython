def MakeHeap(input, Root, LastNode):
    Parent = Root
    RootValue = input[Root]
    leftSon = 2*Parent + 1
    rightSon = leftSon + 1
    while(leftSon <= LastNode):
        if(rightSon <= LastNode and input[leftSon] < input[rightSon]) :
            son = rightSon
        else:
            son = leftSon
        if RootValue < input[son]:
            input[Parent] = input[son]
            Parent = son
            leftSon = 2*Parent + 1
            rightSon = leftSon + 1
        else:
            break
    input[Parent] = RootValue
    return input
def HeapSort(input, n):
    for i in range(n//2 -1,-1,-1):
        print("here")
        input = MakeHeap(input, i, n-1)
    print("MakeHeap:"+str(input))
    for i in range(n-1, 0, -1):
        input[0], input[i] = input[i], input[0]
        input = MakeHeap(input[:i], 0, i-1)
        print(input)
input = [4, 4, 3, 2, 16, 9, 10, 14, 9, 10, 7]
HeapSort(input, len(input))
