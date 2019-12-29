import random
import requests
from bs4 import BeautifulSoup
import string
import os
import shutil

html = '<html><head><title>The Dormouses story</title></head><body><p class="title"><b>The Dormouses story</b></p><p class="story">Once upon a time there were three little sisters; and their names were<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;nd they lived at the bottom of a well.</p><p class="story">...</p>'
#For testing purposes, piece of html

url = 'https://prnt.sc/qabada'
WrongUrl = [
	'st.prntscr.com/2019/11/26/0154/img/0_173a7b_211be8ff.png'
	]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
content = requests.get(url, headers = headers).text
soup = BeautifulSoup(content, 'html.parser')

imgUrl = soup.find_all("img")[0].get('src')
imgExt = imgUrl.split('.')[-1]


response = requests.get(imgUrl, stream=True)
with open(os.getcwd()+'\\temp\\'+url[-6:]+'.'+imgExt, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response