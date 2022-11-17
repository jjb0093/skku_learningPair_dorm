import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize, QDir
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

        pixmap1 = QPixmap('images/delivery.png')  # 박스 아이콘 @ 택배조회 칸
        pixmap1 = pixmap1.scaled(500, 500, Qt.IgnoreAspectRatio)
        boximage = QLabel()
        boximage.setPixmap(pixmap1)

        iicon = QIcon()
        iicon.addPixmap(pixmap1)
        self.button1 = QPushButton(self)
        self.button1.move(450, 470)
        self.button1.setIcon(iicon)
        self.button1.setIconSize(QSize(150, 250))
        self.button1.setStyleSheet('QPushButton {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        pixmap2 = QPixmap('images/food.png')  # 박스 아이콘 @ 택배조회 칸
        pixmap2 = pixmap2.scaled(500, 500, Qt.IgnoreAspectRatio)
        foodimage = QLabel()
        foodimage.setPixmap(pixmap2)

        icon = QIcon()
        icon.addPixmap(pixmap2)
        self.button2 = QPushButton(self)
        self.button2.move(670, 470)
        self.button2.setIcon(icon)
        self.button2.setIconSize(QSize(150, 250))
        self.button2.setStyleSheet('QPushButton {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        self.wthicon = QIcon()
        self.button3 = QPushButton(self)

        pixmap4 = QPixmap('images/skku.png')
        pixmap4 = pixmap4.scaled(40, 40, Qt.IgnoreAspectRatio)
        skkuimage = QLabel()
        skkuimage.setPixmap(pixmap4)
        skkuimage.resize(40, 40)

        postpage = QVBoxLayout()
        postpage.addWidget(QLabel("택배조회"))
        postpage.addWidget(self.button1)
        self.button1.clicked.connect(lambda :self.openPage("delivery"))

        foodpage = QVBoxLayout()
        foodpage.addWidget(QLabel("식단"))
        foodpage.addWidget(self.button2)
        self.button2.clicked.connect(lambda :self.openPage("cafeteria"))

        postandfood = QHBoxLayout()
        postandfood.addLayout(postpage)
        postandfood.addLayout(foodpage)

        weatherpage = QVBoxLayout()
        weatherpage.addWidget(QLabel("날씨"))
        weatherpage.addWidget(self.button3)
        self.button3.clicked.connect(lambda :self.openPage("weather"))

        rightgrid = QVBoxLayout()
        rightgrid.addLayout(weatherpage)
        rightgrid.addLayout(postandfood)

        if (MyApp.campus == "Seoul"): self.noticehead = QLabel("인문사회과학캠퍼스")
        else: self.noticehead = QLabel("자연과학캠퍼스")
        self.noticehead.setFixedWidth(400)

        font2 = self.noticehead.font()
        font2.setPointSize(30)
        self.noticehead.setFont(font2)

        gongji = QLabel("공지사항")

        self.noticeSeoulbody = QVBoxLayout()
        self.noticeSeouldata = QTextBrowser() #여기에 서울 날씨 관련 자료 넣기

        self.noticeSuwonbody = QVBoxLayout()
        self.noticeSuwondata = QTextBrowser() # 여기에 수원 날씨 관련 자료 넣기

        self.noticebody = QTextBrowser()
        self.noticebody.setStyleSheet('QTextBrowser {background-color: #FFFFFF; border-radius: 5px;}')
        self.noticebody.setOpenExternalLinks(True)
        MyApp.showNotice(self)

        self.radio1 = QRadioButton('인사캠')
        self.radio2 = QRadioButton('자과캠')
        if(MyApp.campus == "Seoul"): self.radio1.setChecked(True)
        else: self.radio2.setChecked(True)

        self.radio1.toggled.connect(self.radio1_clicked)
        self.radio2.toggled.connect(self.radio2_clicked)

        radiobox = QHBoxLayout()
        radiobox.addWidget(self.radio1)
        radiobox.addWidget(self.radio2)

        headandbutton = QGridLayout()
        headandbutton.addWidget(skkuimage, 0, 0)
        headandbutton.addWidget(self.noticehead, 0, 2)
        headandbutton.addWidget(gongji, 3, 0)
        headandbutton.addLayout(radiobox, 3, 6)

        notice = QVBoxLayout()
        notice.addLayout(headandbutton)
        notice.addWidget(self.noticebody)

        allgrid = QHBoxLayout()
        allgrid.addLayout(notice)
        allgrid.addLayout(rightgrid)

        self.setLayout(allgrid)

        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 900, 700)
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
        MyApp.showWeather(self)

    def showWeather(self):
        result = weather.getNowWeather(MyApp.campus)

        sky = int(result[0]['sky'])
        pty = int(result[0]['pty'])
        tmp = result[0]['tmp']
        reh = result[0]['reh']
        pop = result[0]['pop']

        if (sky == 1): state = "맑음"
        else:
            if (pty == 0):
                if (sky == 3): state = "구름많음"
                elif (sky == 4): state = "흐림"
            elif (pty == 1 or pty == 4): state = "비"
            elif (pty == 2 or pty == 3): state = " 눈"

        cloudpic = QPixmap('images/cloud.png')
        cloudpic = cloudpic.scaled(500, 500, Qt.IgnoreAspectRatio)
        rainpic = QPixmap('images/rain.png')
        rainpic = rainpic.scaled(500, 500, Qt.IgnoreAspectRatio)
        snowpic = QPixmap('images/snow.png')
        snowpic = snowpic.scaled(500, 500, Qt.IgnoreAspectRatio)
        sunpic = QPixmap('images/sun.png')
        sunpic = sunpic.scaled(500, 500, Qt.IgnoreAspectRatio)


        if (state == "맑음"): self.wthicon.addPixmap(sunpic)
        elif (state == "흐림" or state == "구름많음"): self.wthicon.addPixmap(cloudpic)
        elif (state == "비"): self.wthicon.addPixmap(rainpic)
        elif (state == "눈"): self.wthicon.addPixmap(snowpic)
        self.button3.setIcon(self.wthicon)
        self.button3.setIconSize(QSize(370, 350))

        self.button3.setText(tmp+"°C\n \n"+state)

        self.button3.setStyleSheet('QPushButton {background-color: #FFFFFF; color: black; border-radius: 5px;}')


    def radio1_clicked(self, enabled):
        if enabled:
            self.noticehead.setText('인문사회과학캠퍼스')
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
            self.noticehead.setText('자연과학캠퍼스')
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

    dir = QDir("fonts")
    fontDB = QFontDatabase().addApplicationFont("fonts/AppleSDGothicNeoL.ttf.ttf")
    print(QFontDatabase().applicationFontFamilies(fontDB))
    app.setFont(QFont("AppleSDGothicNeoL00"))

    ex = MyApp()
    sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())