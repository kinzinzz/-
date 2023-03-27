import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
url = "http://nadocoing.tistroy.com"
res = requests.get(url, headers=headers)
res.raise_for_status()

# 파일 만들기
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

print("성공")