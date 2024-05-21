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

user_data = ('Talhahshah', 'Talhahstan', 1990) + ('Engineer', 'male')
print(user_data)
# Output:
# ('Talhahshah', 'Talhahstan', 1990, 'Engineer', 'male')

numbers = (0,1) * 10
print(numbers)
# Output:
# (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)

# Below is an example of list where all are names and all represent male names
male_name = ['Hamzah', 'Omar', 'Sohaib']
# Each element is a float that represents temperature in balloon on different day
# Again, all elements are floats and all of them represent temperatures
berlin_temp = [13.0, 17.5, 12.0]

# Difference between Tuples and Lists?
# Other than the fact that Tuples use () brackets and Lists use [] 
# Tuples are often used when you want to group together values of different types that are
# somehow related and together they form some sort of structure some sort of bigger data
# You have seen one such example already when we had user data variable
# Here you can see that we have three elements of different data types
