name_original = 'Talhahshah'
name_new = name_original
name_original = 'Rahmansultan'
print(name_original, name_new)

# Output:
# Rahmansultan Talhahshah

list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
# Output:
# Original: [-5, 2, 3]
# New: [-5, 2, 3]
#---------------------------------------------------------------
# Below is an example of the same above code except with slicing
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
Original: [-5, 2, 3]
New: [1, 2, 3]
