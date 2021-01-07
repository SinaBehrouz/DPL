from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from .UIFunctions import UIHandler
# import threading
# import concurrent.futures

class Ui_Dialog(object):
    def __init__(self):
        self.handler = UIHandler()
        self.EnteredPasscode = []
        self.msg = QMessageBox()

    def verifyPasscode(self):

        if self.handler.verifyPasscode(self.EnteredPasscode) == False:
            self.msg.setWindowTitle("Passcode Cannot be verified")
            self.msg.setText("Passcode Cannot be verified. Plase Double check it")
            self.msg.exec_()
            self.EnteredPasscode.clear()
            return

        self.msg.setWindowTitle("Passcode Verified")
        self.msg.setText("Please grab your package and close the locker")
        self.msg.exec_()

        self.handler.wait_till_locker_closes(self.EnteredPasscode)
        self.EnteredPasscode.clear()

    def verifyCameraRecordings(self):
        RecordingPassCode = self.handler.verifyCameraRecordings()
        if int(RecordingPassCode) > 0:
            self.msg.setWindowTitle("Passcode Verified")
            self.msg.setText("Your appropiate locker is now open")
            self.msg.exec_()

            self.handler.wait_till_locker_closes(RecordingPassCode)
            self.EnteredPasscode.clear()

        else:
            self.msg.setWindowTitle("Could not verify the tracking Number.")
            self.msg.setText("Wrong! Please try again or enter your passcode")
            self.msg.exec_()
            self.EnteredPasscode.clear()

    def setupUi(self, Dialog):
        print("GUI setupUi")
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 100, 451, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)

        self.pushButton_BackSpace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_BackSpace.setObjectName("pushButton_BackSpace")
        self.gridLayout.addWidget(self.pushButton_BackSpace, 3, 0, 1, 1)

        self.pushButton_Cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 3, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.WelcomeLabel = QtWidgets.QLabel(Dialog)
        self.WelcomeLabel.setGeometry(QtCore.QRect(160, 20, 431, 20))
        self.WelcomeLabel.setObjectName("WelcomeLabel")

        self.push_ScanQR = QtWidgets.QPushButton(Dialog)
        self.push_ScanQR.setGeometry(QtCore.QRect(220, 40, 231, 61))
        self.push_ScanQR.setObjectName("push_ScanQR")

        self.push_Enter = QtWidgets.QPushButton(Dialog)
        self.push_Enter.setGeometry(QtCore.QRect(110, 400, 451, 41))
        self.push_Enter.setObjectName("push_Enter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        print("GUI retranslateUi")
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.pushButton_0.setText(_translate("Dialog", "0"))
        # self.pushButton_0.clicked.connect(lambda: self.EnteredPasscode.append('0'))
        self.pushButton_0.clicked.connect(self.verifyPasscode)

        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_1.clicked.connect(lambda: self.EnteredPasscode.append('1'))

        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_2.clicked.connect(lambda: self.EnteredPasscode.append('2'))

        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_3.clicked.connect(lambda: self.EnteredPasscode.append('3'))

        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_4.clicked.connect(lambda: self.EnteredPasscode.append('4'))

        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_5.clicked.connect(lambda: self.EnteredPasscode.append('5'))

        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_6.clicked.connect(lambda: self.EnteredPasscode.append('6'))

        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_7.clicked.connect(lambda: self.EnteredPasscode.append('7'))

        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_8.clicked.connect(lambda: self.EnteredPasscode.append('8'))

        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_9.clicked.connect(lambda: self.EnteredPasscode.append('9'))

        self.pushButton_BackSpace.setText(_translate("Dialog", "Backspace"))
        self.pushButton_BackSpace.clicked.connect(lambda: self.EnteredPasscode.pop() if len(self.EnteredPasscode)>0 else None)

        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        # self.pushButton_Cancel.clicked.connect(lambda: self.EnteredPasscode.clear() )
        self.pushButton_Cancel.clicked.connect(lambda: print(self.EnteredPasscode) )

        self.push_Enter.setText(_translate("Dialog", "Enter"))
        self.push_Enter.clicked.connect(self.verifyPasscode)


        self.WelcomeLabel.setText(_translate("Dialog", "Please Enter your Passcode Or Scan your Package/QrCode"))
        self.push_ScanQR.setText(_translate("Dialog", "Scan Qr Code/Tracking Number"))

        self.push_ScanQR.clicked.connect(self.verifyCameraRecordings)
