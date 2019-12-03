from PIL import Image
import numpy as np
import math as m
import sys

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

if (width <= 0 or height <= 1 or iterations <= 1):
    print("invalid arguments")
    quit()

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


def get_max(my_list):
    m = None
    for item in my_list:
        if isinstance(item, list):
            item = get_max(item)
        if not m or m < item:
            m = item
    return m


def get_color(val, maxVal):
    n = int(m.pow(255, 3) * (val/maxVal))

    r = n % 255
    n = int(n / 255)
    g = n % 255
    n = int(n / 255)
    b = n % 255

    return (int(r), int(g), int(b))


mset = mandelbrot_set(-2.0, 0.5, -1.25, 1.25, width, height, iterations)

img = Image.new('RGB', (width, height))

maxVal = get_max(mset)
for x in range(len(mset)):
    for y in range(len(mset[x])):
        color = get_color(mset[x][y], maxVal)
        img.putpixel((x, y), color)

img.save("export.png")
