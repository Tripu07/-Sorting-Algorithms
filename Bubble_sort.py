#bubble sort algorithm
def bubble_sort(a):   #time Complexiety:O(n^2)
    n=len(a)
    for i in range(0,n):
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    return a
print(bubble_sort([18,2,5,98,2,43,1,334]))


                
                 
    
                
            
            
        
        
        

                
        
