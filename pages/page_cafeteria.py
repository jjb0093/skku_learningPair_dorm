import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QLabel, QAction, qApp, QPushButton,QVBoxLayout,QGridLayout,QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt, QSize
from modules import cafeteria

class Cafeteria(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(46, 78, 63))
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.setStyleSheet('QLabel {color: white;}')

    def initUI(self):

        todaysmeal = QLabel("오늘의 학식")
        font0 = todaysmeal.font()
        font0.setPointSize(30)
        font0.setBold(True)
        todaysmeal.setFont(font0)


        epn = QLabel("오늘의 기숙사 학식을 확인하세요!")


        self.tb1 = QTextBrowser()
        self.tb1.setAcceptRichText(True)
        self.tb1.setOpenExternalLinks(True)
        self.tb1.setFixedSize(200, 400)
        self.tb1.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        self.tb2 = QTextBrowser()
        self.tb2.setAcceptRichText(True)
        self.tb2.setOpenExternalLinks(True)
        self.tb2.setFixedSize(200, 400)
        self.tb2.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        self.tb3 = QTextBrowser()
        self.tb3.setAcceptRichText(True)
        self.tb3.setOpenExternalLinks(True)
        self.tb3.setFixedSize(200, 400)
        self.tb3.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        lb1 = QLabel('아침', self)
        lb1.setAlignment(Qt.AlignCenter)
        font1 = lb1.font()
        font1.setPointSize(15)
        font1.setBold(True)
        lb1.setFont(font1)

        lb2 = QLabel('점심', self)
        lb2.setAlignment(Qt.AlignCenter)
        font2 = lb2.font()
        font2.setPointSize(15)
        font2.setBold(True)
        lb2.setFont(font2)

        lb3 = QLabel('저녁')
        lb3.setAlignment(Qt.AlignCenter)
        font3 = lb3.font()
        font3.setPointSize(15)
        font3.setBold(True)
        lb3.setFont(font3)

        tlb1 = QVBoxLayout()
        tlb1.addWidget(lb1)
        tlb1.addWidget(self.tb1)

        tlb2 = QVBoxLayout()
        tlb2.addWidget(lb2)
        tlb2.addWidget(self.tb2)

        tlb3 = QVBoxLayout()
        tlb3.addWidget(lb3)
        tlb3.addWidget(self.tb3)

        tables = QHBoxLayout()
        tables.addLayout(tlb1)
        tables.addStretch(2)
        tables.addLayout(tlb2)
        tables.addStretch(2)
        tables.addLayout(tlb3)

        final = QVBoxLayout()
        final.addStretch(2)
        final.addWidget(todaysmeal)
        final.addStretch(1)
        final.addWidget(epn)
        final.addStretch(1)
        final.addLayout(tables)
        final.addStretch(2)

        blank = QHBoxLayout()
        blank.addStretch(1)
        blank.addLayout(final)
        blank.addStretch(1)

        f = open("init.txt", 'r')
        campus = f.readlines()[0].replace("\n", "")
        result = cafeteria.getFood(campus)
        f.close()

        food = []
        for i in range(len(result)): food.append(result[i])
        for i in range(len(food[0].keys())):
            self.tb1.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[0].keys())[i] + "</span>")
            self.tb1.append("<span style='font-size: 16px'>" + str(list(food[0].values())[i]).replace(',', "\n") + "</span>")
        for i in range(len(food[1].keys())):
            self.tb2.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[1].keys())[i] + "</span>")
            self.tb2.append("<span style='font-size: 16px'>" + str(list(food[1].values())[i]).replace(',', "\n") + "</span><br>")
        for i in range(len(food[2].keys())):
            self.tb3.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[2].keys())[i] + "</span>")
            self.tb3.append("<span style='font-size: 16px'>" + str(list(food[2].values())[i]).replace(',', "\n") + "</span><br>")


        self.setLayout(blank)

        self.setWindowTitle('FOOD')
        self.setGeometry(300, 300, 800, 600)
        self.show()

def show():
    app = QApplication(sys.argv)
    ex = Cafeteria()
    sys.exit(app.exec_())