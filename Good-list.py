import os,sys
R="\033[0;35m"
G='\033[0;32m'
try:
	Files=input(G+'Enter Name The List : ')
	file=open(Files,'w')
except:
	sys.exit()
os.system('clear')
print("\033[0;31m")
print('''
  ____                 _       _     _     _
 / ___| ___   ___   __| |     | |   (_)___| |_
| |  _ / _ \ / _ \ / _` |_____| |   | / __| __|       | |_| | (_) | (_) | (_| |_____| |___| \__ \ |_
 \____|\___/ \___/ \__,_|     |_____|_|___/\__|
''')
print(R+'-'*50)
print('\033[0;33mCoding bay issam iso \033[0;32m')
print(R+'-'*50+G)
def passwordlist():
	lists=set([])
	lists2=set([])
	Namber=0
	while True:
		Namber+=1
		command=input('Enter {} : '.format(Namber))
		if command=="exit":
			break;
		lists.add(command)
	for i in lists:
		if i not in lists2:
			lists2.add(i)
			for por in lists2:
				finall=i+por
				file.write(finall+'\n')
	print(R+'-'*50)
	print('\033[0;31mSave Password file --> {} '.format(Files))
	print(R+'-'*50)
try:	
	passwordlist()
except:
	sys.exit()