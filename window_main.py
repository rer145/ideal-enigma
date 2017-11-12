# Load Libraries
import os
from PyQt5 import QtCore, QtGui, QtWidgets

# Load Resources
import resource_main

# Load Dialogs
import dialog_about
import dialog_protracer


class SplashWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 448))
        self.label.setObjectName("label")
        self.btnSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFile.setGeometry(QtCore.QRect(30, 470, 201, 51))
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.btnDemoFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnDemoFile.setGeometry(QtCore.QRect(30, 530, 201, 51))
        self.btnDemoFile.setObjectName("btnDemoFile")
        self.btnAbout = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbout.setGeometry(QtCore.QRect(570, 470, 201, 51))
        self.btnAbout.setObjectName("btnAbout")
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(570, 530, 201, 51))
        self.btnQuit.setObjectName("btnQuit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 470, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Wire up Event Handlers
        self.btnAbout.clicked.connect(self.show_about_dialog)
        self.btnQuit.clicked.connect(self.close_application)
        self.btnDemoFile.clicked.connect(self.load_demo_file)
        self.btnSelectFile.clicked.connect(self.select_file)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyProTracer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo/logo.jpg\"/></p></body></html>"))
        self.btnSelectFile.setText(_translate("MainWindow", "Select Data File"))
        self.btnDemoFile.setText(_translate("MainWindow", "Use Demo File"))
        self.btnAbout.setText(_translate("MainWindow", "About"))
        self.btnQuit.setText(_translate("MainWindow", "Quit"))
        self.label_2.setText(_translate("MainWindow", "PyProTracer"))


    # Event Handlers
    def show_about_dialog(self):
        qtAboutDialog = QtWidgets.QDialog()
        self.aboutDialog = dialog_about.AboutDialog()
        self.aboutDialog.setupUi(qtAboutDialog)
        qtAboutDialog.exec()

    def close_application(self):
        QtCore.QCoreApplication.quit()

    def load_demo_file(self):
        qtProTracerDialog = QtWidgets.QDialog()
        self.proTracerDialog = dialog_protracer.ProTracerDialog()
        self.proTracerDialog.setupUi(qtProTracerDialog)
        self.proTracerDialog.set_filename(os.getcwd() + '\\data\\traj-detail-2017771908.TXT')
        self.proTracerDialog.initialize()
        qtProTracerDialog.exec()

    def select_file(self):
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            QtWidgets.QWidget(), "QFileDialog.getOpenFileName()", "",
            "All Files (*);;CSV Files (*.csv);;Text Files (*.txt)", options=options)

        if filename:
            qtProTracerDialog = QtWidgets.QDialog()
            self.proTracerDialog = dialog_protracer.ProTracerDialog()
            self.proTracerDialog.setupUi(qtProTracerDialog)
            self.proTracerDialog.set_filename(filename)
            self.proTracerDialog.initialize()
            qtProTracerDialog.exec()


class MainWindowLauncher:
    def __init__(self):
        import sys

        app = QtWidgets.QApplication(sys.argv)
        app.setApplicationName('PyProTracer')

        MainWindow = QtWidgets.QMainWindow()
        main = SplashWindow()
        main.setupUi(MainWindow)
        MainWindow.show()

        sys.exit(app.exec_())
