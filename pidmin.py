#!/usr/bin/python
############################
#       pidmin v2.0        #
# developed by SALMAN ASAD #
#  github.com/salman1410/  #
############################

import requests

print "\033[1;34m                                        ___   \033[1;m"                                  
print "\033[1;34m _____         _                       / _ \  \033[1;m"                              
print "\033[1;34m|  _  | *     | |            *   v2.0 /_/ \ \ \033[1;m"       
print "\033[1;34m| |_| | _  ___| | _________  _  _____     / / \033[1;m"
print "\033[1;34m|  ___|| ||  _  ||  _   _  || ||  _  |   / /  \033[1;m" 
print "\033[1;34m| |    | || |_| || | | | | || || | | |  / /   \033[1;m"
print "\033[1;34m|_|    |_||_____||_| |_| |_||_||_| |_| / /___ \033[1;m"
print "\033[1;34m     https://github.com/salman1410    /______|\033[1;m"

try:
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
			print "\033[1;32m[+]FOUND:\033[1;m",finallink
#		else:
#			print "\033[1;31m[-]NOTFOUND:\033[1;m",finallink
	
		     
except (KeyboardInterrupt, SystemExit):
    print "\n\t\033[1;31m[!]ABORTED\033[1;m"

