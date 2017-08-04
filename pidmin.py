import requests

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
x = "\033[0;0m"

banner="""
_______________________________________
|        .__    .___      .__         |
| ______ |__| __| _/_____ |__| ____   |
| \____ \|  |/ __ |/     \|  |/    \  |
| |  |_> >  / /_/ |  Y Y  \  |   |  \ |
| |   __/|__\____ |__|_|  /__|___|  / |
| |__|           \/     \/        \/  |
|                                     |
| developed by: Salman Asad | egg sec |
|    http://github.com/salman1410/    |
|_____________________________________|
"""

def main():
	o = open("panels.txt","r");
	url = raw_input("enter url:~# ")
	print y+"\n[!]searching, please wait..."+x
	while True:
		panel = o.readline()
		if not panel:
			break
		x_url = "http://"+url+"/"+panel
		search = requests.head(x_url)
            	if search.status_code < 400:
			print g+"\n[+]Found:"+x, x_url
	print y+"\n[!]Done"+x

try:
	print(b+banner+x)
	main()
except (KeyboardInterrupt, SystemExit):
    print r+"\n[x]Aborted"+x
