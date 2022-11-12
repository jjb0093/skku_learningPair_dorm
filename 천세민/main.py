import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MyApp(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap('box.png') # 박스 아이콘 @ 택배조회 칸
        pixmap1 = pixmap1.scaled(150, 150, Qt.IgnoreAspectRatio)
        boximage = QLabel()
        boximage.setPixmap(pixmap1)

        pixmap2 = QPixmap('food.png') # 수저 아이콘 @ 식단조회 칸
        pixmap2 = pixmap2.scaled(150, 150, Qt.IgnoreAspectRatio)
        soojeoimage = QLabel()
        soojeoimage.setPixmap(pixmap2)

        postpage = QVBoxLayout()
        postpage.addStretch(1)
        postpage.addWidget(QPushButton("택배조회"))
        postpage.addStretch(3)
        postpage.addWidget(boximage)
        postpage.addStretch(4)

        foodpage = QVBoxLayout()
        foodpage.addStretch(1)
        foodpage.addWidget(QPushButton("식단"))
        foodpage.addStretch(3)
        foodpage.addWidget(soojeoimage)
        foodpage.addStretch(4)

        postandfood = QHBoxLayout()
        postandfood.addLayout(postpage)
        postandfood.addLayout(foodpage)

        weatherdata = QTextBrowser()

        weatherpage = QVBoxLayout()
        weatherpage.addStretch(1)
        weatherpage.addWidget(QPushButton("날씨"))
        weatherpage.addStretch(3)
        weatherpage.addWidget(weatherdata)
        weatherpage.addStretch(3)

        rightgrid = QVBoxLayout()
        rightgrid.addLayout(weatherpage)
        rightgrid.addLayout(postandfood)

        self.noticehead = QLabel("인문사회과학캠퍼스\n \n 공지사항")

        self.noticeSeoulbody = QVBoxLayout()
        self.noticeSeouldata = QTextBrowser() #여기에 서울 날씨 관련 자료 넣기

        self.noticeSuwonbody = QVBoxLayout()
        self.noticeSuwondata = QTextBrowser()  # 여기에 수원 날씨 관련 자료 넣기

        self.noticebody = QTextBrowser()

        self.radio1 = QRadioButton('인사캠')
        self.radio2 = QRadioButton('자과캠')
        self.radio1.setChecked(True)

        self.radio1.toggled.connect(self.radio1_clicked)
        self.radio2.toggled.connect(self.radio2_clicked)

        radiobox = QVBoxLayout()
        radiobox.addWidget(self.radio1)
        radiobox.addWidget(self.radio2)

        headandbutton = QHBoxLayout()
        headandbutton.addWidget(self.noticehead)
        headandbutton.addLayout(radiobox)

        notice = QVBoxLayout()
        notice.addLayout(headandbutton)
        notice.addWidget(self.noticebody)

        allgrid = QHBoxLayout()
        allgrid.addLayout(notice)
        allgrid.addLayout(rightgrid)

        self.setLayout(allgrid)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()

    def radio1_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('인문사회과학캠퍼스\n \n공지사항')
            self.noticebody.setLayout(self.noticeSeoulbody)

    def radio2_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('자연과학캠퍼스\n \n공지사항')
            self.noticebody.setLayout(self.noticeSuwonbody)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())