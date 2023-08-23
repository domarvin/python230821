# demoFile.py
f = open("c:\\work\\demo2.txt", "wt", encoding="utf-8")
f.write("데이터1번\n데이타2번\n데이터3번\n")
f.close()

#읽기
f = open("c:\\work\\demo2.txt", encoding="utf-8")
result = f.read()
print("---read()---")
print(result)
print("---readline()---")
f.seek(0)
#print(f.readline(), end="\n") #print는 줄끝에 줄바꿈을 기본적으로 \n을 자동으로 주는데, 이걸 ""로 처리하면 줄바꿈하지 않음
print(f.readline(), end="") 
print(f.readline(), end="")
print("---readlines()---")
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="")
f.close()