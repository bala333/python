n=int(input())
c=0
for i in range(1,1000):
    n1=pow(2,i)
    if n1==n:
        print('yes')
        c=1
        break
if c==0:
    print('no')
