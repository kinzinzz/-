# 정규식

import re

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미 > cafe, case, cave, care
# ^ (^de): 문자열의 시작 > desk, destination
# $ (se$): 문자열의 끝 > case, base

def print_match(m):
    
    # 매치되지 않으면 에러가 발생
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 일치하는 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index

    else:
        print("매칭되지 않음")
        
# m = p.match("case") # 주어진 문자열의 처음부터 일치하는지  확인 good care(x) careless(o)
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("careless cafe") # findall : 일치하는 모든 것을 리스틔 형태로 반환
print(lst)

# 1. p = re.complie("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열을 처음부터 일치하는지 확인
