# 기본 설정 
# import selenium
from tkinter import BROWSE
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup as bs



# webdriver 옵션 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# 검색 시작점, url 이동
url_path = "https://www.tripadvisor.co.kr/Attractions"
driver.get(url_path) # url로 이동

# 검색어 창에 검색하기 
search_box = driver.find_element_by_name("q")

search_box.send_keys("전주") # ()안의 값을 현재 커서가 위치한 곳에 넣음 
search_box.send_keys(Keys.RETURN)  #Enter키를 누르게 함 
driver.maximize_window() # 화면 최대화
time.sleep(1)


# 카테고리 검색

# # 호텔 
# driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[2]/a').click()
# # 음식점
# driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[3]/a').click()
# 즐길거리 
driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[4]/a').click()
# # 도시 및 지역 
# driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[5]/a').click()

# 활성화된 url을 search_url로 지정 
present_url = driver.current_url
driver.get(present_url)

# adddress
count_address = 1
time.sleep(2)

address_raw = driver.find_elements_by_class_name("address-text")
address_list=[]

for address in address_raw:
    if count_address < 6:
        address_list.append(address.text)
        count_address+=1
    else:
        break

        
# title, address 가져오기 
count_data = 1
time.sleep(2)

data_raw = driver.find_elements_by_class_name("result-title")
url_list= []
title_list=[]

for data in data_raw:
    if count_data < 6:

        #title
        title = (data.text)

        #url
        detail_url = data.get_attribute('onclick')
        url1 = detail_url.split('/')[1]
        url2 = url1.split('html')[0]
        url = "https://www.tripadvisor.co.kr/" + url2 +"html"

        title_list.append(title)
        url_list.append(url)

        count_data+=1
    else:
        break
        
# adddress
# count_image=1

time.sleep(2)
count_image = 1

image_raw = driver.find_elements_by_css_selector(".aspect.is-shown-at-mobile.is-hidden-tablet > .inner")
image_list=[]

for image1 in image_raw:
    if count_image < 6:
        image2 = image1.get_attribute('style')
        image3 = image2.split('"')[1]
        image4 = image3.split('"')[0]
        count_image +=1
        image_list.append(image4)
    else:
        break

 
print(title_list)
print(url_list)
print(address_list)
print(image_list)


    

    
