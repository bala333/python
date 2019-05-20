n = int(input("Enter number of elements : "))  
hour=n//60
min=abs(hour*60-n)
print(f'{hour} {min}')
