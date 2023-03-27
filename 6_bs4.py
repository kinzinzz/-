import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text())
# print(soup.a) # soup 객첵에서 처음 발견되는 a element 출력
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

# print(rank3.a.get_text())
# rank2 = rank2.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# print(rank1.find_next_siblings("li"))
webtoon = soup.find("a", text="김부장-70화 에피소드 마무리+아레스 [1]")
print(webtoon)