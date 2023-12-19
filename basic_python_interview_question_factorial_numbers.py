# Write python program to find factorial of number
# Factorial of number is multiplication
# Of each and every number till given number except zero
# Factorial of 3 = 1 * 2 * 3
# 4 = 1 * 2 * 3 * 4 = 24
# 5 = 1 * 2 * 3 * 4 * 5 = 120

number = 5
factorial = 1
if number < 0:
  print("Cannot use negative numbers or numbers less than zero to find factorial")
elif number == 0:
  print("Factorial of zero is 1")
else:
  for i in range(1, num+1):
      factorial = factorial * i
  print("Factorial of is", factorial)
