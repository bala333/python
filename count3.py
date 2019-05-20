le=1
n=input('Enter the sentence: ')
x=len(n)
for i in range(0,x):
    if n[i]==".":
        le =le+1
print(le)
