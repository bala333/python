n=int(input())
string=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
le=len(string)
for i in range(le):
    if n==i:
        print(string[i],end=" ")
