import math


def dummy(p):
    return p


def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def map_helper(data, f):
    if f is not None:
        return [f(row) for row in data]
    else:
        return data


# Find if value is between two other values (+ and - of radius)
def point_in_area_square(point, center, radius):
    return (range(center[0] - radius <= point[0] <= center[0] + radius)) and (range(center[1] - radius <= point[1] <= center[1] + radius))


# Compute Euclidean distance to the circle's center and compare to radius. If less return true.
def point_in_area_circle(point, center, radius):
    return radius >= math.hypot(point[0] - center[0], point[1] - center[1])