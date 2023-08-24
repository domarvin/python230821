# web1.py
#크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩(메서드 체인, 함수체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색을 위한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#문서 전체에서 <p> 검색
#print(soup.find_all("p"))

#첫번째 <p>를 검색
#print(soup.find("p"))

#조건이 있는 경우:<p class='outer'>
#print(soup.find_all("p", class_="outer-text")) #class에 _를 붙여야한다.(파이썬에서 class는 별도 용도의 용어이므로)
#특정 속성을 지정할 때: attrs    #위에 class_ 를 쓰기보다는 아래처럼 한다.
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#특정 id만 지정
#print(soup.find_all(id="first"))
#태그 내부에 컨텐츠를 출력 : .text .get_text()
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print("----")
    print(tag)
    print(title)
    print("----")
