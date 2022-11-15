import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap = QPixmap('sun.jpg') # 날씨 아이콘 - 예제

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)

        time = QDateTime.currentDateTime() #시간 및 날짜 세팅

        tableWidget = QTableWidget() # 표 세팅
        tableWidget.setRowCount(1)
        tableWidget.setColumnCount(7)

        tableWidget.setVerticalHeaderItem(0, QTableWidgetItem('날씨'))
        for i in range(7):
            tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(time.addSecs(7200*(i-3)).toString('MM월 dd일 hh:mm')))

        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # tableWidget.setItem(i, j, QTableWidgetItem()) - 여기다가 자료 채워주세용


        grid = QGridLayout() # 온,습,강 나타내는 그리드
        grid.addWidget(QLabel("온도: "), 0, 0)
        grid.addWidget(QLabel("습도: "), 1, 0)
        grid.addWidget(QLabel("강수량: "), 2, 0)

        grid.addWidget(QTextBrowser(), 0, 1) # 현재 온도 자료
        grid.addWidget(QTextBrowser(), 1, 1) # 현재 습도 자료
        grid.addWidget(QTextBrowser(), 2, 1) # 현재 강수량 자료

        hbox = QHBoxLayout() # 온습강 그리드와 날씨 아이콘
        hbox.addStretch(1)
        hbox.addLayout(grid)
        hbox.addWidget(lbl_img)

        vbox = QVBoxLayout() #hbox와 시간별 날씨 표시
        vbox.addStretch(4)
        vbox.addLayout(hbox)
        vbox.addStretch(2)
        vbox.addWidget(QLabel('시간별 날씨'))
        vbox.addStretch(1)
        vbox.addWidget(tableWidget)
        vbox.addStretch(4)

        self.setLayout(vbox)

        self.setWindowTitle('Weather')
        self.setGeometry(300, 100, 800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())