user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
  print('You can apply for German student exchange programme')
else:
  print('Sorry, you do not qualify')

#Output:
#What's your age? 26
#What's your country? Germany
#Sorry, you do not qualify

user_country = input('What is your country?')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
  print('You can apply for Scandinavian student exchange programme')
else:
  print('Sorry, you do not qualify')

