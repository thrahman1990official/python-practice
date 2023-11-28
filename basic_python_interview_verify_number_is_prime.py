#Write python program to find if given number is prime or not

#prime number :- 2, 3, 5, 7

#9 :- No. 1, 3, 9

num = int(input("Enter number to verify if it is prime"))
flag = False
if num > 1: #prime number is a natural number greater than one
  for i in range(2, num//2): #for the range of numbers are starting from from 2 end till 4
    if num % i == 0:
     flag = True
      break
if flag:
   print(num, "is not prime number")
else:
   print(num, "is prime number")
