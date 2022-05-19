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
import re
# from urllib.request import uropen

# 옵션
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)



#웹 드라이버 생성 
# driver = webdriver.Chrome('./chromedriver.exe')

# driver.get(url_path) 


url_path = "https://www.tripadvisor.co.kr/Attractions"

# url로 이동
driver.get(url_path) # url로 이동

# driver.implicitly_wait(5) # wait time
# driver.maximize_window() # 화면 최대화

# 검색어 창 찾기 
search_box = driver.find_element_by_name("q")

# ()안의 값을 현재 커서가 위치한 곳에 넣음 
search_box.send_keys("전주")

#Enter키를 누르게 함 
search_box.send_keys(Keys.RETURN) 

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


search_list = driver.find_elements_by_css_selector("div.lsnx")


# 활성화된 url을 search_url로 지정 
present_url = driver.current_url
driver.get(present_url)


# 제목 가져오기 
count = 1
time.sleep(2)
titles_raw = driver.find_elements_by_class_name("result-title")
for title in titles_raw:
    if count < 3:
        print(title.get_attribute('onclick'))
        print(title.text)
        print()
        count+=1
    else:
        break
