import numpy
import random
import math
from matplotlib.path import Path


class TrackSet:

    def __init__(self, tracks=[]):
        self.tracks = tracks

    @property
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

    def points(self, statistic):
        return [track.point(statistic) for track in self.tracks]

    def growths(self, statistic):
        return [track.growth(statistic) for track in self.tracks]

    def mortalities(self, statistic):
        return [track.mortality(statistic) for track in self.tracks]

    def habitat_qualities(self, statistic):
        return [track.habitat_quality(statistic) for track in self.tracks]

    def worths(self, statistic):
        return [track.worth(statistic) for track in self.tracks]

    def weights(self, statistic):
        return [track.weight(statistic) for track in self.tracks]

    def biomasses(self, statistic):
        return [track.biomass(statistic) for track in self.tracks]

    def extras(self, id, statistic):
        return [track.extra(id, statistic) for track in self.tracks]


# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:

    def __init__(self, data, num_extra):
        self._data = data
        self._extra = []
        for _ in range(len(num_extra)):
            self._extra.append(numpy.array([], dtype=float))

    class DataWrapper:

        def __init__(self, attribute):
            self.attribute = attribute

        @property
        def start(self):
            return self.attribute[0]

        @property
        def end(self):
            return self.attribute[-1]

        @property
        def all(self):
            return self.attribute

    def _fetch_data(self, attribute, statistic):
        return {
            'start': attribute[0],
            'end': attribute[-1],
            'all': attribute,
        }.get(statistic, None)

    @property
    def ticks(self):
        return len(self._data[0])

    # Make the first code MOVETO then the rest LINETO
    @property
    def codes(self):
        return [Path.MOVETO].extend([Path.LINETO] * (self.ticks - 1))

    @property
    def distances_between_timesteps(self):
        distances_worker = numpy.array([], dtype=float)
        for i in range(len(self.points) - 1):
            distances_worker = numpy.append(distances_worker, [math.hypot(self.points[i + 1][0] - self.points[i][0], self.points[i + 1][1] - self.points[i][1])])
        return distances_worker

    @property
    def total_distance(self):
        return numpy.sum(self.distances_between_timesteps)

    def point(self, statistic):
        return self._fetch_data(numpy.column_stack((self._data[1], self._data[2])), statistic)

    def growth(self, statistic):
        return self._fetch_data(self._data[3], statistic)

    def mortality(self, statistic):
        return self._fetch_data(self._data[4], statistic)

    def habitat_quality(self, statistic):
        return self._fetch_data(numpy.subtract(self.growth, self.mortality), statistic)

    def worth(self, statistic):
        return self._fetch_data(self._data[5], statistic)

    def weight(self, statistic):
        return self._fetch_data(self._data[6], statistic)

    def biomass(self, statistic):
        return self._fetch_data(numpy.multiply(self.weight, self.worth), statistic)

    def extra(self, id, statistic):
        return self._fetch_data(self._extra[id], statistic)