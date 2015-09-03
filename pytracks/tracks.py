import numpy
import random
import math
from matplotlib.path import Path


class ListWrapper:

    def __init__(self, data_array):
        self.data_array = data_array

    @property
    def all(self):
        return self.data_array

    @property
    def count(self):
        return len(self.data_array)

    @property
    def start(self):
        return self.data_array[0]

    @property
    def end(self):
        return self.data_array[-1]

    @property
    def sum(self):
        return numpy.sum(self.data_array)

    @property
    def range(self):
        return numpy.ptp(self.data_array)

    @property
    def min(self):
        return numpy.min(self.data_array)

    @property
    def max(self):
        return numpy.max(self.data_array)

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


class TrackSet:

    def __init__(self, tracks=[]):
        self.tracks = tracks

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

    def count(self):
        return len(self.tracks)

    def get_track_by_id(self, id):
        return TrackSet([self.tracks[id]])

    def get_tracks_by_ids(self, ids):
        return TrackSet([self.tracks[id] for id in ids])

    def get_random_tracks(self, num):
        return TrackSet(random.sample(self.tracks, num))

    # Find if value is between two other values (+ and - of radius)
    def __point_in_area_square(self, point, center, radius):
        return (range(center[0] - radius <= point[0] <= center[0] + radius)) and (range(center[1] - radius <= point[1] <= center[1] + radius))

    # Compute Euclidean distance to the circle's center and compare to radius. If less return true.
    def __point_in_area_circle(self, point, center, radius):
        return radius >= math.hypot(point[0] - center[0], point[1] - center[1])

    def get_tracks_end_point_in_circle(self, center, radius):
        return TrackSet([track for track in self.tracks if self.__point_in_area_circle(track.start_point, center, radius)])

    # Return a TrackSet of tracks which started in a given area.
    def get_tracks_start_point_in_circle(self, center, radius):
        return TrackSet([track for track in self.tracks if self.__point_in_area_circle(track.end_point, center, radius)])

    # Return a TrackSet of tracks which ended in a given area.
    def get_tracks_end_point_in_square(self, center, radius):
        return TrackSet([track for track in self.tracks if self.__point_in_area_square(track.start_point, center, radius)])

    # Return a TrackSet of tracks which started in a given area.
    def get_tracks_start_point_in_square(self, center, radius):
        return TrackSet([track for track in self.tracks if self.__point_in_area_square(track.end_point, center, radius)])

    @property
    def points(self):
        return self.TrackSetDataWrapper([track.point.all for track in self.tracks])

    @property
    def growths(self):
        return self.TrackSetDataWrapper([track.growth.all for track in self.tracks])

    @property
    def mortalities(self):
        return self.TrackSetDataWrapper([track.mortality.all for track in self.tracks])

    @property
    def habitat_qualities(self):
        return self.TrackSetDataWrapper([track.habitat_quality.all for track in self.tracks])

    @property
    def worths(self):
        return self.TrackSetDataWrapper([track.worth.all for track in self.tracks])

    @property
    def weights(self):
        return self.TrackSetDataWrapper([track.weight.all for track in self.tracks])

    @property
    def biomasses(self):
        return self.TrackSetDataWrapper([track.biomass.all for track in self.tracks])

    def extras(self, element_id):
        return self.TrackSetDataWrapper([track.extra(element_id).all for track in self.tracks])


# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:

    def __init__(self, data, extra):
        self._data = data
        self._extra = extra

    def __len__(self):
        return len(self._data[0])


    # Make the first code MOVETO then the rest LINETO
    @property
    def codes(self):
        return [Path.MOVETO].extend([Path.LINETO] * (self.ticks - 1))

    @property
    def distance(self):
        return DistanceWrapper(self.point)

    @property
    def point(self):
        return ListWrapper(numpy.column_stack((self._data[1], self._data[2])))

    @property
    def growth(self):
        return ListWrapper(self._data[3])

    @property
    def mortality(self):
        return ListWrapper(self._data[4])

    @property
    def habitat_quality(self):
        return ListWrapper(numpy.subtract(self.growth.all, self.mortality.all))

    @property
    def worth(self):
        return ListWrapper(self._data[5])

    @property
    def weight(self):
        return ListWrapper(self._data[6])

    @property
    def biomass(self):
        return ListWrapper(numpy.multiply(self.weight.all, self.worth.all))

    def extra(self, extra_id):
        return ListWrapper(self._extra[extra_id])
