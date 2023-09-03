# FIRST IMPORTS
import os
import sys
import time
import asyncio
import warnings
import datetime
from time import sleep

#SILENCE
warnings.filterwarnings('ignore')

#COLORS
st     = "\033[1;"
red    = f"{st}31;40m"
green  = f"{st}32;40m"
yellow = f"{st}33;40m"
blue   = f"{st}34;40m"
purple = f"{st}35;40m"
cyan   = f"{st}36;40m"
white  = f"{st}37;40m"
reset  = white

#DEF CLEAR
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#CHECKING MANUAL MODULES
try :
    clear()
    import bs4
except ModuleNotFoundError:
       os.system('pip install bs4')
       sleep(3)
       clear()

try :
    import requests
except ModuleNotFoundError:
       os.system('pip install requests')
       sleep(3)
       clear()

try :
    import requests_toolbelt
except ModuleNotFoundError:
       os.system('pip install requests_toolbelt -q')
       sleep(3)
       clear()

       #claimbits_v3
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import os
def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()


st     = "\033[1;"
red    = f"{st}31;40m"
green  = f"{st}32;40m"
yellow = f"{st}33;40m"
blue   = f"{st}34;40m"
purple = f"{st}35;40m"
cyan   = f"{st}36;40m"
white  = f"{st}37;40m"
reset  = white

import requests
import json
import sys
import re
import datetime
import base64
import random

from time import sleep
from bs4 import BeautifulSoup as Soup
from getpass import getpass

def slow(text) :
        for word in text:
            print (word, end ="", flush=True)
            sleep(0.009)

def baner():
    baner = f'''
{cyan}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{cyan}┗┑ {green}╔═╗╦═╗ ╦╔╦╗╔═╗╔═╗╔╗╔  ╔═╗╦═╗╦ ╦╔═╗╔╦╗╔═╗ {cyan}┍┛
{cyan} │ {red}╚═╗║╔╩╦╝ ║ ║╣ ║╣ ║║║  ║  ╠╦╝╚╦╝╠═╝ ║ ║ ║ {cyan}│
{cyan}┏┙ {green}╚═╝╩╩ ╚═ ╩ ╚═╝╚═╝╝╚╝  ╚═╝╩╚═ ╩ ╩   ╩ ╚═╝{reset}{cyan} ┕┓
{cyan}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n'''
    slow (baner)
    sleep(2)

 #DEF PASS ROTATOR
def pass_rotator():

 c = requests.session()
 now = datetime.datetime.now()
 date = now.strftime("%A")

  #WEB FOR INTERNAL PASSWORD
 try:

    url = 'https://rentry.co/websites-scripts/raw'
    req = c.get(url)
    res = Soup(req.content, "html.parser")
    data = res.prettify()
    js = json.loads(data)
    password = js[f'{date}']

    #WEB FOR PASS DISPLAY
    url = 'https://rentry.co/websites-scripts_dates/raw'
    req = c.get(url)
    res = Soup(req.content, "html.parser")
    data = res.prettify()
    js = json.loads(data)
    link = js[f'{date}1']
    link1 = js[f'{date}2']

    if os.path.exists("config/.pass.txt"):
       passw = open("config/.pass.txt").read()
       if passw == password:
          baner()
          print (f" {green}𝗔𝗖𝗖𝗘𝗦𝗦 𝗚𝗥𝗔𝗡𝗧𝗘𝗗 𝗣𝗔𝗦𝗦 𝗪𝗔𝗦 𝗔𝗟𝗥𝗘𝗔𝗗𝗬 𝗦𝗔𝗩𝗘𝗗{reset}")
          slow (cyan+"—".center(47, '—')+"\n")
          sleep(2)
       else:
           while True:
             baner()
             print (f" {green}𝕡𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕝𝕚𝕟𝕜 𝕆𝕟𝕖 {reset}: {purple}{link}{reset}")
             print (f" {green}𝕡𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕝𝕚𝕟𝕜 𝕋𝕨𝕠 {reset}: {cyan}{link1}{reset}")
             print (cyan+"—".center(47, '—'))
             pas = getpass(f" {blue}ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴘᴀssᴡᴏʀᴅ დ \n {red}»{reset} ")
             if pas == password:
                slow (f" {green}𝗔𝗖𝗖𝗘𝗦𝗦 𝗚𝗥𝗔𝗡𝗧𝗘𝗗{reset}\n")
                slow (cyan+"—".center(47, '—')+"\n")
                with open('config/.pass.txt', "w") as txt:
                     txt.write(pas)
                     sleep(2)
                     break
             else:
                 slow (f" {red}𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗{reset}\n")
                 sleep(2)
                 clear()

    if not os.path.exists("config/.pass.txt"):
       while True:
             baner()
             print (f" {green}𝕡𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕝𝕚𝕟𝕜 𝕆𝕟𝕖 {reset}: {purple}{link}{reset}")
             print (f" {green}𝕡𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝕝𝕚𝕟𝕜 𝕋𝕨𝕠 {reset}: {cyan}{link1}{reset}")
             print (cyan+"—".center(47, '—'))
             passw = getpass(f" {blue}ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ დ \n {purple}»{reset} ")
             if passw == password:
                print (f" {green}𝗔𝗖𝗖𝗘𝗦𝗦 𝗚𝗥𝗔𝗡𝗧𝗘𝗗{reset}")
                slow (cyan+"—".center(47, '—')+"\n")
                with open('config/.pass.txt', "w") as txt:
                     txt.write(passw)
                     txt.close()
                     sleep(2)
                     break
             else:
                 print (f" {red}𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗{reset}")
                 sleep(2)
                 clear()

 except (ConnectionError,requests.exceptions.ConnectionError) as e:
        print (f"{red} ɴᴏ ɪɴᴛᴇʀɴᴇʀᴛ ᴄᴏɴɴᴇᴄᴛɪᴏɴ{reset}")
        exit(1)
 except KeyboardInterrupt:
        pass
        exit(1)

 clear()
 os.system("xdg-open https://www.youtube.com/@anonymoussixteen")
 try:
    input (" sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ... ᴘʀᴇss ᴇɴᴛᴇʀ ᴡʜᴇɴ ᴅᴏɴᴇ...")
    sleep(1)
    clear()
 except:
       pass

def banner():
    print (f"""{green}

╔═════════════════════════════════════════════════════╗
║                                                     ║
║  {red} _______                            _____________{green}  ║
║   {red}___    |________________________  ___<  /_  ___/{green}  ║
║   {cyan}__  /| |_  __ \  __ \_  __ \_  / / /_  /_  __ \{green}   ║
║   {cyan}_  ___ |  / / / /_/ /  / / /  /_/ /_  / / /_/ /{green}   ║
║   {blue}/_/  |_/_/ /_/\____//_/ /_/_\__, / /_/  \____/{green}    ║
║                              {blue}/____/{green}                 ║
║                                                     ║
╠══════════════════════════╗       ╔══════════════════╣
║  {white}Script  :  {green}Macro-Bit    ╠═══════╝ {white}version : [{green}1.0.1{white}]{green}║
║  {white}Author  :  {green}Rashy    ╔═══╝                          ║
║  {white}Country :  {green}Zimbabwe{green} ║{white} Channel : {green}@anonymoussixteen  ║
╠══════════════════════╩══════════════════════════════╣
║   {white}Donate TRX : {yellow}TGBkWNfvePzJGHB6SrsJ2vvw1zymTApjB6{green}   ║
╠═════════════════════════════════════════════════════╝{reset}""")


def timer (t):
     try:
        while t:
          mins, secs = divmod(t, 60)
          timer = '{:02d}m:{:02d}s'.format(mins, secs)
          x = datetime.datetime.now().strftime("%X")
          print (f"{reset}\r [{cyan}{x}{reset}] please wait {cyan}-»", timer, end="           \r")
          sleep(1)
          t -= 1
     except SystemExit:
           sys.exit("                     \r")

def media_image(x):
    while True:
          try:

             url    = f'https://api-secure.solvemedia.com/papi/_challenge.js?k={x};f=_ACPuzzleUtil.callbacks[0];l=en;t=img;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome112,os/android,os/android9,fwv/AJijUw.mydy22,jslib/jquery,htmlplus;am=gkT3aliR7J-C3FrcWJHsnw;ca=ajax;ts=1693304630;ct=1693305299;th=white;r=0.6298777439249539'
             req    = c.get(url)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()

             chid   = re.search('"chid"     : "(.*)",',data)[1]
             url    = f'https://api-secure.solvemedia.com/papi/media?c={chid};w=300;h=150;fg=000000;bg=f8f8f8'
             media  = c.get(url)
             img    = media.content
             with open('config/.img.jpg', "wb") as picture:
                  picture.write(img)
                  picture.close()
                  return chid
                  break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError) as E :
                  sys.stdout.write(f" {red} Mantain Good Connection {reset}    \r")

def imgsolver():
    apikey_list = ["K82801409388957", "K89244761888957", "K81467461288957", "K83423491388957", "K81658559088957"]

    with open("config/.img.jpg", "rb") as image_file:
         image_data = image_file.read()
         base64_string = base64.b64encode(image_data).decode("utf-8")

    payload = ("data:image/jpeg;base64,%s" % (base64_string))
    data = {
            "apikey": random.choice(apikey_list),
            "base64Image": payload,
            "isOverlayRequired": True,
            "language": "eng",
            "OCREngine": 2
           }

    try:
       response = c.post("https://api.ocr.space/parse/image", data=data)
       data = json.loads(response.text)
       text = data["ParsedResults"][0]["TextOverlay"]["Lines"][1]["LineText"]
       return text
    except IndexError:
           pass


def media_audio(x):
    while True:
          try:

             url    = f'https://api-secure.solvemedia.com/papi/_challenge.js?k={x};f=_ACPuzzleUtil.callbacks%5B0%5D;l=en;t=img;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome80,os/android,os/android10,fwv/AA.1DQ.nrar21,jslib/jquery,htmlplus;am=d3ZY-YsCksp3ea4aiwKSyg;ca=ajax;ts=1685754216;ct=1685754502;th=white;r=0.440799585296759'
             req    = c.get(url)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()

             chid   = re.search('"chid"     : "(.*)",',data)[1]
             url2   = f'https://api-secure.solvemedia.com/papi/_challenge.js?k={x};f=_ACPuzzleUtil.callbacks%5B1%5D;l=en;t=aud;s=standard;c=js,h5c,h5ct,svg,h5v,v/h264,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome114,os/android,os/android10,fwv/AMAkgA.hokf37,jslib/jquery,htmlplus;am=TKzjW7dRMUtMbFvWt1ExSw;ca=script;p={chid};ts=1689600229;ct=1689640168;th=white;r=0.1503411687485281'
             req    = c.get(url2)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()

             chid2   = re.search('"chid"     : "(.*)",',data)[1]
             url3    = f'https://api-secure.solvemedia.com/papi/media?c={chid2};w=300;h=150;fg=000000;bg=f8f8f8;aa=1'
             media   = c.get(url3)
             aud     = media.content

             with open('config/audio.mp3', "wb") as picture:
                  picture.write(aud)
                  picture.close()
                  return chid2
                  break
          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError) as E :
                  sys.stdout.write(f" {red} Mantain Good Connection {reset}    \r")


def audioToText(audioFile, api_key):
    endpoint = "https://api.assemblyai.com/v2/upload"
    headers = {
            "authorization": api_key,
            "content_type": "application/json"
            }
    def read_file(filename):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(5242880)
                if not data:
                    break
                yield data

    response = requests.post(endpoint, headers=headers, data=read_file(audioFile))
    audio_url= response.json()['upload_url']
    transcript_request = {'audio_url': audio_url}
    request_endpoint = "https://api.assemblyai.com/v2/transcript"
    transcript_response = requests.post(request_endpoint, json=transcript_request, headers=headers)
    audio_id = transcript_response.json()['id']
    text = None
    while text is None:
        status_endpoint = "https://api.assemblyai.com/v2/transcript/" + audio_id
        polling_response = requests.get(status_endpoint, headers=headers)
        text = polling_response.json()['text']
    return text

def captcha(captcha_type ,capkey, api_key):
    if captcha_type == "audio":
       chid    = media_audio(capkey)
       _txt    = audioToText('config/audio.mp3', api_key)
       captcha = re.search('Please enter the following (.*).', _txt)[1].replace('-', '').replace(' ', '')
       return captcha, chid

    elif captcha_type == "image":
         chid    = media_image(capkey)
         captcha = imgsolver()
         return captcha, chid


def slow2(text) :
   for word in text:
       print (word, end ="", flush=True)
       sleep(0.009)


def slow(text) :
   for word in text:
       print (word, end ="", flush=True)
       sleep(0.005)


def _config():

    if not os.path.exists('config'):
       os.mkdir('config')
    if not os.path.exists('config/.nomedia'):
       open('config/.nomedia', 'w')

    try:
       pass#_rotator()
    except:
          sys.exit()

    if not os.path.exists('config/data.json'):
       print (cyan+"–".center(47, "–")+reset)
       sys.stdout.write(f"{red}\r")
       os.system(f'figlet Setting Up')
       print (cyan+"–".center(47, "–")+reset)
       cookie = input(f" Cookie --------» {blue}")
       sys.stdout.write(f"{reset}")
       _ua    = input(f" user agent ---» {blue}")
       sys.stdout.write(f"{reset}")
       key   = input(f" {reset}audio API key -» {blue}")
       dict  = {"api_key" : key,
                "cookie" : cookie,
                "user_agent" : _ua}
       dump  = json.dumps(dict, indent=6)
       with open('config/data.json', 'w') as file:
            file.write(dump)
            slow (cyan+"–".center(47, "–")+reset)
            sleep(2)
            clear()

    _data = json.load(open('config/data.json', 'r'))
    cookie     = _data['cookie']
    user_agent = _data['user_agent']
    api_key    = _data['api_key']
    return api_key, user_agent, cookie

def server():
    baner()
    print (f" --» Captcha Server «--")
    print (cyan+"─".center(47, "─")+reset)
    print (f" [{green}1{reset}] {blue}Image Server{reset}")
    print (f" [{blue}2{reset}] {green}Audio Server{reset}")
    slow (cyan+"–".center(47, "–")+reset+'\n')
    server_type = input(f" Captcha Server -» {blue}")
    if server_type == "2":
       sleep(2)
       clear()
       return "audio"
    else:
        sleep(2)
        clear()
        return "image"

try:
   _config_data = _config()
   cookie     = _config_data[2]
   user_agent = _config_data[1]
   api_key    = _config_data[0]
   captcha_type = server()
except KeyboardInterrupt:
       sys.exit()


c          = requests.session()
headers    = {
              "host"       : f"macrobits.io",
              "cookie"     : f"{cookie}",
              "user-agent" : f"{user_agent}",
              "accept-language" : "en-US,en;q=0.9"
              }

def get(x, headers):
    while True:
          try:

             req    = c.get(x, headers=headers)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()
             return data
             break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError) as E :
                  sys.stdout.write(f" {red} Mantain Good Connection {reset}        \r")
                  pass

def post(x, y, headers):
    while True:
          try:

             req    = c.post(x, y, headers=headers)
             res    = Soup(req.content, 'html.parser')
             data   = res.prettify()
             return data
             break

          except (ConnectionResetError,requests.exceptions.ConnectionError, ConnectionError,requests.exceptions.ChunkedEncodingError) as E :
                  sys.stdout.write(f" {red} Mantain Good Connection {reset}        \r")


print (cyan+"─".center(47, "─")+reset)
sys.stdout.write(f"{red}\r")
os.system("figlet loging In")
print (cyan+"─".center(47, "─")+reset)


data = get('https://macrobits.io/claims.html', headers)
if 'Logout' in data:
   slow (f" {green}✅ Data Verified 🔰 {reset}\n")
   print (cyan+"─".center(47, "─")+reset)
   sleep (3)
   clear ()

   bits = re.findall('''<td class="text-right text-success">
            (.*)
           </td>''',data)[0]
   user    = re.findall('''<font class="text-success">
          (.*)
         <\/font>''',data)[0]

   display = banner()
   slow2 (f"{green}║{reset} 🔰 user-name --» {green}{user}{reset} \n")
   slow2 (f"{green}║{reset} 🏧 balance ----» {green}{bits}{reset} \n")
   print (green+"╙"+"─".center(53, "─")+reset)

else:
    print (f" {red}cookie[data] expired{reset}")
    os.system("rm -rf config/data.json")
    print (cyan+"─".center(47, "─")+reset)
    sys.exit()

def _balance():
    data = get('https://macrobits.io/claims.html', headers=headers)
    balance = re.findall('''<td class="text-right text-success">
            (.*)
           </td>''',data)[0]
    x = datetime.datetime.now().strftime("%X")
    slow2 (f" 🏧 Updated balance now {green}{balance}{reset} • @{white}[{red}{x}{white}]{reset} \n")
    print (cyan+"─".center(54, "─")+reset)

def _ptc():
    try:

       url  = 'https://macrobits.io/ptc.html'
       data = get(url, headers=headers)

       sid  = re.findall("""onclick="opensite\('(.*)','""",data)[1]
       key  = re.findall("""'&key=(.*)',""",data)[0]
       url  = f'https://macrobits.io/surf.php?sid={sid}&key={key}'

       data = get(url, headers=headers)
       sec  = timer(int(re.search("var secs = (.*)\;",data)[1]))
       token   = re.search("var token = '(\w+)",data)[1]

       payload  = {"cID":"0","rT":"1","tM":"light"}
       header   = {"referer":url,"x-requested-with":"XMLHttpRequest","host":f"macrobits.io","cookie":f"{cookie}","user-agent":f"{user_agent}"}
       data     = post('https://macrobits.io/system/libs/captcha/request.php', payload, header)
       anticaps = json.loads(data)

       for anticap in anticaps :
           pay   = {"cID":"0","pC":anticap,"rT" : "2"}
           _post = post("https://macrobits.io/system/libs/captcha/request.php", pay, header)

           payload = {"a":"proccessPTC","data":sid,"token":token,"captcha-idhf" : "0","captcha-hf":anticap}
           data    = post('https://macrobits.io/system/ajax.php', payload, header)
           if "SUCCESS" in data :
               earned = re.search(r"You received (.*) Bits!",data)[1]
               slow (f" ✅ {green}received from ptc {earned} Bits!{reset}      \n")
               _balance()

    except Exception as error:
           sys.stdout.write(f" 🔼 {error} \r")
           pass

def _main():
    while True:
          try:

             data = get('https://macrobits.io/claims.html', headers=headers)
             if 'You can claim again in' in data:
                 teller = re.search('''<span id="claimTime">
             (.*)
            </span>''', data)[1]
                 if 'minute' in teller:
                     mins = timer((int(re.search('''<span id="claimTime">
              (.*) minute''',data)[1])*60)+30)
                     continue
                 elif 'second' in teller:
                       secs = timer(int(re.search('''<span id="claimTime">
             (.*) second''', data)[1])+30)
                       continue

             solvekey  = "iUeTMJ.5ed9xNHEEuy84OGvH6r3fVVbb"

             try:
                capdata = captcha(captcha_type ,solvekey, api_key)
                cap = capdata[0]
                challenge = capdata[1]
                #sys.stdout.write(f" {cyan}captcha code ¶ {green}{cap}{reset}       \r")
                #sleep(2.5)

                x = datetime.datetime.now().strftime("%X")
                print (f"\033[32m[{x}] \033[31mcaptcha bypassing •", end="   \r")
                sleep(1)
                x = datetime.datetime.now().strftime("%X")
                print (f"\033[32m[{x}] \033[34mcaptcha bypassing • •", end="   \r")
                sleep(1)
                x = datetime.datetime.now().strftime("%X")
                print (f"\033[32m[{x}] \033[33mcaptcha bypassing • • •", end="   \r")
                sleep(1)
             except :
                   continue

             try:
                token = re.findall("var token = '(\w+)",data)[0]
             except:
                   if 'Just a moment...' in data:
                       print (f" {red}Expired Data Reason : [{reset}cloudflare detected{red}]{reset}")
                       os.system("rm -rf config/data.json")
                       print (cyan+"─".center(47, "─")+reset)
                       sys.exit()
                   else:
                       sleep(30)

             payload = {"a":"getFaucet","token":token,"captcha":"0","challenge":challenge,"response":cap}
             data    = post("https://macrobits.io/system/ajax.php", payload, headers)
             if "Congratulations, your lucky number was" in data:
                 roll = re.search('Congratulations, your lucky number was (.*)\!',data)[1]
                 slow (f" ✅ {green}number was {roll}{reset}\n")
                 upbal = _balance()
                 timer(5*60)
                 _ptc()
             else:
                 sys.stdout.write("                                    \r")

          except (ZeroDivisionError, IndexError):
                 pass
          except KeyboardInterrupt:
                 sys.exit()
          except Exception as error:
                 sys.stdout.write(f" 🔼 {error}          \r")
                 pass

if __name__ == "__main__":
   while True:
         _main()


#_completed_
