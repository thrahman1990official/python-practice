# dictionary-operations
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
# Output:
# {'John': 'A-', 'Anne': 'B'}
grades['Anne'] = 'A'
print(grades)
# Output:
# {'John': 'A-', 'Anne': 'A'}
grades.update({})
