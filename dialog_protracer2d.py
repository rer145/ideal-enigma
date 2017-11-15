# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/protracer2d.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg2D(object):
    def setupUi(self, dlg2D):
        dlg2D.setObjectName("dlg2D")
        dlg2D.resize(800, 600)
        self.groupBox = QtWidgets.QGroupBox(dlg2D)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 141))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(dlg2D)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 781, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 771, 401))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(dlg2D)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlg2D)

    def retranslateUi(self, dlg2D):
        _translate = QtCore.QCoreApplication.translate
        dlg2D.setWindowTitle(_translate("dlg2D", "PyProTracer 2D"))
        self.groupBox.setTitle(_translate("dlg2D", "Legend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dlg2D", "ProTracer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dlg2D", "Shot Stats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg2D = QtWidgets.QDialog()
    ui = Ui_dlg2D()
    ui.setupUi(dlg2D)
    dlg2D.show()
    sys.exit(app.exec_())

