#!/usr/bin/python
import sys, socket, os

while 1:
	content = raw_input("0:exit  1:nslookup  2:dns pulash  3 Bping \t")

	if content=='0':
		sys.exit(0)

	if content=='1':
		domain=raw_input("you domain: ")
		# print "you damioan is :%s" %(domain)
		try:
			result = socket.getaddrinfo(domain, None)   
			print "you server IP: %s" %(result[0][4][0])
		except Exception, e:
			print domain + "\t | not find"

	if content=='2':
		command="ipconfig /flushdns"
		os.system(command) 

	if content=='3':
		f = open("ping.txt",'r')
		lines = f.readlines()
		for domains in lines:
			line=domains.replace("\n","")
			try:
				ip = socket.getaddrinfo(line, None)
				print line + "\t | "+ ip[0][4][0]
			except Exception, e:
				print line + "\t | not find"
		f.close()
