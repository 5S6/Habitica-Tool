import requests 
import threading
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init
import json

init()

print(Fore.RED + """
  ___ ___       ___.   .__  __  .__                ___________           .__   
 /   |   \_____ \_ |__ |__|/  |_|__| ____ _____    \__    ___/___   ____ |  |  
/    ~    \__  \ | __ \|  \   __\  |/ ___\\__  \     |    | /  _ \ /  _ \|  |  
\    Y    // __ \| \_\ \  ||  | |  \  \___ / __ \_   |    |(  <_> |  <_> )  |__
 \___|_  /(____  /___  /__||__| |__|\___  >____  /   |____| \____/ \____/|____/
       \/      \/    \/                 \/     \/                              
       """)


print(Fore.GREEN+'''
[1] - Coin/XP/Level Farmer
[2] - Mass Buy Armored Warrior
[3] - Mass Birthday Card Send
[4] - Mass Congratulations Card Send
[5] - Mass Good Luck Card Send
[6] - Tavern Spam(Horrible RateLimit)''')

with open('config.json') as f:
    config = json.load(f)




url1 = config.get('url1')
url2 = config.get('url2')
url3 = config.get('url3')
url4 = config.get('url4')
url5 = config.get('url5')
url6 = config.get('url6')
url = config.get('url')

def coins():
  headers = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user': config.get('x-api-user')
  }
  

 
  

  a = requests.post(url, headers = headers)
  b = requests.post(url1, headers = headers)
  c = requests.post(url2, headers=headers)
  d = requests.post(url3, headers= headers)
  e = requests.post(url4, headers = headers)
  f = requests.post(url5, headers= headers)
  g = requests.post(url6, headers= headers)

  print(a.text)
  print(b.text)
  print(c.text)
  print(d.text)
  print(e.text)
  print(f.text)
  print(g.text)
  threads=[]

  for i in range(100):
   t = threading.Thread(target = coins)
   t.Daemon = True
   threads.append(t)

  for i in range(100):
   threads[i].start()
   time.sleep(1.5)

  for i in range(100):
   threads[i].join()


  time.sleep(15)

  for i in range(100):
   t = threading.Thread(target = coins)
   t.Daemon = True
   threads.append(t)

  for i in range(100):
   threads[i].start()
   time.sleep(1.5)

  for i in range(100):
   threads[i].join()


def massbuy():
  headers1 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
  }
  i = 2 
  i = i + 1


  buy = requests.post("https://habitica.com/api/v4/user/buy/head_warrior_6" + str(i), headers=headers1)
  print(buy.text)
  threads=[]

  for i in range(100):
   t = threading.Thread(target = massbuy)
   t.Daemon = True
   threads.append(t)

  for i in range(100):
   threads[i].start()
   time.sleep(1.5)

  for i in range(100):
   threads[i].join()


  time.sleep(15)

  for i in range(100):
   t = threading.Thread(target = massbuy)
   t.Daemon = True
   threads.append(t)

  for i in range(100):
   threads[i].start()
   time.sleep(1.5)

  for i in range(100):
   threads[i].join()



def MassBirthdayCardSend():
 headers2 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
  }
  
 id = config.get('MassBirthdayCardSendID')
 send = requests.post('https://habitica.com/api/v4/user/class/cast/birthday?targetId='+id, headers=headers2)
 print(send.text)
 threads=[]

 for i in range(100):
   t = threading.Thread(target = MassBirthdayCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()


 time.sleep(15)

 for i in range(100):
   t = threading.Thread(target = MassBirthdayCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()


def MassCongratulationsCardSend():
 headers2 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
  }

 id1 = config.get('MassCongratulationsCardSendID')
 send1 = requests.post('https://habitica.com/api/v4/user/class/cast/congrats?targetId='+id1, headers=headers2)
 print(send1.text)
 threads=[]

 for i in range(100):
   t = threading.Thread(target = MassCongratulationsCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()


 time.sleep(15)

 for i in range(100):
   t = threading.Thread(target = MassCongratulationsCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()





def MassGoodLuckCardSend():
 
 headers2 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
  }
  

 id2 = config.get('MassGoodLuckCardSend')
 send2 = requests.post('https://habitica.com/api/v4/user/class/cast/birthday?targetId='+id2, headers=headers2)
 print(send2.text)
 threads=[]

 for i in range(100):
   t = threading.Thread(target = MassGoodLuckCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()


 time.sleep(15)

 for i in range(100):
   t = threading.Thread(target = MassGoodLuckCardSend)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()




def MessageSpam():
 
 headers5 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
  }


 tomessageid =  str(input("\nInput User's ID: "))
 messagecontent =  str(input("\nWhats The Message You Want To Spam?: "))

 
 
 payload = {
 'message': messagecontent,
 'toUserId': tomessageid
  }

 spam = requests.post('https://habitica.com/api/v4/members/send-private-message',headers=headers5,data=payload)
 print(spam.text)
 threads=[]

 for i in range(100):
   t = threading.Thread(target = MessageSpam)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()


 time.sleep(15)

 for i in range(100):
   t = threading.Thread(target = MessageSpam)
   t.Daemon = True
   threads.append(t)

 for i in range(100):
   threads[i].start()
   time.sleep(1.5)

 for i in range(100):
   threads[i].join()



def TavernSpam():
    
 headers1 = {
    'x-api-key': config.get('x-api-key'),
    'x-api-user':config.get('x-api-user')
    }
 tavernurl = 'https://habitica.com/api/v4/groups/00000000-0000-4000-A000-000000000000/chat'
 
 payload = {
    'message': "AlekDevs On Top!"
 }

 tspam = requests.post(tavernurl, headers=headers1, data=payload)
 print(tspam.text)
 threads=[]

 for i in range(20):
   t = threading.Thread(target = TavernSpam)
   t.Daemon = True
   threads.append(t)

 for i in range(20):
   threads[i].start()
   time.sleep(1.5)

 for i in range(20):
   threads[i].join()


 time.sleep(15)

 for i in range(20):
   t = threading.Thread(target = TavernSpam)
   t.Daemon = True
   threads.append(t)

 for i in range(20):
   threads[i].start()
   time.sleep(1.5)

 for i in range(20):
   threads[i].join()



option = int(input("\nWhich Tool Would You Like To Use: "))

if option == 1:
    coins()

if option == 2:
    massbuy()

if option == 3:
    MassBirthdayCardSend()

if option == 4:
    MassCongratulationsCardSend()

if option == 5:
    MassGoodLuckCardSend()

if option == 6:
    TavernSpam()
