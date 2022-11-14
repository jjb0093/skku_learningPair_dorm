import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb = QComboBox(self)
        self.cb.addItem('CJ대한통운')
        self.cb.addItem('우체국택배')
        self.cb.addItem('한진택배')
        self.cb.addItem('롯데택배')
        self.cb.addItem('로젠택배')
        self.cb.addItem('홈픽')
        self.cb.addItem('CVSnet 편의점택배(GS25)')
        self.cb.addItem('CU 편의점택배')
        self.cb.move(30,100)
        self.cb.resize(300,40)

        self.qle2 = QLineEdit(self)
        self.qle2.move(360, 100)
        self.qle2.resize(300,40)

        self.btn1 = QPushButton(self)
        self.btn1.setText('조회')
        self.btn1.move(690,100)
        self.btn1.resize(80,40)

        self.btn1.clicked.connect(self.btn1_clicked)

        self.tb = QTextBrowser(self)
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.move(30,160)
        self.tb.resize(740,400)

        pixmap = QPixmap('김근아/back.png')
        pixmap = pixmap.scaled(30, 30, Qt.IgnoreAspectRatio)

        icon = QIcon()
        icon.addPixmap(pixmap)

        button = QPushButton(self)
        button.setIcon(icon)
        button.setIconSize(QSize(30, 30))


        self.setWindowTitle('POST')
        self.setGeometry(300, 300, 800, 600)
        self.show()
    def btn1_clicked(self):
        #print(self.cb)
        one_text = self.cb.currentText()
        two_text = self.qle2.text()
        QMessageBox.about(self, "Message", two_text)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())