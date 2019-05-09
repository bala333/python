v=['a','e','i','o','u']
n=input('Enter your number: ').lower()

if n in v:
    print('Vowels')
elif  n>='a' and n<='z':
     print('Consonant')
else:
    print('Inavalid')      
