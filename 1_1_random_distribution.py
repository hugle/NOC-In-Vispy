# -*- coding: utf-8 -*-
"""
Random distribution
"""
import sys
import random

from vispy import app, scene
import numpy as np

height = 800
width = 600

canvas = scene.SceneCanvas(size=(height, width), keys='interactive')

bins = 5

rand_counts = list([0] * bins)

w = (width - 100) / len(rand_counts)

polygons = []

total_simulated = 1.0

for idx, val in enumerate(rand_counts):
    # define vertices from clockwise
    shape = scene.visuals.Polygon(pos=np.array(
        [[5+idx*w, 0], [5+idx*w+w-1, 0],
         [5+idx*w+w-1, val*(height-100)/total_simulated],
         [5+idx*w, val*(height-100)/total_simulated]]),
        color='green', parent=canvas.scene)
    polygons.append(shape)


def update(event):
    global total_simulated
    total_simulated += 1.0
    position = random.randint(0, bins-1)
    rand_counts[position] += 1

    for idx, shape in enumerate(polygons):
        vertices = [[5+idx*w, 0], [5+idx*w+w-1, 0],
                    [5+idx*w+w-1,
                     rand_counts[idx]*(height-100)/total_simulated],
                    [5+idx*w,
                     rand_counts[idx]*(height-100)/total_simulated]]

        shape.pos = np.array(vertices)

timer = app.Timer('auto', connect=update, start=True)

if __name__ == '__main__':
    canvas.show()
    if sys.flags.interactive == 0:
        app.run()
