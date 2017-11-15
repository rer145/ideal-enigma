# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/protracer3d.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg3D(object):
    def setupUi(self, dlg3D):
        dlg3D.setObjectName("dlg3D")
        dlg3D.resize(800, 800)

        self.retranslateUi(dlg3D)
        QtCore.QMetaObject.connectSlotsByName(dlg3D)

    def retranslateUi(self, dlg3D):
        _translate = QtCore.QCoreApplication.translate
        dlg3D.setWindowTitle(_translate("dlg3D", "PyProTracer 3D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg3D = QtWidgets.QDialog()
    ui = Ui_dlg3D()
    ui.setupUi(dlg3D)
    dlg3D.show()
    sys.exit(app.exec_())

