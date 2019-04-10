def merge_sort(unsorted_list):

    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    leftRecursive = merge_sort(left)
    rightRecursive = merge_sort(right)

    return merge(leftRecursive, rightRecursive)
 #merge_sort의 return값으로는 원소 1개 아니면 정렬된 배열

def merge(left, right):
    leftPtr = 0
    rightPtr = 0
    sorted_list = [] 

    while(leftPtr < len(left) and rightPtr < len(right)):
        if left[leftPtr] < right[rightPtr]:
             sorted_list.append(left[leftPtr])
             leftPtr += 1
        else:
            sorted_list.append(right[rightPtr]) 
            rightPtr += 1
    while(leftPtr < len(left)):
        sorted_list.append(left[leftPtr])
        leftPtr += 1
    while(rightPtr < len(right)):
        sorted_list.append(right[rightPtr])
        rightPtr +=1 
    return sorted_list

inputList =[1.5, 1, 2, 5, 2.5, 2.25, 0.5, 12.5, 7.5]
print(merge_sort(inputList))