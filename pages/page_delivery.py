from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from modules import delivery

class Delivery(QWidget):

    companyList = ['CJ 대한통운', '우체국택배', '한진택배', '롯데택배', '로젠택배', '경동택배', 'CVSnet 편의점택배(GS25)', 'CU 편의점택배']
    companyNum = ['04', '01', '05', '08', '06', '23', '24', '46']

    def __init__(self):
        super().__init__()
        self.initUI()
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(46, 78, 63))
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.setStyleSheet('QLabel {color: white;}')

    def initUI(self):
        head = QLabel("택배 조회")
        font1 = head.font()
        font1.setPointSize(25)
        font1.setBold(True)
        head.setFont(font1)

        help = QLabel("택배사를 선택하고 운송장 번호를 입력하세요.")

        self.cb = QComboBox()
        for i in range(len(Delivery.companyList)):
            self.cb.addItem(Delivery.companyList[i])
        self.cb.setFixedWidth(300)
        self.cb.setFixedHeight(40)

        self.qle2 = QLineEdit()
        self.qle2.setFixedWidth(300)
        self.qle2.setFixedHeight(40)

        self.btn1 = QPushButton()
        self.btn1.setText('조회')
        self.btn1.setStyleSheet('QPushButton {background-color: #167023; color: white; border-radius: 3px;}')
        self.btn1.setFixedWidth(80)
        self.btn1.setFixedHeight(40)
        self.btn1.clicked.connect(self.btn1_clicked)

        browser = QHBoxLayout()
        browser.addWidget(self.cb)
        browser.addWidget(self.qle2)
        browser.addWidget(self.btn1)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.tb.setStyleSheet('QTextBrowser {background-color: #FFFFFF; border-radius: 3px;}')

        credit = QLabel("본 정보는 스마트택배에서 제공받는 정보로, 실제 배송상황과 다를 수 있습니다.")
        font1 = credit.font()
        font1.setPointSize(10)
        credit.setFont(font1)

        oklayout = QVBoxLayout()
        oklayout.addWidget(head)
        oklayout.addWidget(help)
        oklayout.addLayout(browser)
        oklayout.addWidget(self.tb)
        oklayout.addWidget(credit)

        blank = QHBoxLayout()
        blank.addStretch(1)
        blank.addLayout(oklayout)
        blank.addStretch(1)

        self.setLayout(blank)

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
