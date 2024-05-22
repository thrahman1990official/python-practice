# Below is an example of Dictionaties
# Dictionaries are collections used to store key value pairs
emails = {
'Anne Stahl': 'astahl@gmail.com',
'Peter Small': 'peters@yandex.com',
'Mark Steel': 'mark@steel.com'
}
print(emails['Mark Steel'])
# Output:
# mark@steel.com
spanish_animals = {
  'dog': 'el perro',
  'cat': 'el gato',
  'horse': 'el caballo',
  'bird': 'el pajaro'
}
print(spanish_animals['bird'])
# Output:
# el pajaro
spanish_animals = {
  'dog': 'el perro',
  'cat': 'el gato',
  'horse': 'el caballo',
  'bird': 'el pajaro',
  'bird': 'el ave'
}
# if you print the whole dictionary
print(spanish_animals)
# Output:
# {'dog': 'el perro', 'cat': 'el gato', 'horse': 'el caballo', 'bird': 'el ave'}
# the first bird will be replaced by the second bird
