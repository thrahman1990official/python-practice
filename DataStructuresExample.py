#list of the major tech companies
techList = ["Cisco", "Microsoft", "Samsung", "Google", "Dell", "HP"]
#Check if Microsoft is in tech list
print("Microsoft" in techList)
#if you want to let us say change the name of the second company on the list with another company
techList[2] = "Tesla"
print(techList)
#if you want to remove Cisco from your list, this is how you do it
techList.remove("Cisco")
print(techList)
#if you want to insert a company such as Neflix between Samsung and Google
techList.insert(3, "Tesla");
print(techList)
#clearing list of names in techList
techList.clear()
print(techList)

#below is an example of different fruit and prices of those fruits
fruits = {'banana': 0.49, 'orange': 1.5, 'apple': 1.09}
#below is how to change price of the banana
fruits['banana'] = 2.60
print(fruits)
#below is to display only price of the orange from the list
print(fruits['orange'])
#below is to add a new fruit such as melon with 3 as it's price
fruits['melon'] = 3
print(fruits)
