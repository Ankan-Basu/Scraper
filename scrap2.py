from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.action_chains import ActionChains
import time

from bs4 import BeautifulSoup

print('Import finished')
driver = uc.Chrome()
driver.get('https://google.com/travel') 
search_box = driver.find_element(By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')

actions = ActionChains(driver)
actions.send_keys_to_element(search_box, 'Darjeeling')
actions.send_keys_to_element(search_box, Keys.ENTER)
# actions.scroll()

actions.perform()
time.sleep(1)

driver.execute_script('window.scrollTo(0, document.querySelector(\'.kQb6Eb\').scrollHeight);')

top_sights = driver.find_elements(By.XPATH, '//div[@class="NnEw9 OBk50c T1Yjbc"]')
#NnEw9 OBk50c T1Yjbc
# Ld2paf
#R1Ybne pzJ1lf  img
#skFvHc YmWhbc place name
#nFoFM desc

# with open('res.html', 'w') as file:
#   for elem in x:
#     file.write(elem.get_attribute('innerHTML'))

# driver.quit()
results = []
for sight in top_sights:
  # place_img_tmp = sight.find_element(By.XPATH, './/*[@class="kXlUEb"]')
  # print(place_img_tmp.get_attribute('innerHTML'))

  place_img = sight.find_element(By.CLASS_NAME, 'R1Ybne').get_attribute('src')
  # print(img.get_attribute('src'))

  place_name = sight.find_element(By.XPATH, './/div[@class="skFvHc YmWhbc"]').text
  place_desc = sight.find_element(By.XPATH, './/div[@class="nFoFM"]').text
  place = place_img, place_name, place_desc
  results.append(place)

# time.sleep(60)

# print(res)

with open('res.txt', 'w') as file:
  for result in results:
    file.write(f'Place: {result[1]}' + '\n')
    file.write(f'Desc: {result[2]}' +'\n')
    file.write(f'Img: {result[0]}' + '\n')
    file.write('\n')