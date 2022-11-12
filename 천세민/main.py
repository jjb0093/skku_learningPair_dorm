import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime


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
        foodpage.addWidget(boximage)
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

        noticeSeoulBody = QTextBrowser()
        noticeSuwonBody = QTextBrowser()

        btnSeoul = QRadioButton("인사캠")
        btnSuwon = QRadioButton("자과캠")
        btnSeoul.setChecked(True)

        if btnSeoul.isChecked():
            notice = QGridLayout()
            notice.addWidget(QLabel("인문사회과학캠퍼스"), 0, 0)
            notice.addWidget(QLabel("기숙사 공지사항"), 1, 0)
            notice.addWidget(btnSeoul, 0, 1)
            notice.addWidget(btnSuwon, 1, 1)
            notice.addWidget(noticeSeoulBody, 2, 0)

        if btnSuwon.isChecked():
            notice = QGridLayout()
            notice.addWidget(QLabel("자연과학캠퍼스"), 0, 0)
            notice.addWidget(QLabel("기숙사 공지사항"), 1, 0)
            notice.addWidget(btnSeoul, 0, 1)
            notice.addWidget(btnSuwon, 1, 1)
            notice.addWidget(noticeSuwonBody)

        allgrid = QHBoxLayout()
        allgrid.addLayout(notice)
        allgrid.addLayout(rightgrid)

        self.setLayout(allgrid)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())