import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import time
from lxml import html

Libros= []
versiculos=[]
texto=[]

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
url  = "https://www.bible.com/es/bible/146/GEN."
print('scraping')
print(url)  
for page in range(1,3):
    html = requests.get(url+str(page)+".RVC", headers=headers)
    soup = bs(html.content, "html.parser")
    for i in soup.find_all("span", attrs={"class":"ChapterContent_content__dkdqo"}):
        texto.append(i.text.strip())
        # exit()
texto = list(filter(lambda item: item != "", texto))
print(texto)