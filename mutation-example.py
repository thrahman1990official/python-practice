# Mutations
# Read given string, change character at given index & print modified strong
# Note: Try changing list, tuple, & string. Understand difference between mutable & immutable datatpes

# Input format: First-line contains the string. Next line contains an integer & character indicating the position at which character should be inserted
# & character indicating position at which character should be inserted in string

# Output: Modified string

# Example:
# Input:
# Hello World
# 6 Z
# Output:
# Hello Zorld

s = input()
line = input()

indx= int(line.split()[0])
char = line.split()[1]
# Input 'Hello World'
# Input '6 Z'
indx = line.split()[0]
char = line.split()[1]
indx
# should give an output of '6'
char
# should give an output of 'Z'
out = s[:indx] + char + s[indx+1:]
out
# should give an Output 'Hello Zorld' 


