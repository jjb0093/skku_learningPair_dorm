import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from modules import delivery

class Delivery(QWidget):

    companyList = ['CJ 대한통운', '우체국택배', '한진택배', '롯데택배', '로젠택배', '경동택배', 'CVSnet 편의점택배(GS25)', 'CU 편의점택배']
    companyNum = ['04', '01', '05', '08', '06', '23', '24', '46']

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb = QComboBox(self)
        for i in range(len(Delivery.companyList)):
            self.cb.addItem(Delivery.companyList[i])
        self.cb.setMaximumWidth(300)

        self.qle2 = QLineEdit(self)
        self.qle2.setMaximumWidth(300)

        self.btn1 = QPushButton(self)
        self.btn1.setText('조회')
        self.btn1.setMaximumWidth(80)
        self.btn1.setStyleSheet('QPushButton {background-color: #167023; color: white; border-radius: 3px;}')

        self.btn1.clicked.connect(self.btn1_clicked)

        self.browser = QHBoxLayout()
        self.browser.addWidget(self.cb)
        self.browser.addWidget(self.qle2)
        self.browser.addWidget(self.btn1)

        self.tb = QTextBrowser(self)
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.allbox = QVBoxLayout()
        self.allbox.addLayout(self.browser)
        self.allbox.addWidget(self.tb)

        self.setLayout(self.allbox)

        self.setWindowTitle('POST')
        self.setGeometry(300, 300, 800, 600)
        self.show()

    def btn1_clicked(self):
        index = Delivery.companyList.index(self.cb.currentText())
        result = delivery.getDelivery(Delivery.companyNum[index], self.qle2.text())
        print(result)
        self.tb.setText("<span style='font-size: 20px; font-weight: 600'>" + str(
            result[0]['item_name']) + " </span><span style='font-size: 20px; font-weight: 600; color: red;'>(" + (
            "배송 완료" if (result[0]['complete'] == True) else "배송 중") + ")</span><hr>")
        for i in range(len(result[1])):
            text = result[1][i]
            self.tb.append("<p style='font-size: 20px'>" + str(text['timeString']) + " / " + str(text['trans_where']) + " / " + str(text['trans_kind']).replace("\n", "") + "</p>")
        #self.write(Delivery.companyNum[index], self.qle2.text())
        #self.tb.setText("<span style='font-size: 20px; font-weight: 600; color: red;'>일치하는 정보가 없습니다. 입력한 택배사, 운송번호를 다시 확인해주세요.</span><hr>")


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Delivery()
   sys.exit(app.exec_())

def show():
    app = QApplication(sys.argv)
    ex = Delivery()
    sys.exit(app.exec_())