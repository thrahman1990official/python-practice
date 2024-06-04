# below is an example of an exception
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculate the inverse')
# run the above code 1st time
# input:
# Enter an integer:
# a
# output:
# You did not provide a number, so I will not calculate the inverse
# run the above code 2nd time
# Input:
# Enter an integer:
# 2
# output:
# The inverse of 2 is 0.5


  
