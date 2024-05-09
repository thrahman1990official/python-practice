first = input('Enter 1st number: ')
second = input('Enter 2nd number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)
# Input:
# Enter 1st number: 
# 13
# Enter 2nd number:
# 99
# Output:
# Before swapping: 13 99
# After swapping: 99 13
# Another way to have same input and output above
first = input('Enter 1st number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)
# Output:
# ['Phoenix', 'Los Angeles', 'Chicago', 'Houston', 'New York City']

top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)
# Output:
# ['Chicago', 'Houston', 'Los Angeles', 'New York City', 'Phoenix']
