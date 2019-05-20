lst = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 
max=lst[0]
for j in lst:
    if j>max:
        max=j    
    
print(f"Max is:{max}" )
