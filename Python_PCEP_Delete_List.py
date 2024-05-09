top_cities = ['New York City', 'Los Angeles', 'Detroit', 'Chicago', 'Oakland', 'Miami']
# Below command should delete Detroit from the list since it is in index location 2
del top_cities[2]
print(top_cities)
# Output:
# ['New York City', 'Los Angeles', 'Chicago', 'Oakland', 'Miami']
# Below command should delete all cities starting from index location 3
del top_cities[3:]
print(top_cities)
# Output:
# ['New York City', 'Los Angeles', 'Detroit']
# Below command should delete all cities in the list
del top_cities[:]
print(top_cities)
# Output:
# []
