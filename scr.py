import random
import requests
from bs4 import BeautifulSoup
import string
import os
import shutil

def imgValidate():
    for i in range(6):
        url+=random.choice(string.ascii_lowercase)
    content = requests.get(url, headers = headers).text
    soup = BeautifulSoup(content, 'html.parser')
    imgUrl = soup.find_all("img")[0].get('src')
    if imgUrl in WrongUrl:
        return imgValidate(WrongUrl);
    else:
        return imgUrl, url;

url = 'https://prnt.sc/'
WrongUrl = [
    '//st.prntscr.com/2019/11/26/0154/img/0_173a7b_211be8ff.png'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
imgUrl, url = imgValidate()
imgExt = imgUrl.split('.')[-1]

response = requests.get(imgUrl, stream=True)
with open(os.getcwd()+'\\temp\\'+url[-6:]+'.'+imgExt, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response