        pixmap1 = QPixmap('delivery.png')  # 박스 아이콘 @ 택배조회 칸
        pixmap1 = pixmap1.scaled(500, 500, Qt.IgnoreAspectRatio)
        boximage = QLabel()
        boximage.setPixmap(pixmap1)

        icon = QIcon()
        icon.addPixmap(pixmap1)
        self.button1 = QPushButton(self)
        self.button1.move(450,470)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QSize(150, 200))

        pixmap2 = QPixmap('food.png')  # 박스 아이콘 @ 택배조회 칸
        pixmap2 = pixmap2.scaled(500, 500, Qt.IgnoreAspectRatio)
        foodimage = QLabel()
        foodimage.setPixmap(pixmap2)

        icon = QIcon()
        icon.addPixmap(pixmap2)
        self.button2 = QPushButton(self)
        self.button2.move(670, 470)
        self.button2.setIcon(icon)
        self.button2.setIconSize(QSize(150, 200))

        pixmap3 = QPixmap('sun.png')  # 박스 아이콘 @ 택배조회 칸
        pixmap3 = pixmap3.scaled(200, 200, Qt.IgnoreAspectRatio)
        wthimage = QLabel()
        wthimage.setPixmap(pixmap3)

        icon = QIcon()
        icon.addPixmap(pixmap3)
        self.button3 = QPushButton(self)
        self.button3.move(450, 100)
        self.button3.setIcon(icon)
        self.button3.setIconSize(QSize(370, 350))
        self.button3.setText('g')