# demoRandomOS.py

import random

print(random.random())
print(random.random())
print(random.uniform(2,5))
print([random.randrange(20) for i in range(10)]) # 0~20까지 숫자중 10개를 중복허용 뽑음
print([random.randrange(20) for i in range(10)])
print("---샘플링---")
print(random.sample(range(20),10)) # 0~20까지 숫자중 10개를 안겹치게 유니크하게 뽑음
print(random.sample(range(20),10))

from os.path import *
from os import *

print(abspath("python.exe")) #현재의 경로(파일이 있는지? 검사하는게 아니라, 현재 접속 폴더)
print(basename("c:\\python310\\python.exe")) #파일명만 꺼냄

if exists("c:\\python310\\python.exe"):
    print("파일크기:{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일 없음")

print("운영체제이름:{0}".format(name))
print("환경변수:{0}".format(environ))
#system("notepad.exe") #프로그램 실행

#파일 목록
import glob
print(glob.glob("c:\\work\\*.py"))
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)

