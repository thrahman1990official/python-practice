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
# run the above code 3rd time
# Input:
# Enter an integer:
# 0
# output:
# You did not provide a number, so I will not calculate the inverse

# a better version for the above code, I have stated below:
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')

  
