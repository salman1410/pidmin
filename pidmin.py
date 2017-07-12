#!/usr/bin/python
############################
#         pidmin           #
# developed by SALMAN ASAD #
#  github.com/salman1410/  #
############################

import requests

print \
"""
        .__    .___      .__        ________  
 ______ |__| __| _/_____ |__| ____  \_____  \ 
 \____ \|  |/ __ |/     \|  |/    \  /  ____/ 
 |  |_> >  / /_/ |  Y Y  \  |   |  \/       \ 
 |   __/|__\____ |__|_|  /__|___|  /\_______ \ 
 |__|           \/     \/        \/         \/ 
         https://github.com/salman1410
"""          

def main():
	o = open("panels.txt","r");
	targetlink = raw_input("\nenter target url~: ")
	print "searching, please wait...\n"
	while True:	
		panellink = o.readline()
		if not panellink:
			break
		finallink = "http://"+targetlink+"/"+panellink
		search = requests.head(finallink)
            	if search.status_code < 400:
			print "[+]FOUND:",finallink
		
def complete():
	print "\n\t[!]COMPLETED"
try:
	main()
	complete()
except (KeyboardInterrupt, SystemExit):
    print "\n\t[X]ERROR: aborted by user"
