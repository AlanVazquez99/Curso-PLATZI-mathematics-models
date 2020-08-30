import numpy as np
import scipy as sp
import imageio
import matplotlib.pyplot as plt
import os
import shutil

from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

os.mkdir('pendulum')

theta0 = np.pi / 4
w = sp.pi


def theta(t): return theta0 * np.cos(w*t)
def x(t): return np.sin(theta(t))
def y(t): return -np.cos(theta(t))


tmax, dt = 10, .1
t = np.arange(0, tmax, dt)
filenames = []


def make_plot(i):
    r = 0.05
    n = int(i / dt)

    fig = plt.figure(dpi=72)
    ax = fig.add_subplot(111)
    ax.plot([0, x(i)], [0, y(i)], lw=2, c='k')

    c0 = Circle((0, 0), r/2, fc='k', zorder=10)
    c1 = Circle((x(i), y(i)), r, fc='b', ec='b', zorder=10)
    ax.add_patch(c0)
    ax.add_patch(c1)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 0)
    ax.set_aspect('equal', adjustable='box')

    plt.grid(True)

    filenames.append('pendulum/frames_img{:04d}.png'.format(n))
    plt.savefig('pendulum/frames_img{:04d}.png'.format(n))


for i in t:
    make_plot(i)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('pendulum.gif', images)
shutil.rmtree('pendulum')
