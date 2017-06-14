#!/usr/bin/python
############################
#       pidmin v1.0        #
# developed by SALMAN ASAD #
#                          #
############################

import requests

welcome="""
 _____  _                    _                                      
|  _  ||_|     _            |_|   v1.0       
| |_| | _  ___| | _________  _  _____ 
|  ___|| ||  _  ||  _   _  || ||  _  | 
| |    | || |_| || | | | | || || | | |
|_|    |_||_____||_| |_| |_||_||_| |_|
              developed by SALMAN ASAD"""

def Admin():
	o = open("panels.txt","r");
	targetlink = raw_input("\nenter target url:")
	print "searching for admin panel, please wait...\n"
	while True:	
		panellink = o.readline()
		if not panellink:
			break
		finallink = "http://"+targetlink+"/"+panellink
		search = requests.head(finallink)
            	if search.status_code < 400:
			print "[+]FOUND:",finallink
		     

print(welcome)
Admin()
print "search complete"
