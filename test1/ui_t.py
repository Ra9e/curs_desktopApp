# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_t.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #301E43")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 141))
        self.frame.setStyleSheet("background-color: #46AB8C    ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notifyME = QtWidgets.QLabel(self.frame)
        self.notifyME.setGeometry(QtCore.QRect(80, 40, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.notifyME.setFont(font)
        self.notifyME.setAutoFillBackground(False)
        self.notifyME.setStyleSheet("color: #301E43")
        self.notifyME.setObjectName("notifyME")
        self.pic = QtWidgets.QLabel(self.frame)
        self.pic.setGeometry(QtCore.QRect(340, 50, 51, 51))
        self.pic.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("../загружено.png"))
        self.pic.setScaledContents(True)
        self.pic.setObjectName("pic")
        self.set_time = QtWidgets.QLabel(self.centralwidget)
        self.set_time.setGeometry(QtCore.QRect(50, 170, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.set_time.setFont(font)
        self.set_time.setStyleSheet("color: #46AB8C")
        self.set_time.setObjectName("set_time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 420, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #46AB8C")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-10, 570, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #46AB8C;\n"
"    background-color: #301E43;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #21083A;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 250, 291, 141))
        self.plainTextEdit.setStyleSheet("color: white;\n"
"border: 2px solid #46AB8C;\n"
"border-radius: 10;\n"
"background-color: #301E43;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(137, 481, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("color: white;\n"
"border: 2px solid #46AB8C;\n"
"background-color: #301E43;\n"
"border-radius: 10;")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.notifyME.setText(_translate("MainWindow", "notifyME"))
        self.set_time.setText(_translate("MainWindow", "enter a message"))
        self.label.setText(_translate("MainWindow", "set the countdown"))
        self.pushButton.setText(_translate("MainWindow", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
