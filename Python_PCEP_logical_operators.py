# available logical operators
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals

password = input('Do you know secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')

if True:
    print('Condition met')

if False:
    print('Condition met')

user_age = int(input('What's your age? '))

if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
    
