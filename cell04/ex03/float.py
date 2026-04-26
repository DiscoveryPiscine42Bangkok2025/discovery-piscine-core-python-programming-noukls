A = float(input('Give me a number '))
print(A.is_integer())
if A.is_integer() == True :
    print('This number is an integer')
elif A.is_integer() == False :
    print('This number is a decimal')