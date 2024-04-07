first_bit = 1
second_bit = 0
#In Boolean algebra below is first_bit LOGICAL AND second_bit
print(first_bit & second_bit)

first_bit = 0
second_bit = 0
#In Boolean algebra below is first_bit LOGICAL OR 0
print(first_bit | second_bit)

first_bit = 0
second_bit = 0
#In Boolean algebra below is 1 LOGICAL XOR 0 which results in 0
print(first_bit ^ second_bit)

number = 0
print(~number)
#In Boolean algebra below is LEFT-SHIFT OPERATOR of number
#in case of 0 it should output -1

number = 12
number << 1
#should output 24
#12 * (2^1) = 24

number = 12
number << 2
#should output 48
#12 * (2^2)

number = 12
number << 3
#should output 96
#12 * (2^3)


