#create a variable for first number
numX = float(input("First-Number: "))
#create a variable for second number
numY = float(input("Second-Number: "))
#create a variable that finds the substracts the first number from 2nd number
subXandY = numX - numY
#display the output as a string 
print("Result: " + str(subXandY))
if subXandY < 0:
    print("Above is a Negative Number")
else:
    print("Above is a Positive Number")
