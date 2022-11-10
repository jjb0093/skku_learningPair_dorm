import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDateTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        postpage = QGridLayout()
        postpage.addWidget(QLabel("택배조회"))

        postAndFood = QHBoxLayout()


        self.setWindowTitle('Main')
        self.setGeometry(300, 100, 800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())