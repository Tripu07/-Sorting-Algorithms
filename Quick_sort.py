def Quick_sort(a,low,high):
    if(low<high):
        pi=partition(a,low,high) #partition_index
        Quick_sort(a,low,pi-1)
        Quick_sort(a,pi+1,high)
        
    
    
    
    
    
def partition(a,low,high):
    i=low+1
    j=high
    while(i<j):
        while i<n and a[i]<a[low]:
            i=i+1
        while(a[j]>a[low]):
            j=j-1
        if(i<j):
            k=a[i]
            a[i]=a[j]
            a[j]=k
    k=a[low]
    a[low]=a[j]
    a[j]=k
    return j
a=[35,50,20,25,80,20,45]
n=len(a)
Quick_sort(a,0,n-1)
print(a)
    


        
    

        
        
    
        
        
            
            
