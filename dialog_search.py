from PyQt5 import QtCore, QtGui, QtWidgets

import os
import pandas as pd
import pt_data

import dialog_protracer2d


class SearchDialog(object):
    def __init__(self):
        self.filename = ''
        self.data = pd.DataFrame()

    def setupUi(self, dlgSearch):
        self.dialog = dlgSearch

        dlgSearch.setObjectName("dlgSearch")
        dlgSearch.resize(800, 600)
        dlgSearch.setSizeGripEnabled(False)
        dlgSearch.setModal(True)
        self.groupBox = QtWidgets.QGroupBox(dlgSearch)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 241))
        self.groupBox.setObjectName("groupBox")
        self.btnAddShots = QtWidgets.QPushButton(self.groupBox)
        self.btnAddShots.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.btnAddShots.setObjectName("btnAddShots")
        self.tblShotList = QtWidgets.QTreeWidget(self.groupBox)
        self.tblShotList.setGeometry(QtCore.QRect(10, 20, 751, 171))
        self.tblShotList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblShotList.setProperty("showDropIndicator", False)
        self.tblShotList.setAlternatingRowColors(True)
        self.tblShotList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tblShotList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblShotList.setColumnCount(9)
        self.tblShotList.setObjectName("tblShotList")
        self.tblShotList.AdjustToContentsOnFirstShow = True
        self.tblShotList.setUpdatesEnabled(True)
        self.tblShotList.setColumnHidden(8, True)
        self.groupBox_3 = QtWidgets.QGroupBox(dlgSearch)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 280, 771, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnRemoveShots = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRemoveShots.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.btnRemoveShots.setObjectName("btnRemoveShots")
        self.tblSelectedShots = QtWidgets.QTreeWidget(self.groupBox_3)
        self.tblSelectedShots.setGeometry(QtCore.QRect(10, 20, 751, 171))
        self.tblSelectedShots.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSelectedShots.setProperty("showDropIndicator", False)
        self.tblSelectedShots.setAlternatingRowColors(True)
        self.tblSelectedShots.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tblSelectedShots.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblSelectedShots.setColumnCount(9)
        self.tblSelectedShots.setObjectName("tblSelectedShots")
        self.tblSelectedShots.AdjustToContentsOnFirstShow = True
        self.tblSelectedShots.setUpdatesEnabled(True)
        self.tblSelectedShots.setColumnHidden(8, True)
        self.btn2D = QtWidgets.QPushButton(dlgSearch)
        self.btn2D.setGeometry(QtCore.QRect(210, 540, 181, 41))
        self.btn2D.setObjectName("btn2D")
        self.btn3D = QtWidgets.QPushButton(dlgSearch)
        self.btn3D.setGeometry(QtCore.QRect(420, 540, 181, 41))
        self.btn3D.setObjectName("btn3D")

        self.retranslateUi(dlgSearch)
        QtCore.QMetaObject.connectSlotsByName(dlgSearch)

        # Wire up event handlers
        self.btnAddShots.clicked.connect(self.on_add_shots)
        self.btnRemoveShots.clicked.connect(self.on_remove_shots)
        self.btn2D.clicked.connect(self.on_plot_2d)
        self.btn3D.clicked.connect(self.on_plot_3d)

    def retranslateUi(self, dlgSearch):
        _translate = QtCore.QCoreApplication.translate
        dlgSearch.setWindowTitle(_translate("dlgSearch", "PyProTracer Shot Search"))
        self.groupBox.setTitle(_translate("dlgSearch", "Shot List"))
        self.btnAddShots.setText(_translate("dlgSearch", "Add Selected Shots"))
        self.tblShotList.setSortingEnabled(True)
        self.tblShotList.headerItem().setText(0, _translate("dlgSearch", "Player"))
        self.tblShotList.headerItem().setText(1, _translate("dlgSearch", "Tournament"))
        self.tblShotList.headerItem().setText(2, _translate("dlgSearch", "Round"))
        self.tblShotList.headerItem().setText(3, _translate("dlgSearch", "Hole"))
        self.tblShotList.headerItem().setText(4, _translate("dlgSearch", "Distance (yds)"))
        self.tblShotList.headerItem().setText(5, _translate("dlgSearch", "Apex (ft)"))
        self.tblShotList.headerItem().setText(6, _translate("dlgSearch", "Club Speed (mph)"))
        self.tblShotList.headerItem().setText(7, _translate("dlgSearch", "Ball Speed (mph)"))
        self.tblSelectedShots.headerItem().setText(0, _translate("dlgSearch", "Player"))
        self.tblSelectedShots.headerItem().setText(1, _translate("dlgSearch", "Tournament"))
        self.tblSelectedShots.headerItem().setText(2, _translate("dlgSearch", "Round"))
        self.tblSelectedShots.headerItem().setText(3, _translate("dlgSearch", "Hole"))
        self.tblSelectedShots.headerItem().setText(4, _translate("dlgSearch", "Distance (yds)"))
        self.tblSelectedShots.headerItem().setText(5, _translate("dlgSearch", "Apex (ft)"))
        self.tblSelectedShots.headerItem().setText(6, _translate("dlgSearch", "Club Speed (mph)"))
        self.tblSelectedShots.headerItem().setText(7, _translate("dlgSearch", "Ball Speed (mph)"))
        self.groupBox_3.setTitle(_translate("dlgSearch", "Selected Shots"))
        self.btnRemoveShots.setText(_translate("dlgSearch", "Remove Selected Shots"))
        self.tblSelectedShots.setSortingEnabled(True)
        self.btn2D.setText(_translate("dlgSearch", "ProTracer 2D"))
        self.btn3D.setText(_translate("dlgSearch", "ProTracer 3D"))

    def set_filename(self, filename):
        self.filename = filename

    def initialize(self):
        if len(self.filename) > 0:
            if os.path.isfile(self.filename):
                self.data = pt_data.load_file(self.filename)
                self.populate_shot_list()
            else:
                QtWidgets.QMessageBox.information(
                    QtWidgets.QWidget(), 'Error Loading Data File',
                    'The data file ({0}) could not be found. Please choose another file'.format(self.filename))
                self.dialog.done(0)
        else:
            QtWidgets.QMessageBox.information(
                QtWidgets.QWidget(), 'Error Loading Data File',
                'No file was specified. Please select a file and try again.')
            self.dialog.done(0)

    def populate_shot_list(self):
        shots = pt_data.get_all_shots(self.data)
        tree_items = []
        for i in range(len(shots)):
            shot = shots.iloc[i]
            item = [
                str(shot["Player Last First"]),
                str(shot["Tournament Name"]),
                str(shot["Round"]),
                str(shot["Hole Number"]),
                str(round((shot["Total Distance"] / 12) / 3, 1)),
                str(round(shot["Apex Height"], 1)),
                str(round(shot["Club Head Speed"], 1)),
                str(round(shot["Ball Speed"], 1)),
                str(shot["Index"])
            ]
            tree_items.append(QtWidgets.QTreeWidgetItem(item))
        self.tblShotList.addTopLevelItems(tree_items)

    def on_add_shots(self):
        items = self.tblShotList.selectedItems()

        for item in items:
            self.tblSelectedShots.addTopLevelItem(item.clone())
            self.tblShotList.takeTopLevelItem(self.tblShotList.indexOfTopLevelItem(item))

        self.tblShotList.clearSelection()

    def on_remove_shots(self):
        items = self.tblSelectedShots.selectedItems()

        for item in items:
            self.tblShotList.addTopLevelItem(item.clone())
            self.tblSelectedShots.takeTopLevelItem(self.tblSelectedShots.indexOfTopLevelItem(item))

    def get_chosen_shots(self):
        shots = []
        for i in range(self.tblSelectedShots.topLevelItemCount()):
            shot = {
                'Player Last First': self.tblSelectedShots.topLevelItem(i).data(0, 0),
                'Tournament Name': self.tblSelectedShots.topLevelItem(i).data(1, 0),
                'Round': self.tblSelectedShots.topLevelItem(i).data(2, 0),
                'Hole Number': self.tblSelectedShots.topLevelItem(i).data(3, 0)
            }
            shots.append(shot)
        return shots

    def on_plot_2d(self):
        qtDialog = QtWidgets.QDialog()
        self.protracerDialog = dialog_protracer2d.ProTracer2DDialog()
        self.protracerDialog.setupUi(qtDialog)
        self.protracerDialog.set_shot_data(self.get_chosen_shots())
        self.protracerDialog.initialize()
        qtDialog.exec()

    def on_plot_3d(self):
        # TODO: close dialog and open new dialog with plot, passing selected shots
        #qtDialog = QtWidgets.QDialog()
        #self.protracerDialog = dialog_protracer3d.ProTracer3DDialog()
        #self.protracerDialog.setupUi(qtDialog)
        #self.protracerDialog.set_shot_data(self.get_chosen_shots())
        #self.protracerDialog.initialize()
        #qtDialog.exec()
        return None
