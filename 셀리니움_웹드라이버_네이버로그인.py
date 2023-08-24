# 셀리니움_웹드라이버_네이버로그인.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

#아래는 에러나서 두번째로 고침
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "sksmsdhlfhqek69"
clipboard.copy(loginID) #복사및 시간조절
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')  #XPATH는 태그를계층구조로 관리, //*[@id="id"] 는 모든태그에서 id가 id인것 찾아라

loginPW = "do58150816@"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

#창이 닫히는걸 막기위해 아래는 무한루프를 돌리는 부분
while True:
    pass 