import math
arr=[int(x) for x in input().split()]
x=int(input("Element to find"))
n=len(arr)

def JumpSearch(arr,x,n):
    step=math.sqrt(len(arr))
    
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += math.sqrt(n) 
        if prev >= n: 
            return -1
      
    while arr[int(prev)] < x: 
        prev += 1
          
        # If we reached next block or end  
        # of array, element is not present. 
        if prev == min(step, n): 
            return -1
      
    # If element is found 
    if arr[int(prev)] == x: 
        return prev 
      
    return -1   
