import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QLabel, QAction, qApp, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from modules import cafeteria

class Cafeteria(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap = QPixmap("images/Cafeteria-2.jpg")
        pixmap.scaled(800, 200, Qt.IgnoreAspectRatio)
        image = QLabel()
        image.move(0, 0)
        image.setPixmap(pixmap)

        self.tb1 = QTextBrowser(self)
        self.tb1.setAcceptRichText(True)
        self.tb1.setOpenExternalLinks(True)
        self.tb1.move(50, 180)
        self.tb1.resize(200, 400)
        self.tb1.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        self.tb2 = QTextBrowser(self)
        self.tb2.setAcceptRichText(True)
        self.tb2.setOpenExternalLinks(True)
        self.tb2.move(300, 180)
        self.tb2.resize(200, 400)
        self.tb2.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        self.tb3 = QTextBrowser(self)
        self.tb3.setAcceptRichText(True)
        self.tb3.setOpenExternalLinks(True)
        self.tb3.move(550, 180)
        self.tb3.resize(200, 400)
        self.tb3.setStyleSheet('QTextBrowser {background-color: #FFFFFF; color: black; border-radius: 5px;}')

        lb1 = QLabel('아침', self)
        lb1.move(135, 150)
        font1 = lb1.font()
        font1.setPointSize(15)
        font1.setBold(True)
        lb1.setFont(font1)

        lb2 = QLabel('점심', self)
        lb2.move(385, 150)
        font2 = lb2.font()
        font2.setPointSize(15)
        font2.setBold(True)
        lb2.setFont(font2)

        lb3 = QLabel('저녁', self)
        lb3.move(635, 150)
        font3 = lb3.font()
        font3.setPointSize(15)
        font3.setBold(True)
        lb3.setFont(font3)

        f = open("init.txt", 'r')
        campus = f.readlines()[0].replace("\n", "")
        result = cafeteria.getFood(campus)
        f.close()

        food = []
        for i in range(len(result)): food.append(result[i])
        for i in range(len(food[0].keys())):
            self.tb1.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[0].keys())[i] + "</span>")
            self.tb1.append("<span style='font-size: 16px'>" + str(list(food[0].values())[i]).replace(',', "\n") + "</span>")
            self.tb1.append("\n")
        for i in range(len(food[1].keys())):
            self.tb2.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[1].keys())[i] + "</span>")
            self.tb2.append("<span style='font-size: 16px'>" + str(list(food[1].values())[i]).replace(',', "\n") + "</span><br><br>")
        for i in range(len(food[2].keys())):
            self.tb3.append("<span style='font-size: 20px; font-weight: 800'>" + list(food[2].keys())[i] + "</span>")
            self.tb3.append("<span style='font-size: 16px'>" + str(list(food[2].values())[i]).replace(',', "\n") + "</span><br><br>")

        self.setWindowTitle('FOOD')
        self.setGeometry(300, 300, 800, 600)
        self.show()

def show():
    app = QApplication(sys.argv)
    ex = Cafeteria()
    sys.exit(app.exec_())