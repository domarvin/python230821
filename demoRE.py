# demoRE.py
# 정규표현식은 chat gpt에 물어봐라
# 파이썬에서 re.search()를 사용해서 이메일주소를 찾는 패턴을 만들어줘
import re

result = re.search("[0~9]*th", "35th")
print(result)
print(result.group())

# 야래는 에러가 난다
# result = re.match("[0~9]*th", "35th")
# print(result)
# print(result.group())

print("---연도를 찾는 경우---")
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())

print("---우편번호를 찾는 경우---")
result = re.search("\d{5}", "우리 동네는 52300입니다..")
print(result.group())