# -*- coding: utf-8 -*-
"""
Random walk with tendancy to move right
"""
import sys

from vispy import app, scene
import numpy as np

height = 800
width = 600

canvas = scene.SceneCanvas(size=(height, width), keys='interactive')

x = height/2
y = width/2

el = scene.visuals.Ellipse(center=(x, y),
                           radius=(5., 5.),
                           color='green',
                           parent=canvas.scene)


def step():
    global x
    global y
    p_value = np.random.rand()

    if 0 <= p_value < 0.4:
        x += 1
    elif 0.4 <= p_value < 0.6:
        x -= 1
    elif 0.6 <= p_value < 0.8:
        y += 1
    else:
        y -= 1


def update(event):
    step()
    el.center = (x, y)

timer = app.Timer('auto', connect=update, start=True)

if __name__ == '__main__':
    canvas.show()
    if sys.flags.interactive == 0:
        app.run()
