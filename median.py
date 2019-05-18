lst = []
lst1=[]
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)   
    lst1=sorted(lst) 
n1=round(n/2)   
num=(lst1[n1])
print(f'Madian number is: {num}')
