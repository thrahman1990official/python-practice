user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
  print('You can apply for German student exchange programme')
else:
  print('Sorry, you do not qualify')

#Output:
#What's your age? Age_Entered_By_User_In_Integer
#What's your country? Name_Of_Country_Entered_By_User_String
#Sorry, you do not qualify

user_country = input('What is your country?')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
  print('You can apply for Scandinavian student exchange programme')
else:
  print('Sorry, you do not qualify')

#Output:
#What is your country? Name_Of_Country_Entered_By_User
#You can apply for Scandinavian student exchange programme

user_country = input('Where do you come from? ')
if not user_country == 'Germany':
  print('you are not from Germany!')
else:
  print('you are from Germany')

#Output:
#Where do you come from? Germany
#you are not from Germany!

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
        print('You qualify!')
else:
        print('You don\'t qualify!')
#Output:
#What is your age? Number_Entered_By_User
#What is your country? Country_Entered_By_User
#Should print You Qualify or You don't qualify
