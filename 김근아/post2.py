import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from modules import delivery

class MyApp(QWidget):

    companyList = ['CJ 대한통운', '우체국택배', '한진택배', '롯데택배', '로젠택배', '경동택배', 'CVSnet 편의점택배(GS25)', 'CU 편의점택배']
    companyNum = ['04', '01', '05', '08', '06', '23', '24', '46']

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb = QComboBox(self)
        for i in range(len(MyApp.companyList)):
            self.cb.addItem(MyApp.companyList[i])
        self.cb.move(30,80)
        self.cb.resize(300,40)

        self.qle2 = QLineEdit(self)
        self.qle2.move(360, 80)
        self.qle2.resize(300,40)

        self.btn1 = QPushButton(self)
        self.btn1.setText('조회')
        self.btn1.move(690,80)
        self.btn1.resize(80,40)

        self.btn1.clicked.connect(self.btn1_clicked)

        self.tb = QTextBrowser(self)
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.move(30,160)
        self.tb.resize(740,420)

        self.setWindowTitle('POST')
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def btn1_clicked(self):
        index = MyApp.companyList.index(self.cb.currentText())
        result = delivery.getDelivery(MyApp.companyNum[index], self.qle2.text())
        self.tb.setText("<span style='font-size: 20px; font-weight: 600'>" + str(result[0]['item_name']) + " </span><span style='font-size: 20px; font-weight: 600; color: red;'>(" + ("배송 완료" if(result[0]['complete'] == True) else "배송 중") + ")</span><hr>")
        for i in range(len(result[1])):
            text = result[1][i]
            self.tb.append("<p style='font-size: 20px'>" + str(text['timeString']) + " / " + str(text['trans_where']) + " / " + str(text['trans_kind']).replace("\n", "") + "</p>")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())