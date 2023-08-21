# function1.py
# 함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 x:", x)

# 함수 호출
# 함수에서 리턴하지를 않기때문에 None 값이된다.
result = setValue(5)
print(result)

# 여러개 값을 리턴
def swap(x,y):
    return y,x

# 호출
print(swap(3,4))