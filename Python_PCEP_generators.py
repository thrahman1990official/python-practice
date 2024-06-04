# below is an example of generator
def get_number():
    for i in range(1, 4):
        yield i
generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))
# Output:
# 1
# 2
# 3
