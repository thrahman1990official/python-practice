top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:', city)
# Output:
# Current city: New York City
# Current city: Los Angeles
# Current city: Chicago
# Current city: Houston
# Current city: Phoenix
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index], )
# Output:
# Current index: 0 | Current city: New York City
# Current index: 1 | Current city: Los Angeles
# Current index: 2 | Current city: Chicago
# Current index: 3 | Current city: Houston
# Current index: 4 | Current city: Phoenix

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)
# Output:
# Money spent: 158.1


