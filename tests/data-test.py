import csv
import pandas as pd
import numpy as np


plot_data = []
plot_data_xmax = -1
plot_data_ymax = -1
plot_data_zmax = -1


def add_plot_data_2D(data, golfer, tournament, r, hole):
    x = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole)
        ]["Trajectory X Coordinate"].tolist()

    y = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole)
        ]["Trajectory Y Coordinate"].tolist()

    z = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole)
        ]["Trajectory Z Coordinate"].tolist()

    extrapolated = data.loc[
        (data['Player Full Name'] == golfer) &
        (data['Tournament Name'] == tournament) &
        (data['Round'] == r) &
        (data['Hole Number'] == hole)
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


def adjust_coords(L):
    output = []
    minval = min(L)

    for item in L:
        output.append(item - minval)

    return output


data_file = 'traj-detail-2017-mickelson594296.TXT'
data = pd.read_csv(data_file, sep=';')
data["Player Full Name"] = data["Player First Name"] + " " + data["Player Last Name"]

temp_df = data.loc[
        (data['Player Full Name'] == 'Phil Mickelson') &
        (data['Tournament Name'] == 'Safeway Open') &
        (data['Round'] == 1) &
        (data['Hole Number'] == 5) &
        (data['Trajectory Sequence'] == 1)
        ]

print(temp_df.iloc[0]["Club"])


exit(0)

add_plot_data_2D(data, 'Phil Mickelson', 'Safeway Open', 1, 5)
add_plot_data_2D(data, 'Phil Mickelson', 'Safeway Open', 2, 5)
add_plot_data_2D(data, 'Phil Mickelson', 'Safeway Open', 3, 5)
add_plot_data_2D(data, 'Phil Mickelson', 'Safeway Open', 4, 5)

# print(plot_data)
print('Plot data\n', plot_data[0])
print('plot data shape 0\n', plot_data[0].shape[0])
print('plot data shape 1\n', plot_data[0].shape[1])
print('plot data extrapolated data\n', plot_data[0][2])
print('plot data extrapolated data (5)\n', plot_data[0][2, :5])
# print(plot_data[0][3, :3])
# print(plot_data[0][3, 3])
