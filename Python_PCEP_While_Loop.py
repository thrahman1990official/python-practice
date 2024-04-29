counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Finished!

# But when you do counter less than 11
counter = 1
while counter > 11:
    print(counter)
    counter += 1
print('Finished!')
# Output:
# Finished!

secret_number = 14
user_input = int(input('Try to guess secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number.')
# Output:
# Try to guess secret number from 0 to 20: 
# 15
# Wrong!
# Try to guess secret number from 0 to 20: 
# 14
# Perfect! You have guessed the secret number.
