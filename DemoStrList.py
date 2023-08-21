# DemoStrList.py
# 실행 :ctrl + F5
strA = "python is very powerful"
strB = "파이썬은 강력해"
strC = """파이썬을
오늘부터
학습합니다."""

print(strA)
print(len(strC))
print(strC)

result = "py" + "thon"
print(result)
#슬라이싱(인덱싱)
print(strA[0])
print(strA[0:6])
#약식(축약)
print(strA[:6])
print(strA[-3:])

print("---list형식---")
lst = [1,2,3,4,5]
print(len(lst))
print(lst[0])
lst.append(10)
lst.insert(1,20)
print(lst)
colors = ["red", "blue", "green"]
# "red"를 끝에 추가해주나, 이렇게 쓰지말고 append를 쓰자
colors += ["red"]
# 아래처럼 하면 r e d 3글자를 각각 넣는다. 이것도 쓰지말자
colors += "red"
print(colors)
colors.remove("red")
print(colors)

#디버깅 할 때 중단점(break point)
for item in colors:
    print(item)

print("---tuple---")
tp = (10, 20, 30)
print(len(tp))
print(tp)
print("id:%s, name:%s" % ("kim", "김유신"))

#함수 정의
def times(a,b):
    return a+b, a*b

#함수 호출
print(times(5, 6))

args = (3, 4)
print(times(*args))  #args가 tuple임을 알리기 위해 *를 붙여야한다.

#아래처럼 리스트로 만들었는데도 *를 붙여야 에러안난다
args1 = [3, 4]
print(times(*args)) 

print("---형식변환---")
d = (1,2,3)
a = set(d) #tuple을 set로 변환
#위 2줄을 아래 줄로 대체 가능
#a = set((1,2,3))
print(a)
b = list(a) #set을 list로 변환
b.append(4)
print(b)
c = tuple(b) #list를 tuple로 변환
print(c)

print("---set---")
a = {1,2,3,4}
b = {3,4,4,5}
print(len(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#print(a[0])