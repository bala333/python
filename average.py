sum=0
n=int(input())
m=list(map(int,input().split(" ")))
for i in m:
     sum =sum+int(i)
print(sum//n)   
