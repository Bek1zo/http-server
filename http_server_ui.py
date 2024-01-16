from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 345)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(480, 345))
        MainWindow.setMaximumSize(QSize(480, 345))
        icon = QIcon()
        icon.addFile(u"assets/favicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            """
                QWidget {
                    background-color:#2C3E50;
                    color: #fff
                }
                
                QPushButton{
                    background-color:#06799F;
                    border:none;
                    color:#ffffff;
                    font-size:12px;
                    font-family:Tahoma;
                }
                
                QPushButton:disabled {
                    background-color: #024E68;
                }
                
                QPushButton:hover {
                    background-color:#216278;
                }
                
                QTextEdit {
                    background-color: #fff;
                    color: black;
                }
                
                QMenuBar {
                    border-bottom: 1px solid #024E68
                }
            """
        )
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionTray = QAction(MainWindow)
        self.actionTray.setObjectName(u"actionTray")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(10, 10, 171, 31))
        self.startButton.setStyleSheet(u"")
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(10, 50, 171, 31))
        self.stopButton.setCheckable(False)
        self.stopButton.setAutoDefault(False)
        self.serverPort = QTextEdit(self.centralwidget)
        self.serverPort.setObjectName(u"serverPort")
        self.serverPort.setGeometry(QRect(260, 10, 211, 31))
        self.serverPort.setAutoFillBackground(False)
        self.serverPortLabel = QLabel(self.centralwidget)
        self.serverPortLabel.setObjectName(u"serverPortLabel")
        self.serverPortLabel.setGeometry(QRect(200, 20, 54, 17))
        self.serverAdress = QTextEdit(self.centralwidget)
        self.serverAdress.setObjectName(u"serverAdress")
        self.serverAdress.setGeometry(QRect(260, 50, 211, 31))
        self.serverAdress.setReadOnly(True)
        self.serverAddressLabel = QLabel(self.centralwidget)
        self.serverAddressLabel.setObjectName(u"serverAddressLabel")
        self.serverAddressLabel.setGeometry(QRect(200, 60, 54, 17))
        self.history = QTextEdit(self.centralwidget)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(10, 130, 461, 171))
        self.history.setReadOnly(True)
        self.chooseDirButton = QPushButton(self.centralwidget)
        self.chooseDirButton.setObjectName(u"chooseDirButton")
        self.chooseDirButton.setGeometry(QRect(10, 90, 461, 31))
        self.chooseDirButton.setCheckable(False)
        self.chooseDirButton.setAutoDefault(False)
        self.aboutLabel = QLabel(self.centralwidget)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setGeometry(QRect(10, 300, 461, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 480, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionInfo)
        self.menu.addAction(self.actionTray)
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.stopButton.setDefault(False)
        self.chooseDirButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HTTP File Server", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionTray.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432 \u0442\u0440\u0435\u0439", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.serverPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"8000", None))
        self.serverPortLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442:", None))
        self.serverAdress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.serverAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP-\u0410\u0434\u0440\u0435\u0441", None))
        self.chooseDirButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi