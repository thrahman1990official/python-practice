def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))
# The average is: 7.24
# Another way to write the above code:
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')
# Output:
# The average is too high!
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')

get_average([2])
# Output:
# 2.0

