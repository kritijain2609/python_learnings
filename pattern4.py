n=5
for i in range (n):
    p=1    
    for j in range(n-i):
       print(' ',end=' ')   
    for j in range(i+1-1):
        print(p,end=' ')
        p=p+1   
    for j in range(i+1):
        print(p,end=' ')
        p=p-1    
    print('')        
        

                                     
  
