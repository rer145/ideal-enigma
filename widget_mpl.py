# http://scipy-cookbook.readthedocs.io/items/Matplotlib_Qt_with_IPython_and_Designer.html
# https://github.com/eliben/code-for-blog/blob/master/2009/qt_mpl_bars.py
# https://pythonspot.com/en/pyqt5-matplotlib/
# https://stackoverflow.com/questions/3972158/how-to-plot-on-my-gui

# https://stackoverflow.com/questions/29357442/example-of-embedding-matplotlib-in-pyqt5
# 3d toolbar options not supported

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import matplotlib
matplotlib.use('QT5Agg')

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class ProTracerDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("ProTracer")
        self.resize(800, 600)

        screen = QtWidgets.QDesktopWidget().availableGeometry()
        self.setGeometry(screen.width() - self.width(), 100, self.width(), self.height())

        self.canvas = PlotCanvas(self, width=8, height=6)

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

    def set_plot_data(self, shots):
        self.data = []
        self.shots = shots

    def on_draw_2d(self):
        # set up toolbar for 2D only
        self.canvas.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.canvas.toolbar.update()

        for i in range(len(self.shots)):
            self.add_plot_data(self.shots[i][0], self.shots[i][1], True)

        self.plot_2d()

    def on_draw_3d(self):
        for i in range(len(self.shots)):
            self.add_plot_data(self.shots[i][0], self.shots[i][1], False)

        self.plot_3d()

    def adjust_coordinates(self, L, is2D = True):
        # assumes first value is lowest for plot
        output = []
        if is2D:
            minval = L[0]
        else:
            minval = min(L)

        for item in L:
            output.append(item - minval)

        return output

    def add_plot_data(self, shot_data, shot_summary, is2D=True):
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

        x = self.adjust_coordinates(x, is2D)
        y = self.adjust_coordinates(y, is2D)
        z = self.adjust_coordinates(z, is2D)

        self.xmax = max(self.xmax, max(x))
        self.ymax = max(self.ymax, max(y))
        self.zmax = max(self.zmax, max(z))

        self.data.append(np.array((x, y, z)))
        self.labels.append(shot_summary)
        self.extrapolated.append(extrapolated)

    def init_2d(self):
        self.canvas.ax.clear()
        for i in range(len(self.data)):
            # self.lines[i].set_data([], [])
            x = self.data[i][0, 0:1]
            y = self.data[i][2, 0:1]

            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])

            self.canvas.ax.plot(x, y, linewidth=self.linewidth, label=label)

        self.canvas.draw()

    def update_2d_lines(self, num, datas, lines):
        self.canvas.ax.clear()
        for i in range(len(self.data)):
            x = self.data[i][0, :num]
            y = self.data[i][2, :num]

            print(x)
            print(y)
            print('\n\n')

            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])

            self.canvas.ax.plot(x, y, linewidth=self.linewidth, label=label)

        handles, labels = self.canvas.ax.get_legend_handles_labels()
        self.canvas.ax.legend(handles, labels)
        self.canvas.draw()

    def plot_2d(self):
        self.xmax += self.padding
        self.ymax += self.padding
        self.zmax += self.padding
        self.aspect_ratio = self.xmax // float(self.zmax)

        self.canvas.figure = plt.figure(figsize=(self.aspect_ratio * self.aspect_size, self.aspect_size))
        self.canvas.ax = plt.axes(xlim=(0, self.xmax), ylim=(0, self.zmax))
        self.canvas.ax.get_xaxis().set_visible(False)
        self.canvas.ax.get_yaxis().set_visible(False)

        longest = -1
        for i in range(len(self.data)):
            longest = max(longest, self.data[i].shape[1])

        ani = animation.FuncAnimation(self.canvas.figure, self.update_2d_lines, longest, fargs=(self.data, self.lines),
                                      interval=self.interval, blit=False, repeat=False, init_func=self.init_2d)

        handles, labels = self.canvas.ax.get_legend_handles_labels()
        self.canvas.ax.legend(handles, labels)
        self.canvas.draw()

    def init_3d(self):
        self.canvas.ax.clear()
        for i in range(len(self.data)):
            x = self.data[i][0, 0:1]
            y = self.data[i][1, 0:1]
            z = self.data[i][2, 0:1]

            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])

            self.canvas.ax.plot(x, y, z, linewidth=self.linewidth, label=label)

        self.canvas.draw()

    def update_3d_lines(self, num, datas, lines):
        self.canvas.ax.clear()
        self.canvas.ax.mouse_init()
        for i in range(len(self.data)):
            x = self.data[i][0, :num]
            y = self.data[i][1, :num]
            z = self.data[i][2, :num]

            print(x)
            print(y)
            print(z)
            print('\n\n')

            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])

            self.canvas.ax.plot(x, y, z, linewidth=self.linewidth, label=label)

        handles, labels = self.canvas.ax.get_legend_handles_labels()
        self.canvas.ax.legend(handles, labels)

        self.canvas.ax.set_xlim3d([0, self.xmax + self.padding])
        self.canvas.ax.set_ylim3d([0, self.ymax + self.padding])
        self.canvas.ax.set_zlim3d([0, self.zmax + self.padding])

        self.canvas.ax._axis3don = False
        self.canvas.ax.set_axis_off()

        self.canvas.draw()

    def plot_3d(self):
        self.xmax += self.padding
        self.ymax += self.padding
        self.zmax += self.padding
        self.aspect_ratio = self.xmax // float(self.zmax)

        self.canvas.figure = plt.figure(figsize=(self.aspect_ratio * self.aspect_size, self.aspect_size))
        self.canvas.ax = p3.Axes3D(self.canvas.figure)
        self.canvas.ax.view_init(elev=0, azim=45)
        self.canvas.ax._axis3don = False
        self.canvas.ax.set_axis_off()

        longest = -1
        for i in range(len(self.data)):
            longest = max(longest, self.data[i].shape[1])

        ani = animation.FuncAnimation(self.canvas.figure, self.update_3d_lines, longest, fargs=(self.data, self.lines),
                                      interval=self.interval, blit=False, repeat=False)

        handles, labels = self.canvas.ax.get_legend_handles_labels()
        self.canvas.ax.legend(handles, labels)
        self.canvas.draw()
