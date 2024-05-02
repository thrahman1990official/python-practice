for letter in 'hello!':
    print('Current letter:', letter)
# Output:
# Current letter: h
# Current letter: e
# Current letter: l
# Current letter: l
# Current letter: o
# Current letter: !

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

for counter in range(1,11):
    print(counter)
print('Finished!')
# 1 is the start value and 11 is the stop value
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
# if you remove 1 then a default value of 0 will be used
for counter in range(11):
    print(counter)
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
for counter in range(1, 11, 2):
    print(counter)
print('Finished!')
# 1 will be start value , 11 will be stop value , and 2 will be the incremented increase
# Output:
# 1
# 3
# 5
# 7
# 9
# Finished!
