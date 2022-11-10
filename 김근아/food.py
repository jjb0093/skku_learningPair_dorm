import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QLabel, QMainWindow, QAction, qApp, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tb1 = QTextBrowser(self)
        tb1.setAcceptRichText(True)
        tb1.setOpenExternalLinks(True)
        tb1.move(50, 130)
        tb1.resize(200, 400)

        tb2 = QTextBrowser(self)
        tb2.setAcceptRichText(True)
        tb2.setOpenExternalLinks(True)
        tb2.move(300, 130)
        tb2.resize(200, 400)

        tb3 = QTextBrowser(self)
        tb3.setAcceptRichText(True)
        tb3.setOpenExternalLinks(True)
        tb3.move(550, 130)
        tb3.resize(200, 400)

        lb1 = QLabel('아침', self)
        lb1.move(135, 100)
        font1 = lb1.font()
        font1.setPointSize(15)
        font1.setBold(True)
        lb1.setFont(font1)

        lb2 = QLabel('점심', self)
        lb2.move(385, 100)
        font2 = lb2.font()
        font2.setPointSize(15)
        font2.setBold(True)
        lb2.setFont(font2)

        lb3 = QLabel('저녁', self)
        lb3.move(635, 100)
        font3 = lb3.font()
        font3.setPointSize(15)
        font3.setBold(True)
        lb3.setFont(font3)

        exitAction = QAction(QIcon('back.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('FOOD')
        self.setGeometry(300, 300, 800, 600)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())