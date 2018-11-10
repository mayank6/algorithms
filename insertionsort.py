x=[5,3,2,7,9,10,78,45]
s=0
for i in range(1,len(x)):
    k=x[i] 
    j=i-1
    while j>=0 and k<x[j]:
        x[j+1]=x[j]
        j=j-1
    x[j+1]=k
print(x)
        
