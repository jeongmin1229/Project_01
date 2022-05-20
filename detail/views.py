from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Board
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import requests
import json
# from search.models import Search

def board_list(request):
    caps = DesiredCapabilities().CHROME 
    caps["pageLoadStrategy"] = "none"

    images = []
    # images = img_crawl()
    # review_crawl()

    boards = Board.objects.all().order_by('id')
    # page = int(request.GET.get('p', 1))
    # paginator = Paginator(board, 5) 

    # boards = paginator.get_page(page)

    # 카카오 --------------------------------------------
    searching = '종로구 계동길 37'
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+searching
    headers = {"Authorization": "KakaoAK 2b6d2255a3c62ca88e47dc43bac4ee37"}
    result = json.loads(str(requests.get(url,headers=headers).text))
 
    match_first = result['documents'][0]['address']
    
    y, x = float(match_first['y']),float(match_first['x'])


    return render(request, 'detail/detail.html', {'boards':boards, 'y':y, 'x':x})
    # return render(request, 'detail/detail_list.html', {'boards':boards ,'images' : images, 'y':y, 'x':x})


# 이미지 크롤링
def img_crawl():
    images = []
    url = 'https://www.tripadvisor.co.kr'
    urlplus = '/Attraction_Review-g297885-d1776326-Reviews-Udo-Jeju_Jeju_Island.html'   
    page = 1
    option = Options()
    option.add_argument('no-sandbox')
    option.add_argument('--headless')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome('./chromedriver', options=option)
    browser.get(url+urlplus)

    while page < 5:
        item = WebDriverWait(browser,2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#lithium-root > main > div:nth-child(2) > div.daYrb.z > div:nth-child(2) > div > div > span > section:nth-child(3) > div > div > div > div.AVvza > span > div > div.kBjIf.f.e > div > div > div > div.eFKIy._T.w > div > div.wClCt.w > ul > li.bBdQR._A.bxQEm > div")))
        images.append(item.get_attribute('style').replace('background-image: url("', '').replace('");', '')) 

        try:
            WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#lithium-root > main > div:nth-child(2) > div.daYrb.z > div:nth-child(2) > div > div > span > section:nth-child(3) > div > div > div > div.AVvza > span > div > div.kBjIf.f.e > div > div > div > div.eFKIy._T.w > div > div.fHNog.Z1._S.ezuqT > button'))).click()
        except:
            pass

        page += 1
    return images

# 댓글 크롤링
def review_crawl():
    url = 'https://www.tripadvisor.co.kr'
    urlplus = '/Attraction_Review-g297885-d1776326-Reviews-Udo-Jeju_Jeju_Island.html'  
    page = 1

    option = Options()
    option.add_argument('no-sandbox')
    option.add_argument('--headless')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    option.add_argument("disable-features=NetworkService")
    browser = webdriver.Chrome('./chromedriver', options=option)
    browser.get(url+urlplus)

    while page < 3:
        items = WebDriverWait(browser, 2).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.dHjBB > div')))
        # items = browser.find_elements_by_css_selector('div[class^=dHjBB] > div')
        for item in items:
            try:
                board = Board() 
                # destination = Search.objects.get(text='우도')
                # board.destination = destination

                scope  = item.find_element_by_css_selector('#tab-data-qa-reviews-0 > div > div.dHjBB > div > span > div > div:nth-child(2) > svg')
                scope = scope.get_attribute('aria-label').replace('풍선 5개 중 ', '')
                board.scope = scope

                date = item.find_element_by_css_selector('#tab-data-qa-reviews-0 > div > div.dHjBB > div > span > div > div.eRduX').text
                board.register_dttm = date

                title = item.find_element_by_css_selector('span[class^=NejBf]').text
                board.title = title

                content = item.find_element_by_css_selector('#tab-data-qa-reviews-0 > div > div.dHjBB > div > span > div > div.duhwe._T.bOlcm > div.pIRBV._T.KRIav > div > span').text
                board.contents = content
                
                board.save()
                
            except:
                pass
                
        page += 1
        try:
            WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#tab-data-qa-reviews-0 > div > div.dHjBB > div:nth-child(11) > div:nth-child(2) > div > div.cpUAm.j > div.cCnaz > div > a'))).click()
        except:
            pass
        

def address_crawl():
    url = 'https://www.tripadvisor.co.kr/Search?q=%EC%9A%B0%EB%8F%84&searchSessionId=A0F0FD1A8D5ECFEA45AF9B0EE38B6A0C1652765218741ssid&searchNearby=false&sid=580F955EC7BF48D08CE4E4A5C39561DF1652765224651&blockRedirect=true&rf=2'
    
    option = Options()
    option.add_argument('no-sandbox')
    option.add_argument('--headless')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome('./chromedriver', options=option)
   
    browser.get(url)

    for i in range(1, 5):
        time.sleep(2)
        item  = browser.find_element_by_css_selector('#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div:nth-child(2) > div > div > div:nth-child({})'.format(i))
        page = item.find_element_by_css_selector('div[class^=result-title]')
        print(page.get_attribute('onclick'))

        titles = item.find_element_by_css_selector('div[class^=result-title]').text
        print(titles)

        address =item.find_element_by_css_selector('div[class^=address-text]').text
        print(address)
        print()