#!/usr/local/bin/python3
#vlan_name=input("Введите название влана:")
#vlan_id=input("номер vlan: ")
oper_name=input("Название оператора:")
oper_as=input("ASN:")
ip_local=input("IP address/mask: ")
ip_peer=input("Peer IP:")              
"""vlan_template=['set vlans {} vlan-id {}',
               'set vlans {} l3-interface irb.{}']

print(vlan_template[0].format(vlan_name,vlan_id))
print(vlan_template[1].format(vlan_name,vlan_id))
"""
ipbox=ip_local.split('/')

print("set protocols bgp group peers-direct neighbor ",ipbox[0]," description \"-- ",oper_name," AS(",oper_as,")\"", sep='')
print("set protocols bgp group peers-direct neighbor {} export reject-martians-ipv4".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export reject-small-ipv4".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export export-peers".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export clean-our-communities".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} peer-as {}".format(ip_peer,oper_as))

print("IP={}, Prefix={}".format(ipbox[0], ipbox[1]))
