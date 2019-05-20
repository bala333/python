c=0
a,b=0,1
n=int(input('Enter the number: '))
for i in range(n):
    print(a, end=' ')
    a,b=b,b+a
    c=c+1
