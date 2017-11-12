import csv
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def adjust_coords(L):
    output = []
    minval = min(L)

    for item in L:
        output.append(item-minval)

    return output


def update_lines(num, data, line):
    line.set_data(data[0:2, :num])
    return line


padding = 25.0
lw = 8

data = pd.read_csv('traj-detail-2017-mickelson594296.TXT', sep=';', usecols=['Tournament Sequence Number', 'Player Number', 'Round', 'Hole Number', 'Shot Sequence Number', 'Extrapolated', 'Player Last Name', 'Trajectory Sequence', 'Trajectory X Coordinate', 'Trajectory Y Coordinate', 'Trajectory Z Coordinate', 'Apex Height'])
# print(data.head())

# print(data.groupby(['Tournament Sequence Number', 'Player Number', 'Round', 'Hole Number', 'Shot Sequence Number']).head())

t1 = data.loc[(data['Tournament Sequence Number'] == 10) & (data['Extrapolated'] == 'N') & (data['Player Last Name'] == 'Mickelson')]
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
plots = 0

for name, group in t1:
    x.append(group["Trajectory X Coordinate"].tolist())
    y.append(group["Trajectory Y Coordinate"].tolist())
    z.append(group["Trajectory Z Coordinate"].tolist())
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

lines = []
for index, lay in enumerate(x):
    lobj = ax.plot([], [], lw=lw)[0]
    lines.append(lobj)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    temp = np.array(range(1, data.shape[0]+1))
    for lnum, line in enumerate(lines):
        line.set_data(x, data[:, temp[i]-1,i])
    return tupe(lines)

#for i in list(range(plots)):
#    data = np.array((x[i], z[i]))
#    line = ax.plot(data[0, 0:1], data[1, 0:1], linewidth=lw)[0]
#    line_ani = animation.FuncAnimation(fig, update_lines, data.shape[1], fargs=(data, line), interval=50, blit=False, repeat=False)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.shape(x)[1], interval=50, blit=True)
plt.show()
