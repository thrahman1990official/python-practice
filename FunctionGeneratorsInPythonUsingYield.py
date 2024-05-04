# Generators are the functions in Python which return the repeated sets of items. They are used to create iterators. In Python, the “yield” keyword is used to create the generators.
def demo_gen():
    num = 10
    print('Statement number 1')
    yield num
    num += 1
    print('Statement number 2')
    yield num
    num += 1
    print('Statement number 3')
    yield num
for item in demo_gen():
    print(item)

# Output:
# Statement number 1
# 10
# Statement number 2
# 11
# Statement number 3
# 12

