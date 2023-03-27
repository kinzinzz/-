import requests

res = requests.get("http://google.com")
res.raise_for_status() # 오류가 발생하면 프로그램 종료

# 파일 만들기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
