import numpy as np
import matplotlib.pyplot as plt
import math

from scipy import interpolate

def calc_angle(pt1, pt2):
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]

    rad_ang = math.atan2(dy,dx)

    return rad_ang*180/math.pi

x = (0,1,2,3,4,5)
y = (0,1,0,0,0,0)
 
data = np.array((x,y))

tck,_ = interpolate.splprep(data, s=0)
plot_pts = np.arange(0, 1.01, 0.01)
out = interpolate.splev(plot_pts, tck)

plt.plot(out[0], out[1], color='orange')
plt.plot(data[0,:], data[1,:], 'ob')

traj_pts = []
for i in range(len(out[0])):
    traj_pts.append([out[0][i], out[1][i]])

angles = []
prev_pt = traj_pts[0]
for pt in traj_pts[1:]:
    angles.append(calc_angle(prev_pt, pt))
    prev_pt = pt

for angle in angles:
    print(angle)