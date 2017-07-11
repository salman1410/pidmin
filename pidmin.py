#!/usr/bin/python
############################
#       pidmin v2.0        #
# developed by SALMAN ASAD #
#  github.com/salman1410/  #
############################

import requests

print "\033[1;34m        .__    .___      .__        ________  \033[1;m"
print "\033[1;34m ______ |__| __| _/_____ |__| ____  \_____  \ \033[1;m"
print "\033[1;34m \____ \|  |/ __ |/     \|  |/    \  /  ____/ \033[1;m"
print "\033[1;34m |  |_> >  / /_/ |  Y Y  \  |   |  \/       \ \033[1;m"
print "\033[1;34m |   __/|__\____ |__|_|  /__|___|  /\_______ \\033[1;m"
print "\033[1;34m |__|           \/     \/        \/         \/\033[1;m"
print "\033[1;34m         https://github.com/salman1410        \033[1;m"  

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

