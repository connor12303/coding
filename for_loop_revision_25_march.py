a=input(' enter an integer')
a=int(a)
b=input('enter an integer')
b=int(b)
c=input('enter an integer')
c=int(c)
a_squared = a * a
a_squared=int (a_squared)
b_squared = b * b
b_squared=int (b_squared)
c_squared = c * c
c_squared=int (c_squared)
if a_squared + b_squared == c_squared :
    print('your numbers do equal a pythagorean triple')
else :
    print('your numbers do not equal a pythagorean triple')