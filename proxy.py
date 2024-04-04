import urllib
import urllib.request
import urllib.error
import ua_generator


def is_bad_proxy(pip: str) -> bool:
    print(f"Checking if {pip} is a viable proxy... ", end='') 
    #try:
    proxy_handler = urllib.request.ProxyHandler({pip.split(':')[0]: pip})
    ua = ua_generator.generate()
    
    try:
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            
        urllib.request.install_opener(opener)

        sock=urllib.request.urlopen('https://www.google.com')
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print(f"It is not! details: {detail}")
        return True
    
    print("It is!")
    return False

def validate_proxy_list(list: list) -> list:
    valid = []
    for proxy in list:
        if is_bad_proxy(proxy):
            continue
        else:
            valid.append(proxy)
    return valid

def read_proxy_file(path: str):
    with open(path, 'r+') as f:
        contents = f.read()
        split = contents.split('\n')
        trimmed = [proxy.strip() for proxy in split if proxy != '']
        return trimmed