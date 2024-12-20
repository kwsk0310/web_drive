# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 771, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.lineEdit_remote = QtWidgets.QLineEdit(self.page_1)
        self.lineEdit_remote.setGeometry(QtCore.QRect(180, 90, 251, 21))
        self.lineEdit_remote.setObjectName("lineEdit_remote")
        self.label_remote = QtWidgets.QLabel(self.page_1)
        self.label_remote.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_remote.setObjectName("label_remote")
        self.label_title1 = QtWidgets.QLabel(self.page_1)
        self.label_title1.setGeometry(QtCore.QRect(30, 30, 501, 31))
        self.label_title1.setObjectName("label_title1")
        self.cancel = QtWidgets.QPushButton(self.page_1)
        self.cancel.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.cancel.setObjectName("cancel")
        self.next_1 = QtWidgets.QPushButton(self.page_1)
        self.next_1.setGeometry(QtCore.QRect(670, 490, 75, 23))
        self.next_1.setObjectName("next_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_user = QtWidgets.QLabel(self.page_2)
        self.label_user.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_user.setObjectName("label_user")
        self.label_host = QtWidgets.QLabel(self.page_2)
        self.label_host.setGeometry(QtCore.QRect(60, 170, 111, 16))
        self.label_host.setObjectName("label_host")
        self.label_port = QtWidgets.QLabel(self.page_2)
        self.label_port.setGeometry(QtCore.QRect(60, 210, 111, 16))
        self.label_port.setObjectName("label_port")
        self.label_pass = QtWidgets.QLabel(self.page_2)
        self.label_pass.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label_pass.setObjectName("label_pass")
        self.lineEdit_port = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_port.setGeometry(QtCore.QRect(180, 210, 251, 21))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_user = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_user.setGeometry(QtCore.QRect(180, 90, 251, 21))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_pass.setGeometry(QtCore.QRect(180, 130, 251, 21))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_host = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_host.setGeometry(QtCore.QRect(180, 170, 251, 21))
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.label_title_2 = QtWidgets.QLabel(self.page_2)
        self.label_title_2.setGeometry(QtCore.QRect(30, 30, 381, 31))
        self.label_title_2.setObjectName("label_title_2")
        self.next_2 = QtWidgets.QPushButton(self.page_2)
        self.next_2.setGeometry(QtCore.QRect(670, 490, 75, 23))
        self.next_2.setObjectName("next_2")
        self.back_2 = QtWidgets.QPushButton(self.page_2)
        self.back_2.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.back_2.setObjectName("back_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.finish = QtWidgets.QPushButton(self.page_3)
        self.finish.setGeometry(QtCore.QRect(670, 490, 75, 23))
        self.finish.setObjectName("finish")
        self.label_title_3 = QtWidgets.QLabel(self.page_3)
        self.label_title_3.setGeometry(QtCore.QRect(30, 30, 381, 31))
        self.label_title_3.setObjectName("label_title_3")
        self.info = QtWidgets.QLabel(self.page_3)
        self.info.setGeometry(QtCore.QRect(80, 100, 451, 271))
        self.info.setStyleSheet("background-color: white; border: 2px solid gray;")
        self.info.setText("")
        self.info.setObjectName("info")
        self.info.setWordWrap(True)
        self.back_3 = QtWidgets.QPushButton(self.page_3)
        self.back_3.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.back_3.setObjectName("back_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_remote.setText(_translate("MainWindow", "遠端名稱："))
        self.label_title1.setText(_translate("MainWindow", "將您的 SFTP 伺服器上的資料掛載到本地路徑 D:/sftp 並顯示"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.next_1.setText(_translate("MainWindow", "Next"))
        self.label_user.setText(_translate("MainWindow", "用戶名稱："))
        self.label_host.setText(_translate("MainWindow", "sftp伺服器網址："))
        self.label_port.setText(_translate("MainWindow", "sftp伺服器阜號："))
        self.label_pass.setText(_translate("MainWindow", "用戶密碼："))
        self.label_title_2.setText(_translate("MainWindow", "您是第一次使用此遠端名稱，請先進行連線設定"))
        self.next_2.setText(_translate("MainWindow", "Next"))
        self.back_2.setText(_translate("MainWindow", "Back"))
        self.finish.setText(_translate("MainWindow", "Finish"))
        self.label_title_3.setText(_translate("MainWindow", "連線狀態："))
        self.back_3.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
