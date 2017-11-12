from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import pt_data

class ProTracerDialog(object):
    def __init__(self):
        self.filename = ''
        self.data = pd.DataFrame()
        self.shot_list_model = None
        
    def setupUi(self, dlgProTracer):
        self.dialog = dlgProTracer
        dlgProTracer.setObjectName("dlgProTracer")
        dlgProTracer.resize(800, 600)
        self.label_2 = QtWidgets.QLabel(dlgProTracer)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label_2.setObjectName("label_2")
        self.ddlGolfer = QtWidgets.QComboBox(dlgProTracer)
        self.ddlGolfer.setGeometry(QtCore.QRect(160, 10, 211, 22))
        self.ddlGolfer.setObjectName("ddlGolfer")
        self.btnSearchShots = QtWidgets.QPushButton(dlgProTracer)
        self.btnSearchShots.setGeometry(QtCore.QRect(80, 80, 111, 31))
        self.btnSearchShots.setObjectName("btnSearchShots")
        self.label = QtWidgets.QLabel(dlgProTracer)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label.setObjectName("label")
        self.btnPlotShots = QtWidgets.QPushButton(dlgProTracer)
        self.btnPlotShots.setGeometry(QtCore.QRect(210, 80, 111, 31))
        self.btnPlotShots.setObjectName("btnPlotShots")
        self.ddlTournament = QtWidgets.QComboBox(dlgProTracer)
        self.ddlTournament.setGeometry(QtCore.QRect(160, 40, 211, 22))
        self.ddlTournament.setObjectName("ddlTournament")
        self.tabPlots = QtWidgets.QTabWidget(dlgProTracer)
        self.tabPlots.setGeometry(QtCore.QRect(10, 230, 781, 351))
        self.tabPlots.setObjectName("tabPlots")
        self.tabShotList = QtWidgets.QWidget()
        self.tabShotList.setObjectName("tabShotList")
        self.tblShotList = QtWidgets.QTreeView(self.tabShotList)
        self.tblShotList.setGeometry(QtCore.QRect(0, 0, 781, 331))
        self.tblShotList.setObjectName("tblShotList")
        self.tblShotList.setRootIsDecorated(True)
        self.tblShotList.setAlternatingRowColors(True)
        self.tabPlots.addTab(self.tabShotList, "")
        self.tabProTracer = QtWidgets.QWidget()
        self.tabProTracer.setObjectName("tabProTracer")
        self.gProTracer = QtWidgets.QGraphicsView(self.tabProTracer)
        self.gProTracer.setGeometry(QtCore.QRect(0, 0, 781, 331))
        self.gProTracer.setObjectName("gProTracer")
        self.tabPlots.addTab(self.tabProTracer, "")
        self.tabShotStats = QtWidgets.QWidget()
        self.tabShotStats.setObjectName("tabShotStats")
        self.tabPlots.addTab(self.tabShotStats, "")

        self.retranslateUi(dlgProTracer)
        self.tabPlots.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlgProTracer)

        # Wire up event handlers
        self.btnSearchShots.clicked.connect(self.search_shots)
        # self.ddlGolfer.currentTextChanged.connect(self.on_golfer_changed)
        # self.ddlTournament.currentTextChanged.connect(self.on_tournament_changed)

    def retranslateUi(self, dlgProTracer):
        _translate = QtCore.QCoreApplication.translate
        dlgProTracer.setWindowTitle(_translate("dlgProTracer", "PyProTracer"))
        self.label_2.setText(_translate("dlgProTracer", "Choose a Tournament:"))
        self.btnSearchShots.setText(_translate("dlgProTracer", "List Shots"))
        self.label.setText(_translate("dlgProTracer", "Choose a Golfer:"))
        self.btnPlotShots.setText(_translate("dlgProTracer", "Start ProTracer"))
        self.tabPlots.setTabText(self.tabPlots.indexOf(self.tabShotList), _translate("dlgProTracer", "Shot List"))
        self.tabPlots.setTabText(self.tabPlots.indexOf(self.tabProTracer), _translate("dlgProTracer", "ProTracer"))
        self.tabPlots.setTabText(self.tabPlots.indexOf(self.tabShotStats), _translate("dlgProTracer", "Shot Stats"))
        
    # Custom Methods/Properties
    def set_filename(self, filename):
        # check if file exists?
        self.filename = filename

    def initialize(self):
        self.shot_list_model = self.create_shots_list_model()
        self.tblShotList.setModel(self.shot_list_model)

        if len(self.filename) > 0:
            self.data = pt_data.load_file(self.filename)
            self.populate_golfers()
            self.populate_tournaments()

    def populate_golfers(self, tournament=''):
        if len(tournament) > 0:
            golfers = pt_data.get_golfers_by_tournament(self.data, tournament)
        else:
            golfers = pt_data.get_all_golfers(self.data)

        self.ddlGolfer.clear()
        self.ddlGolfer.addItem("")
        self.ddlGolfer.addItems(golfers)

    def populate_tournaments(self, golfer=''):
        if len(golfer) > 0:
            tournaments = pt_data.get_tournaments_by_golfer(golfer)
        else:
            tournaments = pt_data.get_all_tournaments(self.data)

        self.ddlTournament.clear()
        self.ddlTournament.addItem("")
        self.ddlTournament.addItems(tournaments)

    def populate_shots_list(self, df):
        for i in range(len(df)):
            self.add_shot_to_list(self.shot_list_model, df.iloc[i])

    def create_shots_list_model(self):
        model = QtGui.QStandardItemModel(0, 7, self.tblShotList)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Round")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Hole #")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Carry Distance (yds)")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Total Distance (yds)")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Apex (ft)")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Club Speed (mph)")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Ball Speed (mph)")
        return model

    def search_shots(self):
        golfer = self.ddlGolfer.currentText()
        tournament = self.ddlTournament.currentText()

        if len(golfer) > 0 and len(tournament) > 0:
            shots = pt_data.get_shots_by_golfer_tournament(self.data, golfer, tournament)
            if len(shots) > 0:
                self.populate_shots_list(shots)
            else:
                QtWidgets.QMessageBox.information(
                    QtWidgets.QWidget(), 'Shot Search Results',
                    'There were no shots found in the data file for {0} at {1}'.format(
                        golfer, tournament
                    ))
        else:
            QtWidgets.QMessageBox.information(
                QtWidgets.QWidget(), 'Shot Search Error',
                'You need to select both a golfer and tournament before continuing.')

    def add_shot_to_list(self, model, shot):
        model.insertRow(0)
        model.setData(model.index(0, 0), shot["Round"])
        model.setData(model.index(0, 1), shot["Hole Number"])
        model.setData(model.index(0, 2), round(shot["Distance of Impact"] * 0.27778, 1))
        model.setData(model.index(0, 3), round(shot["Total Distance"] * 0.27778, 1))
        model.setData(model.index(0, 4), round(shot["Apex Height"], 1))
        model.setData(model.index(0, 5), round(shot["Club Head Speed"], 1))
        model.setData(model.index(0, 6), round(shot["Ball Speed"], 1))

    def on_golfer_changed(self, golfer):
        self.populate_tournaments(golfer)

    def on_tournament_changed(self, tournament):
        self.populate_golfers(tournament)



    # on select of golfer or tournament, populate the other box
