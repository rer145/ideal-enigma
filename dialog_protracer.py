from PyQt5 import QtCore, QtGui, QtWidgets

# Import Resource Module

class ProTracerDialog(object):
    def __init__(self):
        self.filename = ''
        
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
        self.tblShotList = QtWidgets.QTableView(self.tabShotList)
        self.tblShotList.setGeometry(QtCore.QRect(0, 0, 781, 331))
        self.tblShotList.setObjectName("tblShotList")
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
        self.filename = filename
        #_translate = QtCore.QCoreApplication.translate
        #self.lblFileName.setText(_translate("dlgProTracer", filename))
        #self.lblFileNameProp.setText(_translate("dlgProTracer", self.filename))
    


    # Event Handlers
    
