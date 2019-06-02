
import requests
from bs4 import BeautifulSoup

res=requests.get("https://pypi.org/project/requests/")

soup=BeautifulSoup(res.content,'html.parser')

text_class=soup.find_all('a')
for u in text_class:
    print(u['href'])
