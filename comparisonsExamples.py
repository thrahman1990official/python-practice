#if talhah is assigned as 5 is greater than 4
talhah = 14>13
#it should print true
print(talhah)

#if rahman is assigned as 5 not equal to 4
rahman = 14!=13
#it should print true
print(rahman)

#if hamdur is assigned as 5 equal to 4
hamdur = 14==13
#it should print false
print(hamdur)

#if rentTalhah is equal to 1500
rentTalhah = 1500
#it should print true in either case because rentTalhah is greater than 1000 or rentTalha is less than 2000
print(rentTalhah > 1000 or rentTalhah < 2000)

#if rentRahman is equal to 3000
rentRahman = 3000
#it should print false since rentRahman is not less than 2500 even though it is greater than 2000
print(rentRahman > 2000 and rentRahman < 2500)

#Below is an example of the current car speed on a Canadian highway in the province of Ontario
#if it goes above 120, it is fine plus demerit points
#if it goes under 100, unless there is huge traffic, it is fine but no demerit points
speedCarHighway = 130
if speedCarHighway > 120:
  print("Police: You drive too fast, you are getting fine plus demerit points")
elif speedCarHighway < 100:
  print("Police: You drive too slow, you are getting fine but no demerit points")
else:
  print("Driver: This is right speed range not too get a ticket, don't need to worry about getting pulled over")

