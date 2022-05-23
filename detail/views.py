from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Board, Img
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests
import json
from search.models import Search
# from search.models import Search

def detail_list(request):
    images = Img.objects.all()
    # boards = Board.objects.get().order_by('id')
    # page = int(request.GET.get('p', 1))
    # paginator = Paginator(boards, 5) 
    # boards = paginator.get_page(page)

    # 카카오 --------------------------------------------
    # searching = '종로구 계동길 37'
    # url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+searching
    # headers = {"Authorization": "KakaoAK 2b6d2255a3c62ca88e47dc43bac4ee37"}
    # result = json.loads(str(requests.get(url,headers=headers).text))
    # match_first = result['documents'][0]['address']
    # y, x = float(match_first['y']),float(match_first['x'])

    return render(request, 'detail/detail.html')

    # return render(request, 'detail/detail.html', {'boards':boards ,'images' : images, 'y':y, 'x':x})



def detail(request):
    # img_crawl()
    # review_crawl()
    return redirect('./detail')


# 이미지 크롤링
def img_crawl():
    img = Img.objects.all()
    img.delete()
    link = Search.objects.get(title = '우도') # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    page = 1
    option = Options()
    option.add_argument('no-sandbox')
    option.add_argument('--headless')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome('./chromedriver', options=option) # Mac
    # browser = webdriver.Chrome('./chromedriver', options=option) # Window
    browser.get(link.url)

    while page < 7:
        try:
            img = Img()
            item = WebDriverWait(browser,2).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#lithium-root > main > div:nth-child(2) > div.daYrb.z > div:nth-child(2) > div > div > span > section:nth-child(3) > div > div > div > div.AVvza > span > div > div.kBjIf.f.e > div > div > div > div.eFKIy._T.w > div > div.wClCt.w > ul > li.bBdQR._A.bxQEm > div")))
            image = item.get_attribute('style').replace('background-image: url("', '').replace('");', '')
            img.address= image
            img.save()
        except:
            pass

        try:
            WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#lithium-root > main > div:nth-child(2) > div.daYrb.z > div:nth-child(2) > div > div > span > section:nth-child(3) > div > div > div > div.AVvza > span > div > div.kBjIf.f.e > div > div > div > div.eFKIy._T.w > div > div.fHNog.Z1._S.ezuqT > button'))).click()
        except:
            pass

        page += 1

# 댓글 크롤링
def review_crawl():
    board = Board.objects.all()
    board.delete()

    url = 'https://www.tripadvisor.co.kr'
    urlplus = '/Attraction_Review-g297885-d1776326-Reviews-Udo-Jeju_Jeju_Island.html'  
    page = 1

    option = Options()
    option.add_argument('no-sandbox')
    option.add_argument('--headless')
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    option.add_argument("disable-features=NetworkService")
    browser = webdriver.Chrome('./chromedriver', options=option) # Mac
    # browser = webdriver.Chrome('./chromedriver', options=option) # Window
    browser.get(url+urlplus)

    while page < 3:
        items = WebDriverWait(browser, 2).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.dHjBB > div')))
        for item in items:
            try:
                board = Board() 

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
        

