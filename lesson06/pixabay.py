from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

url = 'https://pixabay.com/zh/photos/?cat=nature'
html = requests.get(url, headers=headers)

sp = BeautifulSoup(html.text, 'html.parser')
print(sp)
