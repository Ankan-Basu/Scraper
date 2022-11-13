from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.action_chains import ActionChains
import time

from bs4 import BeautifulSoup


driver = uc.Chrome()
driver.get('https://google.com/travel') 
search_box = driver.find_element(By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')

# time.sleep(2)
# driver.execute_script("document.querySelector('.II2One').value='Sikkim';")
# # driver.execute_script("document.querySelector('.II2One').click()';")
# time.sleep(2)

actions = ActionChains(driver)
actions.send_keys_to_element(search_box, 'Sikkim')
# time.sleep(2)
actions.send_keys_to_element(search_box, Keys.ENTER)

actions.perform()
time.sleep(5)

