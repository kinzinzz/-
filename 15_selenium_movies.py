import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
 
url = "https://play.google.com/store/movies?hl=ko&gl=kr"
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept-Language":"ko-KR,ko"
# }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"j2FCNc"})

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
browser = webdriver.Chrome()
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
interval = 2

# 현재 문서 높이을 가져와서 저장
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

soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"})
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    
    if original_price:
        price = movie.find("span", attrs={"class":"VfPpfd VixbEe"})
        print(title.text, "할인전 금액: ", original_price.text, "할인금액:", price.text)