# DemoDict.py

colors = {"apple":"red", "banana":"yellow"}
print(len(colors))

#입력
colors["kiwi"] = "green"

#검색
print(colors["apple"])

for item in colors.items():
    print(item)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
#아래는 복사본을 만드는게 아니라 같은 참조를 쓴다
p = phone
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))

#아래처럼 위치 인자는 못쓴다
#print(phone[0])
print(phone["kim"])

#원본과 별도의 복사보을 생성하는 경우
import copy
device = {"아이폰":5, "아이패드":10}
#별도의 복사본을 생성
device2 = copy.deepcopy(device)
#device2 = device #이것은 참조, 위는 값복사(서로다른 객체)
device["맥북"] = 20
print(device)
print(device2)
