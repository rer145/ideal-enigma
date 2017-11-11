import csv
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# TODO: update to use first value as 'zero' and adjust all others from there
def adjust_coords(L):
    output = []
    minval = min(L)
    # minval = L[0]

    for item in L:
        output.append(item-minval)

    return output


def update_lines(num, data, lines):
    for line in lines:
        line.set_data(data[0:2, :num])
    return lines


padding = 25.0
lw = 5
tournament_id = 190

data = pd.read_csv('traj-detail-2017-mickelson594296.TXT', sep=';', usecols=['Tournament Sequence Number', 'Player Number', 'Round', 'Hole Number', 'Shot Sequence Number', 'Extrapolated', 'Player Last Name', 'Trajectory Sequence', 'Trajectory X Coordinate', 'Trajectory Y Coordinate', 'Trajectory Z Coordinate', 'Apex Height'])
# print(data.head())

# print(data.groupby(['Tournament Sequence Number', 'Player Number', 'Round', 'Hole Number', 'Shot Sequence Number']).head())

#t1 = data.loc[(data['Tournament Sequence Number'] == 10) & (data['Extrapolated'] == 'N') & (data['Player Last Name'] == 'Mickelson')]
t1 = data.loc[(data['Tournament Sequence Number'] == tournament_id) & (data['Extrapolated'] == 'N') & (data['Player Last Name'] == 'Mickelson')]
# print(t1.groupby(['Round', 'Hole Number', 'Shot Sequence Number'])['Trajectory X Coordinate'].describe())
t1 = t1.groupby(['Round', 'Hole Number', 'Shot Sequence Number'])

#for name, group in t1:
#    print(name)
#    print('\n\n')
#    print(group)
#    print('\n\n')
#    print('-----------------------------------')

x = []
y = []
z = []
labels = []
plots = 0

for name, group in t1:
    x.append(group["Trajectory X Coordinate"].tolist())
    y.append(group["Trajectory Y Coordinate"].tolist())
    z.append(group["Trajectory Z Coordinate"].tolist())
    labels.append(group['Round'].tolist()[0])
    plots += 1


# adjust all coordinates
maxx = 0
maxy = 0
maxz = 0

for i in list(range(len(x))):
    x[i] = adjust_coords(x[i])
    if max(x[i]) > maxx:
        maxx = max(x[i])

for i in list(range(len(y))):
    y[i] = adjust_coords(y[i])
    if max(y[i]) > maxy:
        maxy = max(y[i])

for i in list(range(len(z))):
    z[i] = adjust_coords(z[i])
    if max(z[i]) > maxz:
        maxz = max(z[i])

# figure out min/max plotting area
xmin = 0
ymin = 0
xmax = maxx + padding
ymax = maxz + padding

aspect_ratio = xmax // float(ymax)
aspect_size = 3

fig = plt.figure(figsize=(aspect_ratio*aspect_size, aspect_size))
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

for i in list(range(plots)):
    plt.plot(x[i], z[i], linewidth=lw, label='Round ' + str(labels[i]))


#lines = []
#for i in list(range(plots)):
#    data = np.array((x[i], z[i]))
#    lines.append(ax.plot(data[0, 0:1], data[1, 0:1], linewidth=lw)[0])
#    line_ani = animation.FuncAnimation(fig, update_lines, data.shape[1], fargs=(data, lines), interval=50, blit=False, repeat=False)



data0 = np.array((x[0], z[0]))
line0 = ax.plot(data0[0, 0:1], data0[1, 0:1], linewidth=lw)[0]
line_ani0 = animation.FuncAnimation(fig, update_lines, data0.shape[1], fargs=(data0, line0), interval=50, blit=False, repeat=False)

data1 = np.array((x[1], z[1]))
line1 = ax.plot(data1[0, 0:1], data1[1, 0:1], linewidth=lw)[0]
line_ani1 = animation.FuncAnimation(fig, update_lines, data1.shape[1], fargs=(data1, line1), interval=50, blit=False, repeat=False)

# data2 = np.array((x[2], z[2]))
# line2 = ax.plot(data2[0, 0:1], data2[1, 0:1], linewidth=lw)[0]
# line_ani2 = animation.FuncAnimation(fig, update_lines, data2.shape[1], fargs=(data2, line2), interval=50, blit=False, repeat=False)
#
# data3 = np.array((x[3], z[3]))
# line3 = ax.plot(data3[0, 0:1], data3[1, 0:1], linewidth=lw)[0]
# line_ani3 = animation.FuncAnimation(fig, update_lines, data3.shape[1], fargs=(data3, line3), interval=50, blit=False, repeat=False)

ax.legend()
plt.title("Phil Mickelson Drives")
plt.show()
