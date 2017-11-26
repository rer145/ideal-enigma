from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os
import pt_data
import pt_plot
import widget_mpl

class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SearchWindow, self).__init__(parent)
        self.filename = ''
        self.data = pd.DataFrame()
        self.pt = pt_plot.ProTracerPlot()

    def setupUi(self, windowSearch):
        windowSearch.setObjectName("windowSearch")
        windowSearch.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(windowSearch)
        self.centralwidget.setObjectName("centralwidget")
        self.btn3D = QtWidgets.QPushButton(self.centralwidget)
        self.btn3D.setGeometry(QtCore.QRect(420, 520, 141, 31))
        self.btn3D.setObjectName("btn3D")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 254, 782, 238))
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
        self.tblSelectedShots.setColumnCount(7)
        self.tblSelectedShots.setObjectName("tblSelectedShots")
        self.tblSelectedShots.headerItem().setText(1, "Tournament")
        self.tblSelectedShots.headerItem().setText(2, "Round # / Hole #")
        self.tblSelectedShots.headerItem().setText(3, "Distance (yds)")
        self.tblSelectedShots.headerItem().setText(4, "Club Speed (mph)")
        self.tblSelectedShots.headerItem().setText(5, "Ball Speed (mph)")
        self.tblSelectedShots.headerItem().setText(6, "Launch Angle (deg)")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 782, 239))
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
        self.tblShotList.setColumnCount(7)
        self.tblShotList.setObjectName("tblShotList")
        self.tblShotList.headerItem().setText(2, "Round # / Hole #")
        self.btn2D = QtWidgets.QPushButton(self.centralwidget)
        self.btn2D.setGeometry(QtCore.QRect(210, 520, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2D.sizePolicy().hasHeightForWidth())
        self.btn2D.setSizePolicy(sizePolicy)
        self.btn2D.setObjectName("btn2D")
        windowSearch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowSearch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        windowSearch.setMenuBar(self.menubar)
        self.actionLoad_Demo_File = QtWidgets.QAction(windowSearch)
        self.actionLoad_Demo_File.setObjectName("actionLoad_Demo_File")
        self.actionOpen_Data_File = QtWidgets.QAction(windowSearch)
        self.actionOpen_Data_File.setObjectName("actionOpen_Data_File")
        self.actionAbout = QtWidgets.QAction(windowSearch)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(windowSearch)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_Demo_File)
        self.menuFile.addAction(self.actionOpen_Data_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(windowSearch)
        QtCore.QMetaObject.connectSlotsByName(windowSearch)

        # Wire up event handlers
        self.btnAddShots.clicked.connect(self.on_add_shots)
        self.btnRemoveShots.clicked.connect(self.on_remove_shots)
        self.btn2D.clicked.connect(self.on_plot_2d)
        self.btn3D.clicked.connect(self.on_plot_3d)

    def retranslateUi(self, windowSearch):
        _translate = QtCore.QCoreApplication.translate
        windowSearch.setWindowTitle(_translate("windowSearch", "ProTracer Shot Search"))
        self.btn3D.setText(_translate("windowSearch", "ProTracer 3D"))
        self.groupBox_3.setTitle(_translate("windowSearch", "Selected Shots"))
        self.btnRemoveShots.setText(_translate("windowSearch", "Remove Selected Shots"))
        self.tblSelectedShots.setSortingEnabled(True)
        self.tblSelectedShots.headerItem().setText(0, _translate("windowSearch", "Player"))
        self.groupBox.setTitle(_translate("windowSearch", "Shot List"))
        self.btnAddShots.setText(_translate("windowSearch", "Add Selected Shots"))
        self.tblShotList.setSortingEnabled(True)
        self.tblShotList.headerItem().setText(0, _translate("windowSearch", "Player"))
        self.tblShotList.headerItem().setText(1, _translate("windowSearch", "Tournament"))
        self.tblShotList.headerItem().setText(3, _translate("windowSearch", "Distance (yds)"))
        self.tblShotList.headerItem().setText(4, _translate("windowSearch", "Club Speed (mph)"))
        self.tblShotList.headerItem().setText(5, _translate("windowSearch", "Ball Speed (mph)"))
        self.tblShotList.headerItem().setText(6, _translate("windowSearch", "Launch Angle (deg)"))
        self.btn2D.setText(_translate("windowSearch", "ProTracer 2D"))
        self.menuFile.setTitle(_translate("windowSearch", "File"))
        self.menuHelp.setTitle(_translate("windowSearch", "Help"))
        self.actionLoad_Demo_File.setText(_translate("windowSearch", "Load Demo File"))
        self.actionOpen_Data_File.setText(_translate("windowSearch", "Open Data File"))
        self.actionAbout.setText(_translate("windowSearch", "About"))
        self.actionExit.setText(_translate("windowSearch", "Exit"))

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
        self.ptdialog = widget_mpl.ProTracerDialog()
        self.ptdialog.set_plot_data(self.add_shots_to_plot())
        self.ptdialog.on_draw_2d()
        self.ptdialog.exec()

        #self.move_search_window(True)
        #self.pt.plot_2d()

        # qtdialog = QtWidgets.QDialog()
        # self.protracerDialog = widget_mpl.ProTracerDialog()
        # self.protracerDialog.setupUi(qtdialog)
        # self.protracerDialog.set_protracer(self.pt)
        # self.protracerDialog.plot()
        # qtdialog.exec()

    def on_plot_3d(self):
        self.add_shots_to_plot()
        self.move_search_window(False)
        self.pt.plot_3d()

    def move_search_window(self, is_2d):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        widget = self.dialog.geometry()

        if is_2d:
            # Center horizontally and at the top of the screen
            x = (screen.width() - widget.width()) / 2
            y = 0
        else:
            # Centered vertically and to the left of the screen
            x = 0
            y = (screen.height() - widget.height()) / 2

        self.dialog.move(x, y)
