def Count_sort(a):
    m=int(max(a))
    c=[]
    b=[]
    for i in range(0,m+1):
        k=a.count(i)
        c.append(k)
    for j in range(0,m+1):
        while(c[j]>0):
            b.append(j)
            c[j]=c[j]-1
    return b
c=Count_sort([1.2,0.4,1.6])
print(c)
            
            

        
