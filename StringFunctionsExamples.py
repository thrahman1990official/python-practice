# len(s) -> Returns # of items in an object whether it is string or variables
# str(s) -> Converts specified values such as a variable into a string
# upper() -> Converts string into upper case
# count(sub[, start[, end]]) -> Returns # of times specified value is found in the string
# isupper() -> boolean for string which returns true if ALL characters inside the string are upper case, but if one or more is lower it will display false
# islower() -> boolean for string which return true if ALL characters inside the string are lower case, but if one or more is upper it will display false
# split(sep=None, maxsplit=-1) -> splits string at specified separator
# rsplit -> splits string into list, starting from right
# strip() -> returns trimmed version of string
# lstrip([chars]) -> Removes any leading characters
# rstrip([chars]) -> Removes any trailing characters
# replace(old, new[, count]) -> Replaces specified phrase with another specified phrase
# find(sub[, start[, end]]) -> Searches string for specified & returns positive
# index(sub[, start[, end]]) -> Searches string for specified value & returns positive
#let us say variable 
t = "Talha The Tiger"
m = "131415"
print(len(t))
#should output 15, although TalhaTheTiger has 5 + 3 + 5 = 13 characters BUT there is space in front of Tiger and after Talha making it 15
#convert variable r to string
s = str(m)
#display the location where this strong starts from
print(s.find("13"))
#should output 0
print(s.find("14"))
#should output 2
print(s.find("15"))
#should output 4
#now we want to convert all characters of t into upper regardless if we already have upper characters in it
print(t.upper())
#should return TALHA THE TIGER
#now we want to convert all characters of t into lower regardless if we already have lower characters in it
print(t.lower())
#should return talha the tiger
r = "Rahman Robotics Rahman Robotics Rahman Robotics"
print(r.count("Robotics", 10, 30))
#should output 0
print(r.count("Rahman", 10, 30))
#should output 1
#assigning h as all string characters of t converted into upper case
h = r.upper()
print(h.isupper())
#should output true
print(h.islower())
#should output as false
