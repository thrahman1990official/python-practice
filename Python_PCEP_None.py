# Functions in Python can typically do two things:
# 1) Cause some effect
# 2) Return a meaningful value
print('hello')
# or
len('hello')
# above only returns
length = len('hello')
number = input('what is the number?')
# Output:
# what is the number?5
print_return = print('Hello world')
print(print_return)
# Output
# None

# None is a null value
x = None
if x:
    print("None is True")
elif x is False:
    print("None is False")
else:
    print("None is not True, or False, None is just None")
# Output:
# None is not True, or False, None is just None
x = None
if x is None:
    print('yes')
if x == None:
    print('it does')
# Output:
# yes
# it does
def greet():
    print('hello!')

x = greet()
print(x)
# Output:
# hello!
# None
    
