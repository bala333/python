n=(input())
c,c1=1,1
for i in n:
    if i.isdigit(): 
        c=0
    elif i.isalpha():    
        c1=0
if c==0 and c1==0:
    print('Yes')        
else:
    print('no')    
