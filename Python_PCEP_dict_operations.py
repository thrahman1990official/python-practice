# dictionary-operations
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
# Output:
# {'John': 'A-', 'Anne': 'B'}
grades['Anne'] = 'A'
print(grades)
# Replace the grade of Anne from B to A
# Output:
# {'John': 'A-', 'Anne': 'A'}
grades.update({'John':'A'})
print(grades)
# Updates the value of John
# Output:
# {'John': 'A', 'Anne': 'A'}
len(grades)
# Returns the number of entries in the dictionary, so in this case, one if John and the other is Anne
# Output:
# 2
if 'John' in grades:
    print('John got:', grades['John'])
# Output:
# John got: A
del grades['John']
print(grades)
# Output:
# {'Anne': 'A'}
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for el in grades:
    print(el)
# Output:
# John
# Anne
for el in grades.keys():
    print(el)
# Output:
# John
# Anne
