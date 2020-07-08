#! /usr/bin/env python3

import os
# from pyping.core import *

# if os.path.exists('reachable_ip.txt'):
# 	os.remove('reachable_ip.txt')

third_octet = range(4)
last_octet = range(1,10)

for ip3 in third_octet:
	for ip4 in last_octet:
		ip = '192.168.'+str(ip3) +'.'+ str(ip4)
		ping_result = pyping.ping(ip)
		f = open('reachable_ip.txt','a')
		if ping_result.ret_code == 0:
			print(ip + 'is reachable.')
			f.write(ip + "\n")
		else:
			print(ip + 'is not reachable.')

f.close()
