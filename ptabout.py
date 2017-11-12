from PyQt5 import QtCore, QtGui, QtWidgets

import resource_about

class AboutDialog(object):
    def setupUi(self, dlgAbout):
        self.dialog = dlgAbout
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.resize(512, 273)
        self.label = QtWidgets.QLabel(dlgAbout)
        self.label.setGeometry(QtCore.QRect(240, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dlgAbout)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dlgAbout)
        self.label_3.setGeometry(QtCore.QRect(240, 100, 241, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dlgAbout)
        self.label_4.setGeometry(QtCore.QRect(240, 140, 221, 21))
        self.label_4.setObjectName("label_4")
        self.btnCloseAbout = QtWidgets.QPushButton(dlgAbout)
        self.btnCloseAbout.setGeometry(QtCore.QRect(300, 190, 111, 31))
        self.btnCloseAbout.setObjectName("btnCloseAbout")
        self.label_5 = QtWidgets.QLabel(dlgAbout)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 187, 225))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

        # Wire up event handlers
        self.btnCloseAbout.clicked.connect(self.close_about_dialog)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "About PyProTracer"))
        self.label.setText(_translate("dlgAbout", "PyProTracer"))
        self.label_2.setText(_translate("dlgAbout", "Version: 1.0.0.0"))
        self.label_3.setText(_translate("dlgAbout", "PyProTracer is designed to visualize PGA Tour Trajectory data, mimicing television broadcasts."))
        self.label_4.setText(_translate("dlgAbout", "Developed by Ron Richardson"))
        self.btnCloseAbout.setText(_translate("dlgAbout", "Close"))
        self.label_5.setText(_translate("dlgAbout", "<html><head/><body><p><img src=\":/logo/logo-about.png\"/></p></body></html>"))


    # Event Handlers
    def close_about_dialog(self):
        self.dialog.done(0)
