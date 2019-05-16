n=int(input("enter the no: "))
n1=int(input("enter the no: "))
for n2 in range(n,n1):
    for i in range(2,(n2//2)):
        if n2%i==0:
            break   
    else:
        print(n2)    
