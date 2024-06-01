# factorial
# 3! = 1 * 2 * 3 = 6
# 5! = 1 * 2 * 3 * 4 * 5 = 120
def get_factorial_iterative(number):
    factorial = 1                     #initially factorial starts with one
    for x in range(1, number + 1):    #for range starting from one and incrementing based on the number limit
        factorial *= x                #factorial equals previous factorial or number multiplied to next number
    return factorial                  #returning the value
print(get_factorial_iterative(6))
# Output:
# 720
# Because 1*2*3*4*5*6
# Above is an example of iterative 
# Now will do an example of recursive
def get_factorial_iterative(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial
print(get_factorial_iterative(6))
# Output:
# 720

