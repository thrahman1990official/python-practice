#Write python program to find if given number is prime or not

#prime number :- 2, 3, 5, 7

#9 :- No. 1, 3, 9

num = int(input("Enter number to verify if it is prime"))
flag = False
if num > 1:
  for i in range(2, num//2)
    if num % i == 0
     flag = True
      break
if flag:
   print(num, "is not prime number")
else:
   print(num, "is prime number")
