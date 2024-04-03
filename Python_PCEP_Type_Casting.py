height_cm = input('Height converter: enter height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48)
#the above three lines can be written like this below
height_cm = float(input('Height converter: enter height in cm: '))
print('Your height in feet is:', height_cm / 30.48)
#another example using in
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')
#another example of type casting
temp_c = input('Enter temperature today in Celsius degree: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + 'degrees Fahrenheit'
print(temp_statement)
