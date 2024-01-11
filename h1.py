import hashlib
from urllib import urlopen
import os

os.system('clear')
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prCyan('''


			 $$$$$$\                               $$\                                  $$$$$$\            $$\ $$\                     
			$$  __$$\                              $$ |                                $$  __$$\           $$ |\__|                    
			$$ /  \__| $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\        $$ /  $$ |$$$$$$$\  $$ |$$\ $$$$$$$\   $$$$$$\  
			$$ |      $$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\       $$ |  $$ |$$  __$$\ $$ |$$ |$$  __$$\ $$  __$$\ 
			$$ |      $$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|      $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$$$$$$$ |
			$$ |  $$\ $$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$   ____|
			\$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |             $$$$$$  |$$ |  $$ |$$ |$$ |$$ |  $$ |\$$$$$$$\ 
			 \______/ \__|      \_______| \_______|\__|  \__| \_______|\__|             \______/ \__|  \__|\__|\__|\__|  \__| \_______|
                              
                              					by Abdee52_                                                                                             
                                                                                                                           

''')
prGreen("===============================================")
prGreen("[1] Crack SHA1")
prGreen("[2] Crack SHA224")
prGreen("[3] Crack SHA256")
prGreen("[4] Crack SHA384")
prGreen("[5] Crack MD5")
prGreen("===============================================")
print("\n")

choose = raw_input("[+] Please choose one option: ")
print("\n")
if choose == '1':
	hashpass = str(raw_input("HASH: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.sha1(p).hexdigest()
		if z == hashpass:
			prCyan("Password: {} 	HASH: {}".format(p,z))

if choose == '2':
	hashpass = str(raw_input("HASH: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.sha224(p).hexdigest()
		if z == hashpass:
			prCyan("Password: {} 	HASH: {}".format(p,z))

if choose == '3':
	hashpass = str(raw_input("HASH: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.sha256(p).hexdigest()
		if z == hashpass:
			prCyan("Password: {} 	HASH: {}".format(p,z))

if choose == '4':
	hashpass = str(raw_input("HASH: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.sha384(p).hexdigest()
		if z == hashpass:
			prCyan("Password: {} 	HASH: {}".format(p,z))
   

if choose == '5':
	hashpass = str(raw_input("HASH: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.md5(p).hexdigest()
		if z == hashpass:
			prCyan("Password: {} 	HASH: {}".format(p,z))
   


