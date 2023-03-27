import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
print('실행중')

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[1].find("div", attrs={"class":"name"}).get_text())

for item in items:
    # 광고 제품 제외
    ad_bedge = item.find("span", attrs={"class":"ad_bedge-text"})
    if ad_bedge:
        print("광고 제품은 제외합니다.")
        print()
        continue
        
    name = item.find("div", attrs={"class":"name"}).get_text()
    # 레노버 제품 제외
    if "레노버" in name:
        print(" 레노버 제품은 제외합니다.")
        print()
        continue
        
    price = item.find("strong", attrs={"class":"price-value"})
    if price:
        price = price.get_text()
    else:
        price = "가격정보 없음"
    
    # 리뷰 100개 이상, 평정 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("평점 없는 제품은 제외합니다.")
        print()
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]

    else:
        print("평점수 없는 제품은 제외합니다.")
        print()
        continue   
    
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
        print()   