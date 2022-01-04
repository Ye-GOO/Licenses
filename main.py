def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1213, 670)
    MainWindow.setFixedSize(1213, 670)  # 设置窗体固定大小
    MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
    self.scrollArea.setGeometry(QtCore.QRect(690, 40, 511, 460))
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setObjectName("scrollArea")
    self.scrollAreaWidgetContents = QtWidgets.QWidget()
    self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 489))
    self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    self.label_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.label_0.setGeometry(QtCore.QRect(10, 10, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(11)
    self.label_0.setFont(font)
    self.label_0.setObjectName("label_0")
    self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
    self.label.setGeometry(QtCore.QRect(10, 40, 481, 420))
    self.label.setObjectName("label")
    self.label.setAlignment(Qt.AlignCenter)
    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
    self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 671, 631))
    self.scrollArea_2.setWidgetResizable(True)
    self.scrollArea_2.setObjectName("scrollArea_2")
    self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
    self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 669, 629))
    self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
    self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_1)
    self.label_1.setGeometry(QtCore.QRect(10, 10, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(11)
    self.label_1.setFont(font)
    self.label_1.setObjectName("label_1")
    self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_1)
    self.tableWidget.setGeometry(QtCore.QRect(10, 40, 651, 581))  # 581))
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(5)
    self.tableWidget.setColumnWidth(0, 140)  # 设置1列的宽度
    self.tableWidget.setColumnWidth(1, 130)  # 设置2列的宽度
    self.tableWidget.setColumnWidth(2, 110)  # 设置3列的宽度
    self.tableWidget.setColumnWidth(3, 90)  # 设置4列的宽度
    self.tableWidget.setColumnWidth(4, 181)  # 设置5列的宽度
    self.tableWidget.setHorizontalHeaderLabels(["图片名称", "录入时间", "车牌号码", "车牌类型", "车牌信息"])
    self.tableWidget.setRowCount(self.RowLength)
    self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头)
    self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.tableWidget.raise_()
    self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_1)
    self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
    self.scrollArea_3.setGeometry(QtCore.QRect(690, 510, 341, 131))
    self.scrollArea_3.setWidgetResizable(True)
    self.scrollArea_3.setObjectName("scrollArea_3")
    self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
    self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 129))
    self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
    self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
    self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(11)
    self.label_2.setFont(font)
    self.label_2.setObjectName("label_2")
    self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
    self.label_3.setGeometry(QtCore.QRect(10, 40, 321, 81))
    self.label_3.setObjectName("label_3")
    self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
    self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
    self.scrollArea_4.setGeometry(QtCore.QRect(1040, 510, 161, 131))
    self.scrollArea_4.setWidgetResizable(True)
    self.scrollArea_4.setObjectName("scrollArea_4")
    self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
    self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 159, 129))
    self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
    self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
    self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 121, 31))
    self.pushButton_2.setObjectName("pushButton_2")
    self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
    self.pushButton.setGeometry(QtCore.QRect(20, 90, 121, 31))
    self.pushButton.setObjectName("pushButton")
    self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
    self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(11)
    self.label_4.setFont(font)
    self.label_4.setObjectName("label_4")
    self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    self.pushButton.clicked.connect(self.__openimage)  # 设置点击事件
    self.pushButton.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
    self.pushButton_2.clicked.connect(self.__writeFiles)  # 设置点击事件
    self.pushButton_2.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
    self.retranslateUi(MainWindow)
    self.close_widget = QtWidgets.QWidget(self.centralwidget)
    self.close_widget.setGeometry(QtCore.QRect(1130, 0, 90, 50))
    self.close_widget.setObjectName("close_widget")
    self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
    self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格
    self.left_close = QPushButton("")  # 关闭按钮
    self.left_close.clicked.connect(self.close)
    self.left_visit = QPushButton("")  # 空白按钮
    self.left_visit.clicked.connect(MainWindow.big)
    self.left_mini = QPushButton("")  # 最小化按钮
    self.left_mini.clicked.connect(MainWindow.mini)
    self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
    self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
    self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
    self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
    self.left_close.setStyleSheet(
        '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet(
        '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet(
        '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    self.ProjectPath = os.getcwd()  # 获取当前工程文件位置
    self.scrollAreaWidgetContents.setStyleSheet(sc)
    self.scrollAreaWidgetContents_3.setStyleSheet(sc)
    self.scrollAreaWidgetContents_4.setStyleSheet(sc)
    b = '''
         color:white;
         background:#2B2B2B;
        '''
    self.label_0.setStyleSheet(b)
    self.label_1.setStyleSheet(b)
    self.label_2.setStyleSheet(b)
    self.label_3.setStyleSheet(b)
    MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
    MainWindow.setAttribute(Qt.WA_TranslucentBackground)
    MainWindow.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框



def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "车牌识别系统"))
    self.label_0.setText(_translate("MainWindow", "原始图片："))
    self.label.setText(_translate("MainWindow", ""))
    self.label_1.setText(_translate("MainWindow", "识别结果："))
    self.label_2.setText(_translate("MainWindow", "车牌区域："))
    self.label_3.setText(_translate("MainWindow", ""))
    self.pushButton.setText(_translate("MainWindow", "打开文件"))
    self.pushButton_2.setText(_translate("MainWindow", "导出数据"))
    self.label_4.setText(_translate("MainWindow", "事件："))
    self.scrollAreaWidgetContents_1.show()