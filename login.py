import requests
import time

payload = {
    'password': "YourPass",
    'username': "YourEmail"
}

login = requests.post('https://habitica.com/api/v4/user/auth/local/login', data=payload)
print(login.text)

time.sleep(100)
