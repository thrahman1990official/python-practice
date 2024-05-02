while True:
    name = input('Enter your name or EXIT to close program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
# Output:
# Enter your name or EXIT to close program: Talhahshah
# Hello Talhahshah
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
# Output below:   
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 11
# 12
# 13
# 14
# 16
# 17
# 18
# 19
