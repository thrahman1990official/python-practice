fav_band = 'Darkroom Familia'
# Below print statement will only print letter at the index #4 of the string
print(fav_band[4])
# Output:
# r

fav_band = 'Darkroom Familia'
# Below print statement will print letters that are before index #4 of the string
# Meaning letters starting from #0 till #3 of the index
print(fav_band[:4])
# Output:
# Dark

user_number = input('Please provide number: ')
if user_number.isnumeric():
    print('Thank you, that\'s correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
# Input:
# Please provide number:
# 15
# Output:
# Thank you, that's correct number!
# Input:
# Please provide number:
# 15a
# Output:
# Sorry, 15a is not a number!

text = 'Hail Lord Allah The King Of Heavens and Earth'
text_cap = text.upper()
print(text_cap)
# Output:
# HAIL LORD ALLAH THE KING OF HEAVENS AND EARTH
