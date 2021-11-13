def selection_sort(a):
    n=len(a)
    i=0
    while(i<n):
        j=i
        while(j<n):
            if(a[i]>a[j]):
                c=a[i]
                a[i]=a[j]
                a[j]=c
            j=j+1
        i=i+1
    return a
print(selection_sort([8,0,7,1,3]))
