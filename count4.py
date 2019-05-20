le=0
n=input('Enter the sentence: ')
x=len(n)
for i in range(0,x):
    if n[i].isdigit():
        le =le+1
print(le)
