# DemoForm.py
# DemoForm.ui(화면을 저장) + DemoForm.py(로직을 저장)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0] # []은 보통 ui하나당 .ui파일을 하나씩 저장하지만, 한파일에 여러 ui저장시 각각 배열처리

#폼 클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 폼 데모")

#직접 모듈을 생행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv) #프로그램 띄울때 실행프로세스 만드는 부분
    demoForm = DemoForm() #위에 초기화 함수 실행
    demoForm.show() #화면 보이기
    app.exec_() #앱의 사용자 액션을 대기