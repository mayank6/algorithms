x=[5,3,2,7,9,10,78,45]
for i in range(len(x)):
    m=i
    #finding min element from i to len(list)
    for j in range(i,len(x)):
        if (x[j]<x[m]):
            m=j
    #swapping elements of index        
    x[i],x[m]=x[m],x[i]

print(x)
