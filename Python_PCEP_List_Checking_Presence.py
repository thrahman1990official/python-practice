for char in 'happy message':
    print(char)
# Output:
# h
# a
# p
# p
# y
#
# m
# e
# s
# s
# a
# g
# e

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
# Input:
# What is your name? Talhah
# Output:
# You are not invited!
# Below is another way to have the desired output above
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')
