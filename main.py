import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from modules import dorm, weather

class MyApp(QWidget):

    if (not os.path.isfile("init.txt")):
        campus = "Seoul"
        f = open("init.txt", 'w')
        f.write("Seoul")
        f.close()
    else:
        f = open("init.txt", 'r')
        campus = f.readlines()[0].replace("\n","")
        f.close()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap1 = QPixmap('images/delivery.png') # 박스 아이콘 @ 택배조회 칸
        pixmap1 = pixmap1.scaled(200, 200, Qt.IgnoreAspectRatio)
        boximage = QLabel()
        boximage.setPixmap(pixmap1)
        #self.page_delivery = delivery.MyApp()
        #boximage.mousePressEvent = self.page_delivery.show

        pixmap2 = QPixmap('images/food.png') # 수저 아이콘 @ 식단조회 칸
        pixmap2 = pixmap2.scaled(200, 200, Qt.IgnoreAspectRatio)
        soojeoimage = QLabel()
        soojeoimage.setPixmap(pixmap2)

        postpage = QVBoxLayout()
        postpage.addStretch(1)
        btnDelivery = QPushButton("택배조회")
        postpage.addWidget(btnDelivery)
        postpage.addStretch(3)
        postpage.addWidget(boximage)
        postpage.addStretch(4)
        btnDelivery.clicked.connect(lambda :self.openPage("delivery"))

        foodpage = QVBoxLayout()
        foodpage.addStretch(1)
        btnFood = QPushButton("식단")
        foodpage.addWidget(btnFood)
        foodpage.addStretch(3)
        foodpage.addWidget(soojeoimage)
        foodpage.addStretch(4)
        btnFood.clicked.connect(lambda :self.openPage("cafeteria"))

        postandfood = QHBoxLayout()
        postandfood.addLayout(postpage)
        postandfood.addLayout(foodpage)

        weatherdata = QTextBrowser()

        weatherpage = QVBoxLayout()
        weatherpage.addStretch(1)
        btnWeather = QPushButton("날씨")
        weatherpage.addWidget(btnWeather)
        weatherpage.addStretch(3)
        weatherpage.addWidget(weatherdata)
        weatherpage.addStretch(3)
        btnWeather.clicked.connect(lambda :self.openPage("weather"))

        rightgrid = QVBoxLayout()
        rightgrid.addLayout(weatherpage)
        rightgrid.addLayout(postandfood)

        if (MyApp.campus == "Seoul"): self.noticehead = QLabel("인문사회과학캠퍼스\n \n공지사항")
        else: self.noticehead = QLabel("자연과학캠퍼스\n \n공지사항")

        self.noticeSeoulbody = QVBoxLayout()
        self.noticeSeouldata = QTextBrowser() #여기에 서울 날씨 관련 자료 넣기

        self.noticeSuwonbody = QVBoxLayout()
        self.noticeSuwondata = QTextBrowser() # 여기에 수원 날씨 관련 자료 넣기

        self.noticebody = QTextBrowser()
        self.noticebody.setOpenExternalLinks(True)
        MyApp.showNotice(self)

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

        self.showWeather()

        self.setLayout(allgrid)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()

    def fileCheck(self):
        import os
        if(not os.path.isfile("init.txt")):
            self.campus = "Seoul"
            f = open.file("init.txt", 'w')
            f.write("Seoul")
            f.close

    def openPage(self, page):
        from pages import page_delivery, page_weather, page_cafeteria

        if(page == "delivery"):
            self.pageDelivery = page_delivery.Delivery()
            self.pageDelivery.show()
        elif(page == "weather"):
            self.pageWeather = page_weather.Weather()
            self.pageWeather.show()
        elif(page == "cafeteria"):
            self.pageCafeteria = page_cafeteria.Cafeteria()
            self.pageCafeteria.show()

    def showNotice(self):
        result_notice = dorm.getDorm(MyApp.campus, 1)

        self.noticebody.setText("")
        url = {"Seoul": "https://dorm.skku.edu/dorm_seoul/notice/notice_all.jsp",
               "Suwon": "https://dorm.skku.edu/dorm_suwon/notice/notice_all.jsp"}

        for i in range(int(result_notice[0])):
            self.noticebody.append(
                "<a href='" + url[MyApp.campus] + result_notice[1][i][5] + "' style='text-decoration: none;'><p style='color: red;');>" +
                result_notice[1][i][2] + "</p></a>")
        for i in range(len(result_notice[1]) - int(result_notice[0])):
            self.noticebody.append("<a href='" + url[MyApp.campus] + result_notice[1][i+2][5] + "' style='text-decoration: none;'>"
                                   "<p style='color: black;'>" + result_notice[1][i + 2][2] + "</p></a>")

    def showWeather(self):
        result = weather.getNowWeather(MyApp.campus)
        sky = int(result[0]['sky'])
        pty = int(result[0]['pty'])
        if (sky == 1): state = "맑음"
        else:
            if (pty == 0):
                if (sky == 3): state = "구름많음"
                elif (sky == 4): state = "흐림"
            elif (pty == 1 or pty == 4): state = "비"
            elif (pty == 2 or pty == 3): state = " 눈"


    def radio1_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('인문사회과학캠퍼스\n \n공지사항')
            self.noticebody.setLayout(self.noticeSeoulbody)
            MyApp.campus = "Seoul"
            f = open("init.txt", 'r')
            lines = f.readlines()
            f.close()
            f = open("init.txt", 'w')
            f.write("Seoul\n" + lines[1] + lines[2])
            f.close
            MyApp.showNotice(self)

    def radio2_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('자연과학캠퍼스\n \n공지사항')
            self.noticebody.setLayout(self.noticeSuwonbody)
            MyApp.campus = "Suwon"
            f = open("init.txt", 'r')
            lines = f.readlines()
            f.close()
            f = open("init.txt", 'w')
            f.write("Suwon\n" + lines[1] + lines[2])
            f.close
            MyApp.showNotice(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())