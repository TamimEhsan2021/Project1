from typing import Pattern
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup


stock = 'NVDA'
url ='https://www.google.com/finance/quote/NVDA:NASDAQ'
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('div', {'class':'rPF6Lc'}).find_all('div')[0].text
articles = soup.find_all('div', {'class':'yY3Lee'})[1].find_all('div')[1].text
article_numbers = len(soup.find_all('div', {'class':'yY3Lee'}))

print(price)

#print(price, articles)