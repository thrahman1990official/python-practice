#list of the major tech companies
techList = ["Cisco", "Microsoft", "Samsung", "Google", "Dell", "HP"]

#if you want to let us say change the name of the second company on the list with another company
techList[2] = "Tesla"
print(techList)

#if you want to remove Cisco from your list, this is how you do it
techList.remove("Cisco")
print(techList)

#if you want to insert a company such as Neflix between Samsung and Google
techList.insert(3, "Tesla");
print(techList)
