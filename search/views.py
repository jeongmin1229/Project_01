# 기본 설정 
# import selenium

import time
# from jmespath import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.shortcuts import render
from .models import Search

# webdriver 옵션 
# webdriver 옵션 
options = Options() 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
options.add_argument("headless") 
driver = webdriver.Chrome('./chromedriver.exe', options=options) # Window 
# driver = webdriver.Chrome('./chromedriver', options=options) # Mac

def home(request):
    search = ''
    if request.method == 'GET':
        search = request.GET.get('query')

    return render(request, 'search/home.html', {'search':search})

def key_word(request):
    Search.objects.all().delete()
    if request.method =='GET':
        question = request.GET.get('q')
        op = request.GET.get('select')
  
    #검색 시작점, url 이동
    url_path = "https://www.tripadvisor.co.kr/Attractions"
    driver.get(url_path) # url로 이동

    # 검색어 창에 검색하기 
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(question) # ()안의 값을 현재 커서가 위치한 곳에 넣음 
    search_box.send_keys(Keys.RETURN)  #Enter키를 누르게 함 
    
    time.sleep(1)


    # 카테고리 검색
    if op == "전체":
        driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[4]/a').click()
    elif op == "호텔":
        driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[2]/a').click()
    elif op == "음식점":
        driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[3]/a').click()
    elif op == "즐길거리":
        driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[4]/a').click()
   
    
    # 활성화된 url을 search_url로 지정 
    present_url = driver.current_url
    driver.get(present_url)
    
    time.sleep(3)


    # title, url 가져오기 
    data_raw = driver.find_elements_by_class_name("result-title")
    url_list= []
    title_list=[]

    for data in data_raw:

        # title
        title = (data.text)

        # url
        detail_url = data.get_attribute('onclick')
        url1 = detail_url.split('/')[1]
        url2 = url1.split('html')[0]
        url = "https://www.tripadvisor.co.kr/" + url2 +"html"
        title_list.append(title)
        url_list.append(url)

    # adddress
    address_raw = driver.find_elements_by_class_name("address-text")
    address_list=[]

    for address1 in address_raw:
        address2 = (address1.text)
        address3 = address2.split(',')[0]
        address_list.append(address3)


    # review count 
    review_raw = driver.find_elements_by_class_name("review_count")
    review_list=[]
    
    for review in review_raw:
        review_count = (review.text)
        review_list.append(review_count)
        

    # image 

    image_raw = driver.find_elements_by_css_selector(".aspect.is-shown-at-mobile.is-hidden-tablet > .inner")
    image_list=[]

    for image1 in image_raw:
        image2 = image1.get_attribute('style')
        image3 = image2.split('"')[1]
        image4 = image3.split('"')[0]
        image_list.append(image4)


    # rating

    rating_raw = driver.find_elements_by_css_selector(".rating-review-count > div > span")
    rating_list=[]

    for rating in rating_raw:
        rating1 = rating.get_attribute('alt')
        rating2 = rating1.split('중')[1]
        rating_list.append(rating2)


    # DB에 추가 
    
    time.sleep(1)

    aa = 0
    while aa < 6:
        u = Search(address = address_list[aa], title = title_list[aa], url = url_list[aa], image = image_list[aa], review_count=review_list[aa], rating=rating_list[aa])
        u.save()
        aa += 1

    context = {
        "address1" : address_list[0],
        "title1" : title_list[0], 
        "url1" : url_list[0], 
        "image1" : image_list[0],
        "rating1" : rating_list[0],
        "review1" : review_list[0],

        "address2" : address_list[1],
        "title2" : title_list[1], 
        "url2" : url_list[1], 
        "image2" : image_list[1],
        "rating2" : rating_list[1],
        "review2" : review_list[1],

        "address3" : address_list[2],
        "title3" : title_list[2], 
        "url3" : url_list[2], 
        "image3" : image_list[2],
        "rating3" : rating_list[2],
        "review3" : review_list[2],

        "address4" : address_list[3],
        "title4" : title_list[3], 
        "url4" : url_list[3], 
        "image4" : image_list[3],
        "rating4" : rating_list[3],
        "review4" : review_list[3],

        "address5" : address_list[4],
        "title5" : title_list[4], 
        "url5" : url_list[4], 
        "image5" : image_list[4],
        "rating5" : rating_list[4],
        "review5" : review_list[4],

        "address6" : address_list[5],
        "title6" : title_list[5], 
        "url6" : url_list[5], 
        "image6" : image_list[5],
        "rating6" : rating_list[5],
        "review6" : review_list[5],

        "question" : question,
        "op": op}
        
    return render(request, 'search/search.html', context)