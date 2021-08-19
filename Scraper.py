from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Setup webdriver
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox()
#driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)



driver.get("https://zoopla.co.uk")

