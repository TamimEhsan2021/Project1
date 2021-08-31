from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
print("Start")
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

driver.get("https://finance.yahoo.com/quote/F")
print("Page loaded")

try:
    print("I am here")
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div/form/div[2]/div[2]/button'))).click()
    #accept_cookies = driver.find_element(By.CLASS_NAME, 'btn primary').click()
    print("button exists")
except NoSuchElementException:
    print("Button is not there")

price = driver.find_element_by_class_name("D(ib) Fz(20px) Fw(b)")
print(price)



def search(ticker):
    searchEl = driver.find_element_by_id('yfin-usr-qry')
    searchEl.send_keys(ticker)


#search('TSLA')