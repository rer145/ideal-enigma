import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


# Global constants
plot_padding = 25.0
plot_linewidth = 8
plot_aspect_size = 3

data_file = 'traj-detail-2017-mickelson594296.TXT'

max_plots = 4

plot_labels = []
plot_data = []
plot_data_xmax = -1
plot_data_ymax = -1
plot_data_zmax = -1

line_data = []

def app():
    print("Welcome to PyProTracer")

    print("Reading file", data_file)
    data = pd.read_csv(data_file, sep=';')
    data["Player Full Name"] = data["Player First Name"] + " " + data["Player Last Name"]

    golfers = data["Player Full Name"].unique()
    print("Select a Golfer:")
    for i in range(len(golfers)):
        print(" {0}) {1}".format(i, golfers[i]))
    io_golfer = int(input("Enter the number of the golfer: "))

    # print(golfers[io_golfer])

    tournaments = data.loc[(data['Player Full Name'] == golfers[io_golfer])]['Tournament Name'].unique()
    print("Select a Tournament:")
    for i in range(len(tournaments)):
        print(" {0}) {1}".format(i, tournaments[i]))
    io_tournament = int(input("Enter the number of the tournament: "))

    rounds = data.loc[(data['Player Full Name'] == golfers[io_golfer]) & (data['Tournament Name'] == tournaments[io_tournament])]['Round'].unique()
    print("Select a Round:")
    for i in range(len(rounds)):
        print(" {0}) {1}".format(i, rounds[i]))
    io_round = int(input("Enter the number of the round: "))

    holes = data.loc[(data['Player Full Name'] == golfers[io_golfer]) & (data['Tournament Name'] == tournaments[io_tournament]) & (data['Round'] == rounds[io_round])]['Hole Number'].unique()
    print("Select a Hole:")
    for i in range(len(holes)):
        print(" {0}) {1}".format(i, holes[i]))
    io_hole = int(input("Enter the number of the hole: "))


    print("Plotting ProTracer for: ")
    print("  Golfer: {0}".format(golfers[io_golfer]))
    print("  Tournament: {0}".format(tournaments[io_tournament]))
    print("  Round: {0}".format(rounds[io_round]))
    print("  Hole: {0}".format(holes[io_hole]))

    plot(data, golfers[io_golfer], tournaments[io_tournament], rounds[io_round], holes[io_hole])


def adjust_coords(L):
    output = []
    minval = min(L)

    for item in L:
        output.append(item - minval)

    return output


def add_plot_data_2D(data, golfer, tournament, r, hole):
    plot_labels.append([golfer, tournament, r, hole])

    x = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory X Coordinate"].tolist()

    y = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory Y Coordinate"].tolist()

    z = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory Z Coordinate"].tolist()

    extrapolated = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Extrapolated"].tolist()

    # adjust all coordinates to baseline
    x = adjust_coords(x)
    y = adjust_coords(y)
    z = adjust_coords(z)

    global plot_data_xmax
    global plot_data_ymax
    global plot_data_zmax

    plot_data_xmax = max(plot_data_xmax, max(x))
    plot_data_ymax = max(plot_data_ymax, max(y))
    plot_data_zmax = max(plot_data_zmax, max(z))

    plot_data.append(np.array((x, z, extrapolated)))


def add_plot_data_3D(data, golfer, tournament, r, hole):
    x = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory X Coordinate"].tolist()

    y = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory Y Coordinate"].tolist()

    z = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole) &
        (data['Extrapolated'] == 'N')
        ]["Trajectory Z Coordinate"].tolist()

    # adjust all coordinates to baseline
    x = adjust_coords(x)
    y = adjust_coords(y)
    z = adjust_coords(z)

    global plot_data_xmax
    global plot_data_ymax
    global plot_data_zmax

    plot_data_xmax = max(plot_data_xmax, max(x))
    plot_data_ymax = max(plot_data_ymax, max(y))
    plot_data_zmax = max(plot_data_zmax, max(z))

    plot_data.append(np.array((x, y, z)))


def init2D():
    for i in list(range(len(plot_data))):
        line_data[i].set_data([], [])
    return line_data


def update_lines_multi_2D(num, datas, lines):
    for i in range(len(datas)):
        lines[i].set_data(datas[i][0:2, :num])
        #if datas[i][2, :num] == 'Y':
        #    lines[i].set_linestyle = '--'
        #else:
        #    lines[i].set_linestyle = '-'
    return lines


def update_lines_2D(num, data, line):
    line.set_data(data[0:2, :num])
    return line


def update_lines_multi_3D(num, datas, lines):
    for i in range(len(datas)):
        lines[i].set_data(datas[i][0:2, :num])
        lines[i].set_3d_properties(datas[i][2, :num])
    return lines


def update_lines_3D(num, data, line):
    line.set_data(data[0:2, :num])
    line.set_3d_properties(data[2, :num])
    return line


def plot2D():
    # Plotting only X and Z coords (distance and height)
    xmin = 0
    ymin = 0
    zmin = 0

    xmax = plot_data_xmax + plot_padding
    ymax = plot_data_ymax + plot_padding
    zmax = plot_data_zmax + plot_padding

    plot_aspect_ratio = xmax // float(zmax)

    fig = plt.figure(figsize=(plot_aspect_ratio * plot_aspect_size, plot_aspect_size))
    # fig = plt.figure()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(zmin, zmax))
    ax.set_title("ProTracer")

    # single line plot
    for i in range(len(plot_data)):
        label = '{0} - Round {1} #{2}'.format(plot_labels[i][0], plot_labels[i][2], plot_labels[i][3])
        line_data.append(ax.plot(plot_data[i][0, 0:1], plot_data[i][1, 0:1], linewidth=plot_linewidth, label=label)[0])


    # this version stops at all data points given
    # plot_line_ani = animation.FuncAnimation(fig, update_lines_multi_2D, plot_data[0].shape[1], fargs=(plot_data, line_data), interval=50, blit=False, repeat=False, init_func=init2D)

    # this version continues the line to end of axis
    plot_line_ani = animation.FuncAnimation(fig, update_lines_multi_2D, fargs=(plot_data, line_data),
                                            interval=50, blit=False, repeat=False, init_func=init2D)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    plt.axis('off')
    plt.show()


def plot3D():
    xmin = 0
    ymin = 0
    zmin = 0

    xmax = plot_data_xmax + plot_padding
    ymax = plot_data_ymax + plot_padding
    zmax = plot_data_zmax + plot_padding

    fig = plt.figure()
    ax = p3.Axes3D(fig)

    ax.set_xlim3d([xmax, xmax])
    ax.set_ylim3d([ymin, ymax])
    ax.set_zlim3d([zmin, zmax])

    ax.set_title("ProTracer")
    ax.view_init(elev=0, azim=55)
    ax._axis3don = True

    for i in range(len(plot_data)):
        line_data.append(ax.plot(plot_data[i][0, 0:1], plot_data[i][1, 0:1], plot_data[i][2, 0:1], linewidth=plot_linewidth)[0])

    plot_line_ani = animation.FuncAnimation(fig, update_lines_multi_3D, plot_data[0].shape[1], fargs=(plot_data, line_data), interval=50, blit=False, repeat=False)
    plt.show()


if __name__ == "__main__":
    # app()
    df = pd.read_csv(data_file, sep=';')
    df["Player Full Name"] = df["Player First Name"] + " " + df["Player Last Name"]

    add_plot_data_2D(df, 'Phil Mickelson', 'Shell Houston Open', 4, 8)
    add_plot_data_2D(df, 'Phil Mickelson', 'Dell Technologies Championship', 2, 2)

    add_plot_data_2D(df, 'Phil Mickelson', 'Safeway Open', 1, 5)
    add_plot_data_2D(df, 'Phil Mickelson', 'Safeway Open', 2, 5)
    add_plot_data_2D(df, 'Phil Mickelson', 'Safeway Open', 3, 5)
    add_plot_data_2D(df, 'Phil Mickelson', 'Safeway Open', 4, 5)
    plot2D()

    # add_plot_data_3D(df, 'Phil Mickelson', 'Safeway Open', 1, 5)
    # plot3D()
