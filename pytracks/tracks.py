import numpy
import random
import math
from matplotlib.path import Path


class TrackSet:

    tracks = None

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

    @property
    def start_points(self):
        return [track.start_point for track in self.tracks]

    @property
    def end_points(self):
        return [track.end_point for track in self.tracks]

    @property
    def total_distances(self):
        return [track.total_distance for track in self.tracks]

    @property
    def start_growths(self):
        return [track.start_growth for track in self.tracks]

    @property
    def end_growths(self):
        return [track.end_growth for track in self.tracks]

    @property
    def start_mortalities(self):
        return [track.start_mortality for track in self.tracks]

    @property
    def end_mortalities(self):
        return [track.end_mortality for track in self.tracks]

    @property
    def start_habitat_qualities(self):
        return [track.start_habitat_quality for track in self.tracks]

    @property
    def end_habitat_qualities(self):
        return [track.end_habitat_quality for track in self.tracks]

    @property
    def start_worths(self):
        return [track.start_worth for track in self.tracks]

    @property
    def end_worths(self):
        return [track.end_worth for track in self.tracks]

    @property
    def start_weights(self):
        return [track.start_weight for track in self.tracks]

    @property
    def end_weight(self):
        return [track.end_weight for track in self.tracks]

    def start_extras(self, id):
        return [track.start_extra(id) for track in self.tracks]

    def end_extras(self, id):
        return [track.end_extra(id) for track in self.tracks]



# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:

    _data = []
    _extra = []

    def __init__(self, data, num_extra):
        self._data = data
        for _ in range(len(num_extra)):
            self._extra.append(numpy.array([], dtype=float))

    @property
    def ticks(self):
        return len(self._data[0])

    # Make the first code MOVETO then the rest LINETO
    @property
    def codes(self):
        return [Path.MOVETO].extend([Path.LINETO] * (self.ticks - 1))




    # Generate points in the format of a list of tuples (x.y)
    @property
    def points(self):
        return numpy.column_stack((self._data[1], self._data[2]))

    @property
    def start_point(self):
        return self._data[1][0], self._data[2][0]

    @property
    def end_point(self):
        return self._data[1][-1], self._data[2][-1]

    @property
    def distances_between_timesteps(self):
        distances_worker = numpy.array([], dtype=float)
        for i in range(len(self.points) - 1):
            distances_worker = numpy.append(distances_worker, [math.hypot(self.points[i + 1][0] - self.points[i][0], self.points[i + 1][1] - self.points[i][1])])
        return distances_worker

    @property
    def total_distance(self):
        return numpy.sum(self.distances_between_timesteps)

    @property
    def growth_lifetime(self):
        return self._data[3]

    @property
    def start_growth(self):
        return self._data[3][0]

    @property
    def end_growth(self):
        return self._data[3][-1]

    @property
    def mortality_lifetime(self):
        return self._data[4]

    @property
    def start_mortality(self):
        return self._data[4][0]

    @property
    def end_mortality(self):
        return self._data[4][-1]

    @property
    def habitat_quality_lifetime(self):
        return numpy.subtract(self.growth, self.mortality)

    @property
    def start_habitat_quality(self):
        return self.start_growth - self.start_mortality

    @property
    def end_habitat_quality(self):
        return self.end_growth - self.end_mortality

    @property
    def weight_lifetime(self):
        return self._data[3]

    @property
    def start_weight(self):
        return self._data[6][0]

    @property
    def end_weight(self):
        return self._data[6][-1]

    @property
    def worth_lifetime(self):
        return self._data[5]

    @property
    def start_worth(self):
        return self._data[5][0]

    @property
    def end_worth(self):
        return self._data[5][-1]

    @property
    def biomass_lifetime(self):
        return numpy.multiply(self.weight, self.worth)

    @property
    def start_biomass(self):
        return self.start_weight * self.start_worth

    @property
    def end_biomass(self):
        return self.end_weight * self.end_worth

    def extra_all(self, id):
        return self._extra[id]

    def start_extra(self, id):
        return self._extra[id][0]

    def end_extra(self, id):
        return self._extra[id][-1]
