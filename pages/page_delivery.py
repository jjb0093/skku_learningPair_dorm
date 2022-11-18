import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from modules import delivery
class Delivery(QWidget):
    f = open("init.txt", 'r')
    lines = f.readlines()
    campus = lines[0].replace("\n", "")
    f.close()
    companyList = ['CJ 대한통운', '우체국택배', '한진택배', '롯데택배', '로젠택배', '경동택배', 'CVSnet 편의점택배(GS25)', 'CU 편의점택배']
    companyNum = ['04', '01', '05', '08', '06', '23', '24', '46']
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        head = QLabel("택배 조회", self)
        head.move(30, 20)
        head.resize(200, 40)
        font1 = head.font()
        font1.setPointSize(25)
        font1.setBold(True)
        head.setFont(font1)

        help = QLabel("택배사를 선택하고 운송장 번호를 입력하세요.", self)
        help.move(30, 70)
        help.resize(350, 30)

        self.cb = QComboBox(self)
        for i in range(len(Delivery.companyList)):
            self.cb.addItem(Delivery.companyList[i])
        self.cb.move(30,110)
        self.cb.resize(300,40)
        self.qle2 = QLineEdit(self)
        self.qle2.move(360, 110)
        self.qle2.resize(300,40)
        self.btn1 = QPushButton(self)
        self.btn1.setText('조회')
        self.btn1.move(690,110)
        self.btn1.resize(80,40)
        self.btn1.setStyleSheet('QPushButton {background-color: #167023; color: white; border-radius: 3px;}')
        self.btn1.clicked.connect(self.btn1_clicked)
        self.tb = QTextBrowser(self)
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.move(30,160)
        self.tb.resize(740,400)
        self.tb.setStyleSheet('QTextBrowser {background-color: #FFFFFF; border-radius: 3px;}')

        self.setWindowTitle('POST')
        self.setGeometry(300, 300, 800, 600)
        self.show()
    def btn1_clicked(self):
        index = Delivery.companyList.index(self.cb.currentText())
        result = delivery.getDelivery(Delivery.companyNum[index], self.qle2.text())
        if(result == "ERROR"): self.tb.setText("<span style='font-size: 20px; color: red;'>배송 정보가 조회되지 않았습니다. 택배사와 운송장 번호를 다시 확인해주세요.</span>")
        else:
            self.tb.setText("<span style='font-size: 20px; font-weight: 600'>" + str(result[0]['item_name']) + " </span><span style='font-size: 20px; font-weight: 600; color: red;'>(" + ("배송 완료" if(result[0]['complete'] == True) else "배송 중") + ")</span><hr>")
            for i in range(len(result[1])):
                text = result[1][i]
                self.tb.append("<p style='font-size: 20px'>" + str(text['timeString']) + " / " + str(text['trans_where']) + " / " + str(text['trans_kind']).replace("\n", "") + "</p>")
            self.write(Delivery.companyNum[index], self.qle2.text())
    def write(self, code, invoice):
        print(code, invoice)
        f = open("init.txt", 'w')
        f.write(Delivery.campus + "\n" + code + "\n" + invoice)
        f.close()
def show():
    app = QApplication(sys.argv)