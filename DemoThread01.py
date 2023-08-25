import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#아래는 병렬로 따로 도는 백그라운드 뜨레드 함수이다. 시간오래걸리는 작업등에사용
class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()