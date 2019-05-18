lst = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 
min=lst[0]
for i in lst:
    if i<min:
        max=i    
    
print(f"Min is:{min}" )
