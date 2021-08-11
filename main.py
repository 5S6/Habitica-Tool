import requests 
import threading
import time

print('[1] - Coin Farmer')
print('[2] - Mass Buy Armored Warrior')
print('[3] - Mass Birthday Card Send')
print('[4] - Mass Congratulations Card Send')
print('[5] - Mass Good Luck Card Send')
print('[6] - Message Spam')






url1 = 'https://habitica.com/api/v4/tasks/600ca03f-4d7a-4ffe-a551-61643017f482/score/up'
url2 = 'https://habitica.com/api/v4/tasks/dd67464b-220f-48b6-8fe5-45de7fef884f/score/up'
url3 = 'https://habitica.com/api/v4/tasks/3d47f2e0-3075-4e72-92a5-9c7e01ca4266/score/up'
url4 = 'https://habitica.com/api/v4/tasks/d33b72b0-64ea-48fd-a56a-7590f7e0d28e/score/up'
url5 = 'https://habitica.com/api/v4/tasks/11c07912-95a7-4bf7-ace2-0bce1dc0ba52/score/up'
url6 = 'https://habitica.com/api/v4/tasks/89abe65b-438d-452a-bd85-2f6ee38bb30b/score/up'
url = 'https://habitica.com/api/v4/tasks/205bd31a-d40d-4d88-b19b-71d87cf7a1c9/score/up'

def coins():
  headers = {
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
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
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
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
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
  }
  
 id = str(input("\nInput User ID: "))
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
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
  }

 id1 = str(input("\nInput User ID: "))
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
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
  }
  

 id2 = str(input("\nInput User ID: "))
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
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
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



def MessageSpam():
  headers1 = {
    'x-api-key': 'e705e8df-42e0-44da-b005-931a601e2ff8',
    'x-api-user':'6f60b8b0-822f-4bc7-a664-c3c8ed13f679'
  }


tavernul = 'https://habitica.com/api/v4/groups/00000000-0000-4000-A000-000000000000/chat'
payload3 = {
    'message': "hey!"
}

tspam = requests.post(tavernul, headers=header1,data = payload3 )




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







