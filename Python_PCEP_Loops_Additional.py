for i in range(11):
    pass
# pass instruction will prevent the code from throwing errors
# below is example of simple multipication table from one to five
for a in range(1,6):
    for b in range(1,6):
         print(a, 'x', b, '=', a * b)
# Output below:    
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)
# Output below:    
# else: 5
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)
# Output below:    
# 2
# 3
# 4
# else: 5
