# http://scipy-cookbook.readthedocs.io/items/Matplotlib_Qt_with_IPython_and_Designer.html
# https://github.com/eliben/code-for-blog/blob/master/2009/qt_mpl_bars.py

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pt_plot

class ProTracerDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("ProTracer")
        self.resize(800, 600)
        self.create_plot_widget()

        self.padding = 25.0
        self.linewidth = 8
        self.interval = 50
        self.aspect_size = 3
        self.aspect_ratio = 0.0

        self.data = []
        self.labels = []
        self.extrapolated = []
        self.lines = []

        self.xmax = -1
        self.ymax = -1
        self.zmax = -1

    def create_plot_widget(self):
        self.plot_widget = QtWidgets.QWidget()
        self.plot_widget.setObjectName("widget")

        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.ax = self.fig.add_subplot(111)
        self.canvas.mpl_connect('pick_event', self.on_pick)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.plot_widget)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)

        self.plot_widget.setLayout(vbox)
        # self.setCentralWidget(self.plot_widget)

        QtCore.QMetaObject.connectSlotsByName(self)

    def on_pick(self, event):
        return None

    def set_plot_data(self, shots):
        self.shots = shots

    def on_draw_2d(self):
        for i in range(len(self.shots)):
            self.add_plot_data(self.shots[i][0], self.shots[i][1])

        self.ax.clear()
        self.plot_2d()


    def adjust_coordinates(self, L):
        output = []
        minval = min(L)

        for item in L:
            output.append(item - minval)

        return output

    def add_plot_data(self, shot_data, shot_summary):
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

        x = self.adjust_coordinates(x)
        y = self.adjust_coordinates(y)
        z = self.adjust_coordinates(z)

        self.xmax = max(self.xmax, max(x))
        self.ymax = max(self.ymax, max(y))
        self.zmax = max(self.zmax, max(z))

        self.data.append(np.array((x, y, z)))
        self.labels.append(shot_summary)
        self.extrapolated.append(extrapolated)

    def init_2d(self):
        for i in range(len(self.data)):
            self.lines[i].set_data([], [])
        return self.lines

    def update_2d_lines(self, num, datas, lines):
        for i in range(len(datas)):
            self.lines[i].set_data(datas[i][0, :num], datas[i][2, :num])
        return self.lines

    def plot_2d(self):
        self.xmax += self.padding
        self.ymax += self.padding
        self.zmax += self.padding
        self.aspect_ratio = self.xmax // float(self.zmax)

        self.fig = plt.figure(figsize=(self.aspect_ratio * self.aspect_size, self.aspect_size))
        self.ax = plt.axes(xlim=(0, self.xmax), ylim=(0, self.zmax))
        self.ax.set_title("ProTracer 2D")

        for i in range(len(self.data)):
            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])
            self.lines.append(self.ax.plot(self.data[i][0, 0:1], self.data[i][2, 0:1], linewidth=self.linewidth, label=label)[0])

        ani = animation.FuncAnimation(self.fig, self.update_2d_lines, fargs=(self.data, self.lines),
                                      interval=self.interval, blit=False, repeat=False, init_func=self.init_2d)

        handles, labels = self.ax.get_legend_handles_labels()
        self.ax.legend(handles, labels)
        # plt.axis('off')
        plt.show()
        # self.canvas.draw()
