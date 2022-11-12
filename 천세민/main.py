import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyApp(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap('box.png') # 박스 아이콘 @ 택배조회 칸
        boximage = QLabel()
        boximage.setPixmap(pixmap1)

        pixmap2 = QPixmap('food.png') # 수저 아이콘 @ 식단조회 칸
        soojeoimage = QLabel()
        soojeoimage.setPixmap(pixmap2)

        postpage = QVBoxLayout()
        postpage.addStretch(1)
        postpage.addWidget(QLabel("택배조회"))
        postpage.addStretch(3)
        postpage.addWidget(boximage)
        postpage.addStretch(4)

        foodpage = QVBoxLayout()
        foodpage.addStretch(1)
        foodpage.addWidget(QLabel("식단"))
        foodpage.addStretch(3)
        foodpage.addWidget(soojeoimage)
        foodpage.addStretch(4)

        postandfood = QHBoxLayout()
        postandfood.addLayout(postpage)
        postandfood.addLayout(foodpage)

        weatherpage = QVBoxLayout()
        weatherpage.addStretch(1)
        weatherpage.addWidget(QLabel("날씨"))
        weatherpage.addStretch(3)
        weatherpage.addWidget(boximage)
        weatherpage.addStretch(3)

        rightgrid = QVBoxLayout()
        rightgrid.addChildLayout(weatherpage)
        rightgrid.addChildLayout(postandfood)

        self.noticeSeoulBody = QTextBrowser()
        self.noticeSuwonBody = QTextBrowser()
        self.noticeSeoulHead = QLabel("인문사회과학캠퍼스\n \n 공지사항")
        self.noticeSuwonHead = QLabel("자연과학캠퍼스\n \n 공지사항")

        notice = QGridLayout()
        notice.addWidget(self.noticeHead(), 0, 0)
        notice.addWidget(self.noticechoose(), 0, 1)
        notice.addWidget(self.noticeBody(), 1, 0)

        allgrid = QHBoxLayout()
        allgrid.addLayout(notice)
        allgrid.addLayout(rightgrid)

        self.setLayout(allgrid)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()

    def noticechoose(self):
        groupbox = QGroupBox('캠퍼스 선택')

        self.radio1 = QRadioButton('인사캠')
        self.radio2 = QRadioButton('자과캠')
        self.radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        groupbox.setLayout(vbox)

        return groupbox

    def noticeHead(self):
        noticehead = QLabel()
        if self.radio1.isChecked():
            noticehead = self.noticeSeoulBody
        elif self.radio2.isChecked():
            noticehead = self.noticeSuwonBody

        return noticehead
    def noticeBody(self):
        noticebody = QTextBrowser()
        if self.radio1.isChecked():
            noticebody = self.noticeSeoulBody
        elif self.radio2.isChecked():
            noticebody = self.noticeSuwonBody

        return noticebody



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())