A = float(input('Enter the first number '))        
B = float(input('Enter the last number '))
print(A*B)
if A*B < 0 :
    print('The result is negative')
elif A*B > 0 :
    print('The result is positve')
else :
    print('The result is zero')