from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

url = "https://play.google.com/store/movies?hl=ko&gl=kr"
browser = webdriver.Chrome(options=options)
browser.get(url)
interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")
    
    if current_height == prev_height:
        break
    
    prev_height = current_height
    
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"})
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    
    if original_price:
        price = movie.find("span", attrs={"class":"VfPpfd VixbEe"})
        print(title.text, "할인전 금액: ", original_price.text, "할인금액:", price.text)