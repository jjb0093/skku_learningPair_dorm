import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime, QSize, Qt
from modules import weather as w


class Weather(QWidget):
    f = open("init.txt", 'r')
    campus = f.read()
    f.close()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        result = w.getWeather(Weather.campus)

        time = QDateTime.currentDateTime() #시간 및 날짜 세팅

        tableWidget = QTableWidget() # 표 세팅
        tableWidget.resize(200,600)
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(6)

        tableWidget.setVerticalHeaderItem(0, QTableWidgetItem('날씨'))
        tableWidget.setVerticalHeaderItem(1, QTableWidgetItem('온도'))
        tableWidget.setVerticalHeaderItem(2, QTableWidgetItem('습도'))
        tableWidget.setVerticalHeaderItem(3, QTableWidgetItem('강수확률'))
        for i in range(6):
            tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(time.addSecs(3600*(i+1)).toString('hh')+"시"))

        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(6):
            sky = int(result[i+1]['sky'])
            pty = int(result[i+1]['pty'])
            if(sky == 1): tableWidget.setItem(0, i, QTableWidgetItem("맑음"))
            else:
                if(pty == 0):
                    if(sky == 3): tableWidget.setItem(0, i, QTableWidgetItem("구름 많음"))
                    elif(sky == 4): tableWidget.setItem(0, i, QTableWidgetItem("흐림"))
                elif(pty == 1 or pty == 4): tableWidget.setItem(0, i, QTableWidgetItem("비"))
                elif(pty == 2 or pty == 3): tableWidget.setItem(0, i, QTableWidgetItem("눈"))

        signs = ["°C", "%", "%"]
        for i in range(1, 4):
            for k in range(6):
                tableWidget.setItem(i, k, QTableWidgetItem(str(list(result[k+1].values())[i+1])+signs[i-1]))


        grid = QGridLayout() # 온,습,강 나타내는 그리드
        grid.addWidget(QLabel("온도: "), 0, 0)
        grid.addWidget(QLabel(), 1, 0)
        grid.addWidget(QLabel("습도: "), 2, 0)
        grid.addWidget(QLabel(), 3, 0)
        grid.addWidget(QLabel("강수확률: "), 4, 0)

        sky_now = int(result[0]['sky'])
        pty_now = int(result[0]['pty'])
        if (sky_now == 1): state = "맑음"
        else:
            if (pty_now == 0):
                if (sky_now == 3): state = "구름많음"
                elif (sky_now == 4): state = "흐림"
            elif (pty_now == 1 or pty_now == 4): state = "비"
            elif (pty_now == 2 or pty_now == 3): state = " 눈"

        grid.addWidget(QLabel(str(result[0]['tmp'])+"°C"), 0, 1) # 현재 온도 자료
        grid.addWidget(QLabel(), 1, 1)
        grid.addWidget(QLabel(str(result[0]['reh'])+"%"), 2, 1) # 현재 습도 자료
        grid.addWidget(QLabel(), 3, 1)
        grid.addWidget(QLabel(str(result[0]['pop'])+"%"), 4, 1) # 현재 강수확률 자료

        gridbox = QVBoxLayout()
        gridbox.addStretch(1)
        gridbox.addLayout(grid)
        gridbox.addStretch(1)

        lbl_img = QLabel()
        lbl_img.resize(300, 300)

        cloudpic = QPixmap('images/cloud.png')
        cloudpic = cloudpic.scaledToWidth(300)
        rainpic = QPixmap('images/rain.png')
        rainpic = rainpic.scaledToWidth(300)
        snowpic = QPixmap('images/snow.png')
        snowpic = snowpic.scaledToWidth(300)
        sunpic = QPixmap('images/sun.png')
        sunpic = sunpic.scaledToWidth(300)

        if(state == "맑음"): lbl_img.setPixmap(sunpic)
        elif(state == "흐림" or state == "구름많음"): lbl_img.setPixmap(cloudpic)
        elif(state == "비"): lbl_img.setPixmap(rainpic)
        elif(state == "눈"): lbl_img.setPixmap(snowpic)

        photobox = QVBoxLayout()
        photobox.addStretch(6)
        photobox.addWidget(lbl_img)
        photobox.addStretch(1)

        hbox = QHBoxLayout() # 온습강 그리드와 날씨 아이콘
        hbox.addStretch(1)
        hbox.addLayout(photobox)
        hbox.addStretch(1)
        hbox.addLayout(gridbox)
        hbox.addStretch(3)

        vbox = QVBoxLayout() #hbox와 시간별 날씨 표시
        vbox.addStretch(7)
        vbox.addLayout(hbox)
        vbox.addWidget(QLabel('시간별 날씨'))
        vbox.addWidget(tableWidget)
        vbox.addStretch(2)

        pixmap = QPixmap('images/back.png')
        pixmap = pixmap.scaled(30, 30, Qt.IgnoreAspectRatio)

        icon = QIcon()
        icon.addPixmap(pixmap)

        button = QPushButton(self)
        button.setIcon(icon)
        button.setIconSize(QSize(30, 30))

        self.setLayout(vbox)

        self.setWindowTitle('Weather')
        self.setGeometry(300, 100, 800, 600)
        self.show()

def show():
    app = QApplication(sys.argv)
    ex = Weather()
    sys.exit(app.exec_())