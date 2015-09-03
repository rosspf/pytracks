import numpy
import math

class TrackSetDataWrapper:

    def __init__(self, attribute_list):
        self._attribute_list = attribute_list

    @property
    def all(self):
        return self._attribute_list

    @property
    def ticks(self):
        return [ListWrapper(attribute).count for attribute in self._attribute_list]

    @property
    def start(self):
        return [ListWrapper(attribute).start for attribute in self._attribute_list]

    @property
    def end(self):
        return [ListWrapper(attribute).end for attribute in self._attribute_list]

    @property
    def sum(self):
        return [ListWrapper(attribute).sum for attribute in self._attribute_list]

    @property
    def range(self):
        return [ListWrapper(attribute).range for attribute in self._attribute_list]

    @property
    def min(self):
        return [ListWrapper(attribute).min for attribute in self._attribute_list]

    @property
    def max(self):
        return [ListWrapper(attribute).max for attribute in self._attribute_list]


class ListWrapper:

    def __init__(self, list):
        self.list = list

    @property
    def all(self):
        return self.list

    @property
    def count(self):
        return len(self.list)

    @property
    def start(self):
        return self.list[0]

    @property
    def end(self):
        return self.list[-1]

    @property
    def sum(self):
        return numpy.sum(self.list)

    @property
    def range(self):
        return numpy.ptp(self.list)

    @property
    def min(self):
        return numpy.min(self.list)

    @property
    def max(self):
        return numpy.max(self.list)


class DistanceWrapper:

    def __init__(self, points):
        self._points = points

    def __calc_distance(self, p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    @property
    def distances(self):
        return ListWrapper([self.__calc_distance(self._points.all[e], self._points.all[e + 1]) for e in range(self._points.count - 1)])

    @property
    def net(self):
        return self.__calc_distance(self._points.start, self._points.end)

    @property
    def total(self):
        return self.distances.sum