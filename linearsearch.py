arr=[int(x) for x in input().split()]        #input list in one line split default(SPACE)
i=int(input())
def LS(arr,i):    
    for x in range(len(arr)):
        if arr[x]==i:
            return(x)                         #return index of found element if exists
    return(-1)                                #return -1 if not exists
if LS(arr,i)==-1:
    print("Element not found")
else:
    print("Element Found at index {0}".format(LS(arr,i)))
    
    
