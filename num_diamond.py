n=5
p=1
for i in range (n-1):
    for j in range(n-i):
        print(' ',end=' ')
        
    for j in range (i+1):
        print (p,end=' ')
     
    for j in range (i):
        print (p,end=' ')    
    p=p+1    
    print('')        
        
for i in range (n):
    for j in range(i+1):
        print(' ',end=' ')
        
    for j in range (n-i):
        print (p,end=' ')
        
    for j in range (n-i-1):
        print (p,end=' ')    
    p=p+1      
    print('')        
                                     
  
