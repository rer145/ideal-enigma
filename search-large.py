# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/search.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgSearch(object):
    def setupUi(self, dlgSearch):
        dlgSearch.setObjectName("dlgSearch")
        dlgSearch.resize(1200, 800)
        dlgSearch.setSizeGripEnabled(False)
        dlgSearch.setModal(True)
        self.groupBox = QtWidgets.QGroupBox(dlgSearch)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1171, 351))
        self.groupBox.setObjectName("groupBox")
        self.btnAddShots = QtWidgets.QPushButton(self.groupBox)
        self.btnAddShots.setGeometry(QtCore.QRect(10, 310, 141, 31))
        self.btnAddShots.setObjectName("btnAddShots")
        self.tblShotList = QtWidgets.QTreeWidget(self.groupBox)
        self.tblShotList.setGeometry(QtCore.QRect(10, 20, 1151, 281))
        self.tblShotList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblShotList.setProperty("showDropIndicator", False)
        self.tblShotList.setAlternatingRowColors(True)
        self.tblShotList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tblShotList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblShotList.setColumnCount(7)
        self.tblShotList.setObjectName("tblShotList")
        self.tblShotList.headerItem().setText(2, "Round # / Hole #")
        self.groupBox_3 = QtWidgets.QGroupBox(dlgSearch)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 1171, 351))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnRemoveShots = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRemoveShots.setGeometry(QtCore.QRect(10, 310, 141, 31))
        self.btnRemoveShots.setObjectName("btnRemoveShots")
        self.tblSelectedShots = QtWidgets.QTreeWidget(self.groupBox_3)
        self.tblSelectedShots.setGeometry(QtCore.QRect(10, 20, 1151, 281))
        self.tblSelectedShots.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSelectedShots.setProperty("showDropIndicator", False)
        self.tblSelectedShots.setAlternatingRowColors(True)
        self.tblSelectedShots.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tblSelectedShots.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblSelectedShots.setColumnCount(7)
        self.tblSelectedShots.setObjectName("tblSelectedShots")
        self.tblSelectedShots.headerItem().setText(1, "Tournament")
        self.tblSelectedShots.headerItem().setText(2, "Round # / Hole #")
        self.tblSelectedShots.headerItem().setText(3, "Distance (yds)")
        self.tblSelectedShots.headerItem().setText(4, "Club Speed (mph)")
        self.tblSelectedShots.headerItem().setText(5, "Ball Speed (mph)")
        self.tblSelectedShots.headerItem().setText(6, "Launch Angle (deg)")
        self.btn2D = QtWidgets.QPushButton(dlgSearch)
        self.btn2D.setGeometry(QtCore.QRect(410, 740, 181, 41))
        self.btn2D.setObjectName("btn2D")
        self.btn3D = QtWidgets.QPushButton(dlgSearch)
        self.btn3D.setGeometry(QtCore.QRect(620, 740, 181, 41))
        self.btn3D.setObjectName("btn3D")

        self.retranslateUi(dlgSearch)
        QtCore.QMetaObject.connectSlotsByName(dlgSearch)

    def retranslateUi(self, dlgSearch):
        _translate = QtCore.QCoreApplication.translate
        dlgSearch.setWindowTitle(_translate("dlgSearch", "PyProTracer Shot Search"))
        self.groupBox.setTitle(_translate("dlgSearch", "Shot List"))
        self.btnAddShots.setText(_translate("dlgSearch", "Add Selected Shots"))
        self.tblShotList.setSortingEnabled(True)
        self.tblShotList.headerItem().setText(0, _translate("dlgSearch", "Player"))
        self.tblShotList.headerItem().setText(1, _translate("dlgSearch", "Tournament"))
        self.tblShotList.headerItem().setText(3, _translate("dlgSearch", "Distance (yds)"))
        self.tblShotList.headerItem().setText(4, _translate("dlgSearch", "Club Speed (mph)"))
        self.tblShotList.headerItem().setText(5, _translate("dlgSearch", "Ball Speed (mph)"))
        self.tblShotList.headerItem().setText(6, _translate("dlgSearch", "Launch Angle (deg)"))
        self.groupBox_3.setTitle(_translate("dlgSearch", "Selected Shots"))
        self.btnRemoveShots.setText(_translate("dlgSearch", "Remove Selected Shots"))
        self.tblSelectedShots.setSortingEnabled(True)
        self.tblSelectedShots.headerItem().setText(0, _translate("dlgSearch", "Player"))
        self.btn2D.setText(_translate("dlgSearch", "ProTracer 2D"))
        self.btn3D.setText(_translate("dlgSearch", "ProTracer 3D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgSearch = QtWidgets.QDialog()
    ui = Ui_dlgSearch()
    ui.setupUi(dlgSearch)
    dlgSearch.show()
    sys.exit(app.exec_())

