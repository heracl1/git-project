#!/usr/local/bin/python3
import socket, struct
vlan_name=input("Введите название влана:")
vlan_id=input("номер vlan: ")
oper_name=input("Название оператора:")
oper_as=input("ASN:")
ip_local=input("IP address/mask: ")
ip_peer=input("Peer IP:")   


######################################### Подсчет дреса сети
ipbox=ip_local.split('/')
#Работа с IP адресами
a=ipbox[0].split('.')
# Преобразуем ip адрес в целое число 
ip = (int(a[0])<<24)+(int(a[1])<<16)+(int(a[2])<<8)+(int(a[3]))
# Преобразуем маску в число
size = 2 ** (32 - int(ipbox[1]))
# Получаем адрес сети
net_address = int(ip/size)*size
# Форматируем адрес сети в привычный вид
net=socket.inet_ntoa(struct.pack('!L', net_address))
##########################################

vlan_template=['set vlans {} vlan-id {}',
               'set vlans {} l3-interface irb.{}']

print(vlan_template[0].format(vlan_name,vlan_id))
print(vlan_template[1].format(vlan_name,vlan_id))
print("set protocols bgp group peers-direct neighbor ",ipbox[0]," description \"-- ",oper_name," AS(",oper_as,")\"", sep='')
print("set protocols bgp group peers-direct neighbor {} export reject-martians-ipv4".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export reject-small-ipv4".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export export-peers".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} export clean-our-communities".format(ip_peer))
print("set protocols bgp group peers-direct neighbor {} peer-as {}".format(ip_peer,oper_as))
print("set policy-options policy-statement export-direct-routes term export-local from route-filter {}/{} exact".format(net,ipbox[1]))