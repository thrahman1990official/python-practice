user_data = ('Talhahshah', 'Talhahstan', 1990)
print(len(user_data))
# Should print out the number of contents inside the tuple
# Output:
# 3

user_data = ('Talhahshah', 'Talhahstan', 1990)
if 'Talhahstan' in user_data:
    print('This person comes from Talhahstan.')
# Output:
# This person comes from Talhahstan.

user_data = ('Talhahshah', 'Talhahstan', 1990)
for element in user_data:
    print(element)
# Output:
# Talhahshah
# Talhahstan
# 1990
