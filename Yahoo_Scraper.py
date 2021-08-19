from typing import Pattern
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup

url_stats = 'https://finance.yahoo.com/quote/{}/key.statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financial = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'APPL'

# response = requests.get('https://finance.yahoo.com/quote/F/financials?p=F')
# print(url_financial.format(stock, stock))
url = 'https://finance.yahoo.com/quote/{}'.format(stock)
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text
change = soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
market_cap = soup.find('td', {'data-test':'MARKET_CAP-value'}).find_all('span')[0].text
year_average = soup.find('td', {'data-test':'FIFTY_TWO_WK_RANGE-value'}).text

print(price, change)
print(market_cap, year_average)

# soup = BeautifulSoup(response.text, 'html.parser')
# pattern = re.compile(r'\s--\sData\s--\s')
# script_data = soup.find('script', text=pattern).contents[0]
# script_data[:500]
# # def load_and_accept_cookies(URL):
#     print("Start")    
    
#     options = Options()
#     options.add_argument('--headless')
#     #driver = webdriver.Firefox(options=options)
#     driver.get(URL)
#     #driver.implicitly_wait(10)
#     print("Hello World 1")
#     accept_cookies = driver.find_element_by_id("Lead-4-QuoteHeader-Proxy")
#     print("hello world 2")
#     print(accept_cookies)
#     for button in accept_cookies: 
#         if button.text == "agree":
#             relevant_button = button

#     relevant_button.click()
#     return driver
    
# driver = webdriver.Firefox()

# load_and_accept_cookies("https://finance.yahoo.com/quote/AAP/news?p=AAP")

#Setup webdriver
# options = Options()
# options.add_argument('--headless')

# driver.implicitly_wait(10)
# driver.get("https://finance.yahoo.com/quote/AAP/news?p=AAP")

#url = 'https://finance.yahoo.com/quote/TSLA/news?p=TSLA'
# response = requests.get(url)
# url_response = response.status_code
# print(url_response)

# url = 'https://news.yahoo.com/dems-head-toward-house-control-160107166.html'
# response = requests.get(url)
# url_response = response.status_code
# print(url_response)