import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# x = distance from screen away from user
# y = distance left or right
# z = height

def adjust_coords(L):
    output = []
    minval = min(L)

    for item in L:
        output.append(item-minval)

    return output

def update_lines_multi(num, datas, lines):
    for i in list(range(len(datas))):
        lines[i].set_data(datas[i][0:2, :num])
    return lines

def update_lines(num, data, line):
    line.set_data(data[0:2, :num])
    return line

x = [9974.563,10017.888,10058.331,10096.2,10131.771,10165.291,10196.984,10227.046,10255.652,10282.958,10309.099,10334.195,10358.352,10381.659,10404.197,10426.033,10447.228,10467.833,10487.892,10507.444,10526.524,10545.161,10563.382,10581.212,10598.674,10615.789,10632.577,10649.06,10665.257,10681.189,10696.876]
y = [12963.628,12947.29,12931.773,12916.999,12902.899,12889.41,12876.473,12864.038,12852.057,12840.488,12829.293,12818.44,12807.899,12797.642,12787.646,12777.89,12768.357,12759.029,12749.893,12740.935,12732.145,12723.513,12715.029,12706.685,12698.475,12690.39,12682.425,12674.574,12666.83,12659.187,12651.639]
z = [135.455,148.746,161.526,173.735,185.317,196.223,206.41,215.842,224.489,232.325,239.329,245.484,250.779,255.205,258.757,261.435,263.238,264.172,264.241,263.453,261.819,259.35,256.056,251.951,247.049,241.362,234.904,227.689,219.73,211.039,201.628]

# does not contain calculated values only extrapolated
x2 = [8321.125,8353.034,8382.989,8411.171,8437.744,8462.858,8486.647,8509.234,8530.727,8551.224,8570.815,8589.576,8607.578,8624.883,8641.545,8657.613,8673.13,8688.135,8702.66,8716.735,8730.389,8743.644,8756.522,8769.044,8781.228,8793.092,8804.651,8815.924,8826.924,8837.67,8848.175,8858.458,8868.534,8878.419,8888.133,8897.691,8907.111]
y2 = [9230.52,9264.774,9297.364,9328.426,9358.085,9386.457,9413.649,9439.759,9464.876,9489.084,9512.458,9535.066,9556.97,9578.229,9598.894,9619.01,9638.62,9657.763,9676.471,9694.776,9712.706,9730.284,9747.534,9764.475,9781.125,9797.501,9813.617,9829.487,9845.124,9860.54,9875.745,9890.751,9905.568,9920.207,9934.676,9948.988,9963.153]
z2 = [1818.41,1831.815,1844.586,1856.704,1868.151,1878.91,1888.968,1898.31,1906.925,1914.8,1921.926,1928.296,1933.902,1938.738,1942.799,1946.084,1948.59,1950.316,1951.264,1951.434,1950.83,1949.456,1947.316,1944.417,1940.765,1936.367,1931.232,1925.368,1918.785,1911.491,1903.498,1894.814,1885.451,1875.417,1864.723,1853.378,1841.391]


x3 = [8599.516,8628.12,8655.129,8680.697,8704.961,8728.046,8750.062,8771.106,8791.267,8810.623,8829.243,8847.19,8864.519,8881.28,8897.518,8913.274,8928.587,8943.489,8958.014,8972.191,8986.049,8999.617,9012.919,9025.982,9038.83,9051.487,9063.978,9076.324,9088.546,9100.665,9112.699,9124.665,9136.575,9148.442,9160.273,9172.07]
y3 = [6981.407,7016.875,7049.945,7080.861,7109.842,7137.082,7162.755,7187.015,7209.997,7231.822,7252.598,7272.417,7291.363,7309.511,7326.924,7343.662,7359.777,7375.317,7390.324,7404.841,7418.903,7432.548,7445.809,7458.72,7471.313,7483.619,7495.671,7507.498,7519.131,7530.599,7541.928,7553.146,7564.275,7575.337,7586.348,7597.321]
z3 = [135.568,148.872,161.567,173.618,184.997,195.683,205.657,214.906,223.418,231.185,238.2,244.459,249.957,254.69,258.656,261.851,264.27,265.908,266.761,266.822,266.082,264.533,262.166,258.968,254.929,250.036,244.275,237.633,230.096,221.652,212.288,201.993,190.758,178.575,165.439,151.351]


currentx = x3
currenty = y3
currentz = z3

padding = 25.0

x = adjust_coords(x)
y = adjust_coords(y)
z = adjust_coords(z)
x2 = adjust_coords(x2)
y2 = adjust_coords(y2)
z2 = adjust_coords(z2)
x3 = adjust_coords(x3)
y3 = adjust_coords(y3)
z3 = adjust_coords(z3)

xmin = 0
xmax = max([max(x), max(x2), max(x3)])+padding
ymin = 0
ymax = max([max(z), max(z2), max(z3)])+padding

aspect_ratio = xmax // float(ymax)
aspect_size = 3

# fig, ax = plt.subplots(figsize=(aspect_ratio*aspect_size, aspect_size), sharex=True, sharey=True)
fig = plt.figure(figsize=(aspect_ratio*aspect_size, aspect_size))
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
#


# ax.set_aspect('auto', 'datalim')
# line, = ax.plot([], [], lw=10)


# plot traj from "side" view.  left to right is distance (x), y-axis is height (z)

datas = []
datas.append(np.array((x,z)))
datas.append(np.array((x2,z2)))
datas.append(np.array((x3,z3)))

lines = []
lines.append(ax.plot(datas[0][0, 0:1], datas[0][1, 0:1], linewidth=10)[0])
lines.append(ax.plot(datas[1][0, 0:1], datas[1][1, 0:1], linewidth=10)[0])
lines.append(ax.plot(datas[2][0, 0:1], datas[2][1, 0:1], linewidth=10)[0])

line_ani = animation.FuncAnimation(fig, update_lines_multi, datas[0].shape[1], fargs=(datas, lines), interval=50, blit=False, repeat=False)

#data = np.array((x, z))
#line = ax.plot(data[0, 0:1], data[1, 0:1], linewidth=10)[0]
#line_ani = animation.FuncAnimation(fig, update_lines, data.shape[1], fargs=(data, line), interval=50, blit=False, repeat=False)

#data2 = np.array((x2, z2))
#line2 = ax.plot(data2[0, 0:1], data2[1, 0:1], linewidth=10)[0]
#line_ani2 = animation.FuncAnimation(fig, update_lines, data2.shape[1], fargs=(data2, line2), interval=50, blit=False, repeat=False)

#data3 = np.array((x3, z3))
#line3 = ax.plot(data3[0, 0:1], data3[1, 0:1], linewidth=10)[0]
#line_ani3 = animation.FuncAnimation(fig, update_lines, data3.shape[1], fargs=(data3, line3), interval=50, blit=False, repeat=False)

# plt.plot(currentx, currentz, linewidth=10, c="red")
plt.show()
