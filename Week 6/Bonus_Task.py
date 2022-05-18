import math
import random


def calculate_pi():
    random_points = [{'x': random.random(), 'y': random.random()} for _ in range(10000)]
    inside_circle_points = []
    for rand_pt in random_points:
        if ((rand_pt['x'] ** 2) + (rand_pt['y'] ** 2)) < 1:
            inside_circle_points.append(rand_pt)
    random_pi = (4 * len(inside_circle_points)) / len(random_points)
    return random_pi


difference = math.pi - calculate_pi()

print(f'Calculated value of π: {calculate_pi()}')
print(f'Value of π from math library: {math.pi}')
print(f'Difference: {difference}')