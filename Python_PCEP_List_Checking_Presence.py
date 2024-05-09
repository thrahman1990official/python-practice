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
# input:
# What is your name? Talhah
# You are not invited!
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')
