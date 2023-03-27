from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
url = "https://flight.naver.com/"
browser.get(url)
browser.maximize_window()
time.sleep(2)

btns = browser.find_elements(By.CLASS_NAME, "btn")

for btn in btns:
   if btn.get_attribute("title") == "한 달간 안보기":
       btn.click()
       break
time.sleep(1)

# 가는 날 선택 클릭
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(2)

# 날짜 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button/b").click()
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[3]/td[5]/button").click()
time.sleep(2)

# 도착지 선택 버튼 클릭
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(2)

# 도착지 검색어 입력
browser.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").send_keys("도쿄")
time.sleep(2)

# 도착지 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/div/a[1]").click()
time.sleep(2)
# 직항만 검색
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[3]/button[2]").click()
time.sleep(2)

# 검색
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()
time.sleep(10)

# 스크롤링
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


elem = browser.find_element(By.CLASS_NAME, "concurrent_inner__iqfJr")
print(elem.text)
# elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[4]/div[1]/div/button")



