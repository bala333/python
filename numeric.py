def is_number(s):
    try:
        float(s)
        return 'Yes'
    except ValueError:
        return 'No'
print(is_number(input('Enter the number: ')))        
