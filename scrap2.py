from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options


def start_browser():
  chrome_options = Options()
  chrome_options.add_argument("--disable-extensions")
  chrome_options.add_argument("--disable-gpu")
  chrome_options.add_argument("--no-sandbox") # linux only
  # chrome_options.add_argument("--headless")
  driver = uc.Chrome(options=chrome_options)
  driver.get('https://google.com/travel') 
  driver.implicitly_wait(10)
  return driver 


def get_top_places(driver, destination):
  search_box = driver.find_element(By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')

  actions = ActionChains(driver)
  actions.send_keys_to_element(search_box, destination)
  actions.send_keys_to_element(search_box, Keys.ENTER)
  # actions.scroll()

  actions.perform()
  time.sleep(1)
  # driver.implicitly_wait(10)


  driver.execute_script('window.scrollTo(0, document.querySelector(\'.kQb6Eb\').scrollHeight);')

  top_sights = driver.find_elements(By.XPATH, '//div[@class="NnEw9 OBk50c T1Yjbc"]')

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


  with open('res.txt', 'w') as file:
    for result in results:
      file.write(f'Place: {result[1]}' + '\n')
      file.write(f'Desc: {result[2]}' +'\n')
      file.write(f'Img: {result[0]}' + '\n')
      file.write('\n')

# G5cKqf
# PH4Kgc QwCDkd
def get_hotels(driver):
  # side_bar = driver.find_element(By.XPATH, '//div[@class="G5cKqf"]')
  nav_links = driver.find_elements(By.XPATH, '//button[@class="VfPpkd-LgbsSe ksBjEc jcukd OXZ8S"]')
  # print(nav_links)

  #P4z3kc KgqTrc a tag
  #VfPpkd-LgbsSe ksBjEc jcukd OXZ8S button
  with open('sample3.html', 'w') as file:
    for link in nav_links:
      # print(link.get_attribute('href'))
      file.write(link.get_attribute('innerHTML'))

  actions = ActionChains(driver)
  actions.click(nav_links[4])
  actions.perform()
  time.sleep(5)
  # driver.implicitly_wait(10)


  #div class="iQJyJ oJeWuf" hotels
  hotels_div = driver.find_elements(By.XPATH, '//div[@class="iQJyJ oJeWuf"]')[3]

  hotel_names = hotels_div.find_elements(By.XPATH, './/h2[@class="BgYkof ogfYpf ykx2he"]')

  hotel_features = hotels_div.find_elements(By.CLASS_NAME, 'HlxIlc')
 
  hotel_prices = hotels_div.find_elements(By.XPATH, './/a[@class="OxGZuc W8vlAc lRagtb"]')


  results = []
  arr_len = len(hotel_names)

  for i in range(arr_len):
    result = {
      'hotelName': hotel_names[i].text, 
      'hotelFeatures': hotel_features[i].text, 
      'hotelPrice': hotel_prices[i].text
      }
    results.append(result)
    
    # print(result)

  for result in results:
    print(result, end='\n')
    print('\n')

  ###printing fxn
  # with open('hotels.txt', 'w') as file:
  #   for result in results:
  #     file.write('Hotel Name: ' + result['hotelName'] + '\n')
  #     file.write('Features:' + '\n'  + result['hotelFeatures'] + '\n')
  #     file.write('Price: ' + result['hotelPrice'] + '\n')
  #     file.write('\n')





if __name__ == '__main__':
  destination = input('Enter destination: ')
  driver = start_browser()
  # destination = 'Sikkim'
  get_top_places(driver, destination)

  print('Bruh i wish this was faster')
  get_hotels(driver)
  driver.quit()



#div class="VfPpkd-Jh9lGc" hotel