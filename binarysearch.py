arr=[int(x) for x in input().split()]
i=int(input())
left=0
right=len(arr)-1
def BinarySearch(array,i,left,right):
    while left<=right:
        middle=(left+right)//2
        #check if middle index is i
        if array[middle]==i:
            return(middle)
        #if middle index value is greater ignore right half
        elif array[middle]>i:
            right=middle-1
        #if middle index value is less ignore left half
        else:
            left=middle+1
    return -1
    
if BinarySearch(arr,i,left,right)==-1:
    print("Element not found")
else:
    print("Element Found at index {0}".format(BinarySearch(arr,i,left,right)))

