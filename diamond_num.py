n=5
for i in range (n-1):
    for j in range(n-i):
        print(' ',end=' ')
    p=1
    for j in range(i+1):
        print(p,end=' ')
        p=p+1    
        
    for j in range(i+1-1):
        print(p,end=' ')
        p=p+1 
    print('')        

for i in range (n):
    for j in range(i+1):
        print(' ',end=' ')
    p=1
    for j in range(n-i):
        print(p,end=' ')
        p=p+1    
        
    for j in range(n-i-1):
        print(p,end=' ')
        p=p+1 
        
    print('')     

                                     
  
