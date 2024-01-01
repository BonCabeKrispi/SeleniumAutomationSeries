from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.support.ui import Select
import time


# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# url
url= "https://www.tasbih.org/"

# Options screen env
chrome_options = Options()

# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("excludeSwitches",["eneble-automation"])
chrome_options.headless = False
driver = webdriver.Chrome(service=s, options=chrome_options)


# Get the response and start automate
print("Process started: Automate!")
driver.get(url)

# case for increment button 
for c in range (0,10): 
	c=driver.find_element(By.ID, "incrementor")
	time.sleep(0.3)
	c.click()


# case for reset button
time.sleep(0.5)
driver.find_element(By.ID, "resetter").click()
alert = Alert(driver) 
time.sleep(0.3)

# get alert text 
print(alert.text) 
  
# accept the alert 
time.sleep(0.3)
alert.accept() 


# for dropdown value
grbf = driver.find_element(By.XPATH, '//*[@id="steps"]')
grbf.click()
time.sleep(0.2)
select = Select(grbf)


# select.select_by_value('100')
seratus = driver.find_element(By.CSS_SELECTOR, 'option[value="100"]')
seratus.click()

# case after dropdown value 100, increment number per 100
for c in range (0,10): 
	c=driver.find_element(By.ID, "incrementor")
	time.sleep(0.3)
	c.click()


# case for decrementor
for c in range (0,15): 
	c=driver.find_element(By.ID, "decrementor")
	time.sleep(0.3)
	c.click()


# delay before close
time.sleep(6)
driver.close()

print("Process done!")