from bs4 import BeautifulSoup as bs
import requests
import re
from urllib.parse import unquote

proxies = {"http": "johannesmaigray@gmail.com:Johs16031603@au473.nordvpn.com",}
           # "https": "http://145.253.118.157:37100"}
#
res = requests.get("https://www.wohnpreis.de/",proxies=proxies)

res = bs(res.text,'html.parser')
print(res)