import requests
from user_agent import generate_user_agent
from random import randrange,choice
from threading import Thread
import sys
n=0
def users():
    global n
    while True:
        try:
            pp=''.join(choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(18))
            cookies = {

    'sessionid': '2270948198%3AmXXLO6dQKKJIDm%3A3%3AAYcytR1itrs2KAJ8PQa3fyQA'+pp,
}
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/direct/inbox/',
    'user-agent': generate_user_agent(),
}
            data = {
    'variables': '{"id":"'+str(randrange(1,30975110))+'","render_surface":"PROFILE"}',
    'doc_id': '7663723823674585',
}
            response = requests.post('https://www.instagram.com/graphql/query', cookies=cookies, headers=headers, data=data).json()
            username=response['data']['user']['username']
            n+=1
            sys.stdout.write(f'''\r\x1b[38;5;208m|| --» : {username} / {n}      @Qredes\r''')
            with open('username.txt', 'a') as f:
                f.write(username+'\n')
        except:''




for _ in range(100):
    Thread(target=users).start()
