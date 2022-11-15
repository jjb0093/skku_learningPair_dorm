import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from modules import dorm

class MyApp(QWidget):
    f = open("init.txt", 'r')
    campus = f.read()
    f.close()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap1 = QPixmap('images/box.png') # 박스 아이콘 @ 택배조회 칸
        pixmap1 = pixmap1.scaled(150, 150, Qt.IgnoreAspectRatio)
        boximage = QLabel()
        boximage.setPixmap(pixmap1)

        pixmap2 = QPixmap('images/food.png') # 수저 아이콘 @ 식단조회 칸
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

        if (MyApp.campus == "Seoul"): self.noticehead = QLabel("인문사회과학캠퍼스\n \n공지사항")
        else: self.noticehead = QLabel("자연과학캠퍼스\n \n공지사항")

        self.noticeSeoulbody = QVBoxLayout()
        self.noticeSeouldata = QTextBrowser() #여기에 서울 날씨 관련 자료 넣기

        self.noticeSuwonbody = QVBoxLayout()
        self.noticeSuwondata = QTextBrowser() # 여기에 수원 날씨 관련 자료 넣기

        result_notice = dorm.getDorm(MyApp.campus, 2)
        print(len(result_notice[1]) - int(result_notice[0]))

        self.noticebody = QTextBrowser()
        self.noticebody.setText("")

        url = {"Seoul":"https://dorm.skku.edu/dorm_seoul/notice/notice_all.jsp"}
        for i in range(int(result_notice[0])):
            self.noticebody.append("<a href='" + url[MyApp.campus] + result_notice[1][i][5] + "'><p style='color: red;'>" + result_notice[1][i][2] + "</p></a>")
            print("<a href='" + url[MyApp.campus] + result_notice[1][i][5] + "'><p style='color: red;'>" + result_notice[1][i][2] + "</p></a>")
        for i in range(len(result_notice[1]) - int(result_notice[0])):
            self.noticebody.append("<p style='color: black;'>" + result_notice[1][i+2][2] + "</p>")

        self.radio1 = QRadioButton('인사캠')
        self.radio2 = QRadioButton('자과캠')
        if(MyApp.campus == "Seoul"): self.radio1.setChecked(True)
        else: self.radio2.setChecked(True)

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
            campus = "Seoul"
            f = open("init.txt", 'w')
            f.write("Seoul")
            f.close

    def radio2_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('자연과학캠퍼스\n \n공지사항')
            self.noticebody.setLayout(self.noticeSuwonbody)
            campus = "Suwon"
            f = open("init.txt", 'w')
            f.write("Suwon")
            f.close

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())