import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap('box.png')

        boximage = QLabel()
        boximage.setPixmap(pixmap1)

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

        postandfood = QGridLayout()
        postandfood.addChildLayout(postpage, 0, 0)
        postandfood.addChildLayout(foodpage, 0, 1)

        weatherpage = QVBoxLayout()
        weatherpage.addStretch(1)
        weatherpage.addWidget(QLabel("날씨"))
        weatherpage.addStretch(3)
        weatherpage.addWidget(boximage)
        weatherpage.addStretch(3)

        rightgrid = QGridLayout()
        rightgrid.addChildLayout(weatherpage, 0, 0)
        rightgrid.addChildLayout(postandfood, 1, 0)

        noticeSeoul = QGridLayout()
        noticeSeoul.addWidget(QLabel("인문사회과학캠퍼스"))
        noticeSeoul.addWidget(QLabel("기숙사 공지사항"))

        noticeSuwon = QVBoxLayout()
        noticeSuwon.addStretch(1)
        noticeSuwon.addWidget()

        notice = QVBoxLayout()


        allgrid = QGridLayout()
        allgrid.addChildLayout(0, 0)
        allgrid.addChildLayout(rightgrid, 0, 1)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())