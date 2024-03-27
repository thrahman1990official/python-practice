def create_vlans(vlan_number, vlan_name)
  return {'vlan': vlan_number, 'name': vlan_name}
vlan_number = input("Enter VLAN number:")
vlan_name = input("Enter VLAN name:")
display_vlan = create_vlans(vlan_number, vlan_name)

print(display_vlan)
