# below is an example of an exception
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculate the inverse')
# input:
# Enter an integer:
# a
# output:
# You did not provide a number, so I will not calculate the inverse
  
