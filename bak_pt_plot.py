import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class ProTracerPlot:
    def __init__(self, add_extrapolation=False, is_2d=True):
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

        self.extrapolation = add_extrapolation
        self.is_2d = is_2d

    def adjust_coordinates(self, L):
        # assumes first value is lowest for plot
        # trim list when x coord hits 0 after 1st?
        output = []
        if self.is_2d:
            minval = L[0]
        else:
            minval = min(L)

        for item in L:
            output.append(item - minval)

        return output

    def add_plot_data(self, shot_data, shot_summary):
        if self.extrapolation:
            x = shot_data["Trajectory X Coordinate"].tolist()
            y = shot_data["Trajectory Y Coordinate"].tolist()
            z = shot_data["Trajectory Z Coordinate"].tolist()
        else:
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

    def plot_2d(self, title="ProTracer 2D"):
        self.is_2d = True
        self.xmax += self.padding
        self.ymax += self.padding
        self.zmax += self.padding
        self.aspect_ratio = self.xmax // float(self.zmax)

        fig = plt.figure(figsize=(self.aspect_ratio * self.aspect_size, self.aspect_size))
        ax = plt.axes(xlim=(0, self.xmax), ylim=(0, self.zmax))
        ax.set_title(title)

        for i in range(len(self.data)):
            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])
            self.lines.append(ax.plot(self.data[i][0, 0:1], self.data[i][2, 0:1], linewidth=self.linewidth, label=label)[0])

        ani = animation.FuncAnimation(fig, self.update_2d_lines, fargs=(self.data, self.lines),
                                      interval=self.interval, blit=False, repeat=False, init_func=self.init_2d)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        #plt.axis('off')

        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()

        plt.show()

    def init_3d(self):
        for i in range(len(self.data)):
            self.lines[i].set_data([], [], [])
        return self.lines

    def update_3d_lines(self, num, datas, lines):
        for i in range(len(datas)):
            lines[i].set_data(datas[i][0:2, :num])
            lines[i].set_3d_properties(datas[i][2, :num])
        return lines

    def plot_3d(self, azim=45, axis_on=False, title="ProTracer 3D"):
        self.is_2d = False
        self.xmax += self.padding
        self.ymax += self.padding
        self.zmax += self.padding
        self.aspect_ratio = self.xmax // float(self.zmax)

        fig = plt.figure()
        ax = p3.Axes3D(fig)
        ax.set_title(title)
        ax.view_init(elev=0, azim=azim)
        ax._axis3don = axis_on

        for i in range(len(self.data)):
            label = '{0} - Round {1}'.format(
                self.labels[i]["Player Last Name"],
                self.labels[i]["Round"])

            self.lines.append(
                ax.plot(self.data[i][0, 0:1], self.data[i][1, 0:1], self.data[i][2, 0:1], linewidth=self.linewidth,
                        label=label)[0])

            ax.set_xlim3d([0, self.xmax + self.padding])
            ax.set_label('x')

            ax.set_ylim3d([0, self.ymax + self.padding])
            ax.set_label('y')

            ax.set_zlim3d([0, self.zmax + self.padding])
            ax.set_label('z')

        ani = animation.FuncAnimation(fig, self.update_3d_lines, self.data[0].shape[1], fargs=(self.data, self.lines),
                                      interval=self.interval, blit=False, repeat=False)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        # plt.axis('off')

        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()

        plt.show()
