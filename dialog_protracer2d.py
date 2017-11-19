from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import numpy as np
import pt_data
import pt_plot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

matplotlib.use('QT5Agg')

# from: https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)


class ProTracer2DDialog(object):
    def __init__(self):
        self.shots = []
        self.data = pd.DataFrame()

        self.padding = 25.0
        self.aspect_ratio = 0.0
        self.aspect_size = 3
        self.linewidth = 8
        self.interval = 50

        self.plot_data_xmax = -1
        self.plot_data_ymax = -1
        self.plot_data_zmax = -1

        self.plot_data = []
        self.line_data = []
        self.plot_labels = []

        self.figure = Figure()

    def setupUi(self, dlg2D):
        self.dialog = dlg2D

        dlg2D.setObjectName("dlg2D")
        dlg2D.resize(800, 600)
        dlg2D.setSizeGripEnabled(False)
        dlg2D.setModal(True)

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

        # self.w_plot = QtWidgets.QWidget(self.widget)
        self.w_plot = FigureCanvas(self.figure)
        self.w_plot.setGeometry(QtCore.QRect(10, 10, 761, 391))
        self.w_plot.setObjectName("w_plot")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(dlg2D)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlg2D)

        # Wire up event handlers

    def retranslateUi(self, dlg2D):
        _translate = QtCore.QCoreApplication.translate
        dlg2D.setWindowTitle(_translate("dlg2D", "PyProTracer 2D"))
        self.groupBox.setTitle(_translate("dlg2D", "Legend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dlg2D", "ProTracer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dlg2D", "Shot Stats"))

    def set_shot_data(self, data):
        self.data = data

    def set_selected_shots(self, data):
        self.shots = data

    def initialize(self):
        if len(self.shots) > 0:
            self.plot_it()
        else:
            QtWidgets.QMessageBox.information(
                QtWidgets.QWidget(), 'Error Displaying ProTracer', 'There are no shots selected to show.')
            self.dialog.done(0)

    def adjust_coordinates(self, L):
        output = []
        minval = min(L)

        for item in L:
            output.append(item - minval)

        return output

    def update_lines_multi(self, num, datas, lines):
        for i in list(range(len(datas))):
            lines[i].set_data(datas[i][0:2, :num])
        return lines

    def plot_setup(self):
        for shot in self.shots:
            shot_data = pt_data.get_shot(self.data, shot["Player Last First"], shot["Tournament Name"],
                                         shot["Round"], shot["Hole Number"])

            x = shot_data.loc[
                (shot_data['Extrapolated'] == 'N')
            ]["Trajectory X Coordinate"].tolist()

            y = shot_data.loc[
                (shot_data['Extrapolated'] == 'N')
            ]["Trajectory Y Coordinate"].tolist()

            z = shot_data.loc[
                (shot_data['Extrapolated'] == 'N')
            ]["Trajectory Z Coordinate"].tolist()

            # Unnecessary at this point
            extrapolated = shot_data.loc[
                (shot_data['Extrapolated'] == 'N')
            ]["Extrapolated"].tolist()

            # Adjust coordinates to all have same relative starting point
            x = self.adjust_coordinates(x)
            y = self.adjust_coordinates(y)
            z = self.adjust_coordinates(z)

            self.plot_data_xmax = max(self.plot_data_xmax, max(x))
            self.plot_data_ymax = max(self.plot_data_ymax, max(y))
            self.plot_data_zmax = max(self.plot_data_zmax, max(z))

            self.plot_data.append(np.array((x, z, extrapolated)))

    def plot_initialize(self):
        for i in range(len(self.plot_data)):
            self.line_data[i].set_data([], [])
        return self.line_data

    def plot_it(self):
        # add to dialog_search
        pt = pt_plot.ProTracerPlot()

        for shot in self.shots:
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

            pt.add_plot_data(shot_data, summary)

        self.dialog.destroy(0)
        pt.plot_2d()

    def plot_it2(self):
        self.plot_setup()

        self.plot_data_xmax += self.padding
        self.plot_data_ymax += self.padding
        self.plot_data_zmax += self.padding

        self.aspect_ratio = self.plot_data_xmax // float(self.plot_data_xmax)

        self.figure = Figure(figsize=(self.aspect_ratio * self.aspect_size, self.aspect_size))
        #ax = self.figure.add_axes(xlim=(0, self.plot_data_xmax), ylim=(0, self.plot_data_zmax))
        ax = self.figure.add_axes([0, 0, self.plot_data_xmax, self.plot_data_zmax])

        for i in range(len(self.plot_data)):
            #label = '{0} - Round {1}'.format(
            #    self.plot_labels[i]["Player Last Name"],
            #    self.plot_labels[i]["Round"])
            label = '{0} - Round {1}'
            self.line_data.append(self.figure.add_subplot(self.plot_data[i][0, 0:1], self.plot_data[i][1, 0:1],
                                                             linewidth=self.linewidth, label=label)[0])

        ani = animation.FuncAnimation(self.figure, self.update_lines_multi,
                                      fargs=(self.plot_data, self.line_data), interval=self.interval, blit=False,
                                      repeat=False, init_func=self.plot_initialize)

        handles, labels = self.w_plot.ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        # self.figure.axis('off')
        # plt.show()
        #self.w_plot.draw()
        self.figure.draw()
