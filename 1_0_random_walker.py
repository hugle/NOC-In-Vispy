# -*- coding: utf-8 -*-
"""
Random walk
"""
import sys
import random

from vispy import app, scene

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
    vertical_choice = 2.0*random.random()-1.0
    horizontal_choice = 2.0*random.random()-1.0

    x += horizontal_choice
    y += vertical_choice


def update(event):
    step()
    el.center = (x, y)

timer = app.Timer('auto', connect=update, start=True)

if __name__ == '__main__':
    canvas.show()
    if sys.flags.interactive == 0:
        app.run()
