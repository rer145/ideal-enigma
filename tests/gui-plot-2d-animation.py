import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.x = np.arange(0, 2 * np.pi, 0.01)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.canvas = PlotCanvas(self, width=6, height=6)
        self.canvas.move(0, 0)

        self.show()
        self.do_plot()

    def init(self):
        self.canvas.ax.clear()
        self.line.set_ydata(np.ma.array(self.x, mask=True))
        self.canvas.draw()
        return self.line,

    def animate(self, i):
        self.canvas.ax.clear()
        self.line.set_ydata(np.sin(self.x + i / 10.0))
        self.canvas.draw()
        return self.line,

    def do_plot(self):
        # self.canvas.figure = plt.figure()
        # self.canvas.ax = plt.axes(xlim=(0, max(self.x_data)), ylim=(0, max(self.y_data)))
        # self.canvas.ax.plot(self.x_data, np.sin(self.x_data))

        self.canvas.figure, self.canvas.ax = plt.subplots()
        self.line, = self.canvas.ax.plot(self.x, np.sin(self.x))
        ani = animation.FuncAnimation(self.canvas.figure, self.animate, np.arange(1, 200), init_func=self.init,
                                      interval=25, blit=True)

        self.canvas.draw()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
