# class1.py
#1) 클래스 형식을 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #인스턴트 멤버 변수 초기화
        self.name = "default name"
    
    def print(self):
        print("My name is {}".format(self.name))

#2) 인스턴트 생성
p1 = Person()
p2 = Person()

#3) 메서드 호출
p1.name = "전우치"
p1.print()
p2.print()

#런타임(코드가 실행되는 시점)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30
print(p1.age) #이것은 가능하나 쓰지말자
# print(p2.age) #에러
# print(Person.age) #에러

str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = ""
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str) #str은 전역변수다, self.str를 출력해야 멤버변수가 찍힌다.

g= GString()
g.set("First Message")
g.print()