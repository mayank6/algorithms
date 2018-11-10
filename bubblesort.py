x=[5,3,2,7,9,10,78,45]

for i in range(len(x)-1):
    flag=0
    for j in range(len(x)-1):
        if (x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
            flag=1
    if (flag==0):
        break
print(x)
            
