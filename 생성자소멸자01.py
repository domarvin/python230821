# -*- 생성자와 소멸자 -*-
class MyClass:
    #초기화메서드
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소명자메서드
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
m = MyClass(5)

del m #GC 가비지 컬렉터가 30분 ~ 1시간마다 메모리 정리한다. 따라서 쓸필요 없다.
#print(m.value) # m 접근안됨
# del을 막고 실행시킨후, 터미널 끄려고 하면 del 이 자동실행됨
print("전체 코드 실행 종료")
