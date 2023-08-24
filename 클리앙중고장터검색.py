# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request #웹서버 요청 라이브러리
import re #검색(키워드) 사용을 위한 정규식 라이브러리

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
#가끔 사이트에서 header가 비어있으면 막는경우가 있어서,우회용
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\clien.txt", "wt", encoding="utf-8")

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr) #헤더같이 넘김
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우에 사용
        page = data.decode('utf-8', 'ignore') #ignore는 약간 글자가깨져도 상관없아는 옵션
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        #<span class="subject_fixed" data-role="list-title-text" title="맥북프로 m1 13인치 512GB 판매합니다(가격인하)">
	#	맥북프로 m1 13인치 512GB 판매합니다(가격인하)
	#</span>

        for item in list:
                try:
                        #아래는 태그안에 다른태그가 중복으로 있을경우, 해당태그로 넘어가는 소스인데, 클리앙에는 맞지않아 주석처리함
                        #<a class='list_subject'><span>text</span><span>text</span>
                        #span = item.contents[1]
                        #span2 = span.nextSibling.nextSibling
                        #title = span2.text 
                        title = item.text.strip()
                        #print(title)

                        if (re.search('아이폰', title)):
                                print(title)
                                f.write(title + "\n")
                        #        print('https://www.clien.net'  + item['href'])
                        #<a href="httt://wwww">xx</a>  만일 링크를뽑고싶으면 link = item.find("a")["href"]
                except:
                        pass #에러나면 스킵(다음으로 넘어감), 광고등 태그가 안맞을수도 있으니, 에러코드 출력하는걸 넣어도 됨
        
f.close()