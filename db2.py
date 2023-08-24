# db1.py

import sqlite3

#일단은 메모리에 저장
#con = sqlite3.connect(":memory:")
#파일로 저장
con = sqlite3.connect("c:\\work\\test2.db")

#구문 실행은 커서객체에서
cur = con.cursor()
#테이블 구조 생성
cur.execute("create table if not exists PhoneBook" + 
  " (id integer primary key autoincrement, name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동', '010-111-1111');")

#입력 파라메터 처리
name = "전우치"
phoneNumber = "010-222-2222"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

#다중의 레코드 입력
datalist = (("박문수", "010-333-3333"), ("김길동","010-444-4444"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

#결과 확인
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
    
#아래처럼 하면, 레코드 커서 가 한번 꺼낼때마다 다음번을 가리키므로, tetchall 등이 전체가 아닐수 있어서,대부분 위처럼 for문을 쓴다
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

# 위까지 실행후 페치하면 결과값도 보이지만, 이프로그램이 끝나고 다른데서 조회하면 데이타가 없다
# commit를 안하면, 나갈때 롤백된다.
#import sqlite3
#con = sqlite3.connect("c:\\work\\test.db")
#cur = con.cursor()
#cur.execute("select * from PhoneBook;")
#<sqlite3.Cursor object at 0x000001AD9929B940>
#cur.fetchall()
#[]
#---위를 다른데서 돌려보면 데이타 없다---

#커밋을 실행
con.commit()

#연결닫기
con.close()
