//function example
//device_type will be the name of the function whereas device will be input argument
def device_type(device): 
    if device == '1800':
      return "It's Cisco router"
    if device == '2900':
      return "It's Cisco router"
    if device == '3750':
      return "It's Cisco switch"
    if device == '2950':
      return "It's a Cisco switch"
what_device = input("Enter Device Number [1800,2900,3750,2950]):")
answer = device_type(what_device)

print(answer)



