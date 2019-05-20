n = int(input("Enter number of elements : "))  
hour=n//60
minutes=abs(hour*60-n)
print(f'{hour} {minutes}')
