lst = []
lst1=[]
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)    
    
print(f"Sorted array is:{sorted(lst)}" )
