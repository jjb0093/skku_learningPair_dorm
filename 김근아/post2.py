import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextBrowser, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QComboBox(self)
        cb.addItem('CJ대한통운')
        cb.addItem('우체국택배')
        cb.addItem('한진택배')
        cb.addItem('롯데택배')
        cb.addItem('로젠택배')
        cb.addItem('홈픽')
        cb.addItem('CVSnet 편의점택배(GS25)')
        cb.addItem('CU 편의점택배')
        cb.move(30,100)
        cb.resize(300,40)

        qle2 = QLineEdit(self)
        qle2.move(360, 100)
        qle2.resize(300,40)

        btn1 = QPushButton(self)
        btn1.setText('조회')
        btn1.move(690,100)
        btn1.resize(80,40)

        tb = QTextBrowser(self)
        tb.setAcceptRichText(True)
        tb.setOpenExternalLinks(True)
        tb.move(30,160)
        tb.resize(740,400)

        pixmap = QPixmap('back.png')
        pixmap = pixmap.scaled(30, 30, Qt.IgnoreAspectRatio)

        icon = QIcon()
        icon.addPixmap(pixmap)

        button = QPushButton(self)
        button.setIcon(icon)
        button.setIconSize(QSize(30, 30))


        self.setWindowTitle('POST')
        self.setGeometry(300, 300, 800, 600)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())