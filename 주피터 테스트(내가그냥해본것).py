#jupyter notebook이아닌 그냥 파이썬 코드에서 차트 그리려면
#C:\Users\student\Desktop\교육\Python핵심과정_리뉴얼_2023\TKInter  안에있는 Matplotlib_labels.py 소스 참조할것

#선언 추가(차트 그리기 위해)
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
dfExcel = pd.read_excel("c:\\work\\demo.xlsx", "Sheet1")
dfExcel
#빈 그림판 추가
fig = plt.figure()
#총 4개 차트를 만들수 있다.
#챠트를 추가(1행, 1열, 1차트)
ax = fig.add_subplot(1,1,1)
#히스토그림
ax.hist(dfExcel["나이"],bins=11) #bins는 데이타를 몇개군으로 모아서 볼것이냐?
def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()