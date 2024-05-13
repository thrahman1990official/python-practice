numbers = [1, 2, 3, 4]
countries = ['UK', 'US', 'Germany']
countries = [1, 'UK', 2, 'US']
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
# Output:
# ['A1', 'A2', 'A3']
print(cells[0][0])
# Output:
# A1
print(cells[0][1])
# Output:
# A2
print(cells[1][2])
# Output:
# B3
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
# Output:
# Element: ['A1', 'A2', 'A3']
# Element: ['B1', 'B2', 'B3']

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
# Output:
# Element: A1
# Element: A2
# Element: A3
# Element: B1
# Element: B2
# Element: B3

table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)
# Output:
# Element: A1
# Element: A2
# Element: A3
# Element: B1
# Element: B2
# Element: B3

table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
# Output
# A1 A2 A3
# B1 B2 B3

table = [[i for i in range(1,6)] for j in range(4)]
print(table)
# Output:
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
