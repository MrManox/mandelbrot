from PIL import Image
import numpy as np
import math as m
import sys
import itertools

def mandelbrot(z, maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return [[log(mandelbrot(complex(r, i), maxiter)) for i in r2] for r in r1]

def log(n):
    if (n <= 0):
        return 0
    return m.log(n)

def get_color(val, maxVal):
    n = int(m.pow(255, 3) * (val / maxVal))

    r = n % 255
    n = int(n / 255)
    g = n % 255
    n = int(n / 255)
    b = n % 255

    return (int(r), int(g), int(b))


if len(sys.argv) != 4:
    print("invalid number of arguments")
    quit()

try:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    iterations = int(sys.argv[3])
except ValueError:
    print("invalid arguments")
    quit()

if width <= 1 or height <= 1 or iterations <= 1:
    print("invalid arguments")
    quit()

mset = mandelbrot_set(-2.0, 0.5, -1.25, 1.25, width, height, iterations)

img = Image.new('RGB', (width, height))

maxVal = max(itertools.chain(*mset))

for x, row in enumerate(mset):
    for y, val in enumerate(row):
        color = get_color(val, maxVal)
        img.putpixel((x, y), color)

img.save("export.png")
