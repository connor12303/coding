total = 0
keep_looping = 'yes'
while keep_looping == 'yes':
    number = input('enter a number: ')
    total = total + float(number)
    keep_looping = input('add another number (yes/no)')
print(f'total value of numbers entered is {total}')