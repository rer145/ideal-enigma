from PyQt5 import QtCore, QtGui, QtWidgets

import os
import pandas as pd
import pt_data
import pt_plot

import widget_mpl


class SearchDialog(object):
    def __init__(self):
        self.filename = ''
        self.data = pd.DataFrame()
        self.pt = pt_plot.ProTracerPlot()

    def setupUi(self, dlgSearch):
        self.dialog = dlgSearch

        dlgSearch.setObjectName("dlgSearch")
        dlgSearch.resize(800, 600)
        dlgSearch.setSizeGripEnabled(False)
        # dlgSearch.setModal(True)
        
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
        dlgSearch.setWindowTitle(_translate("dlgSearch", "ProTracer Shot Search"))
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

    def add_shots_to_plot(self):
        shots = []
        for shot in self.get_chosen_shots():
            shot_data = pt_data.get_shot(self.data, shot["Player Last First"], shot["Tournament Name"],
                                         shot["Round"], shot["Hole Number"])

            # shot summary
            summary = {}
            summary["Player First Name"] = shot_data.iloc[0]["Player First Name"]
            summary["Player Last Name"] = shot_data.iloc[0]["Player Last Name"]
            summary["Player Full Name"] = shot_data.iloc[0]["Player Full Name"]
            summary["Tournament Name"] = shot_data.iloc[0]["Tournament Name"]
            summary["Round"] = shot_data.iloc[0]["Round"]
            summary["Hole Number"] = shot_data.iloc[0]["Hole Number"]
            summary["Club Head Speed"] = shot_data.iloc[0]["Club Head Speed"]
            summary["Ball Speed"] = shot_data.iloc[0]["Ball Speed"]
            summary["Smash Factor"] = shot_data.iloc[0]["Smash Factor"]
            summary["Vertical Launch Angle"] = shot_data.iloc[0]["Vertical Launch Angle"]
            summary["Apex Height"] = shot_data.iloc[0]["Apex Height"]
            summary["Actual Flight Time"] = shot_data.iloc[0]["Actual Flight Time"]
            summary["Actual Range"] = shot_data.iloc[0]["Actual Range"]
            summary["Actual Height"] = shot_data.iloc[0]["Actual Height"]
            summary["Distance of Impact"] = shot_data.iloc[0]["Distance of Impact"]
            summary["Club"] = shot_data.iloc[0]["Club"]
            summary["Total Distance"] = shot_data.iloc[0]["Total Distance"]
            summary["Ending Location Description"] = shot_data.iloc[0]["Ending Location Description"]
            summary["Weather"] = shot_data.iloc[0]["Weather"]

            shots.append((shot_data, summary))

        return shots

    def on_plot_2d(self):
        # self.move_search_dialog()
        self.dialog.setGeometry(0, 100, self.dialog.width(), self.dialog.height())
        self.ptdialog = widget_mpl.ProTracerDialog()
        self.ptdialog.set_plot_data(self.add_shots_to_plot())
        self.ptdialog.on_draw_2d()
        self.ptdialog.exec()

    def on_plot_3d(self):
        self.dialog.setGeometry(0, 100, self.dialog.width(), self.dialog.height())
        self.ptdialog = widget_mpl.ProTracerDialog()
        self.ptdialog.set_plot_data(self.add_shots_to_plot())
        self.ptdialog.on_draw_3d()
        self.ptdialog.exec()
