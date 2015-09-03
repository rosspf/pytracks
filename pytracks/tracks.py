import numpy
import random
import math
from pytracks.datawrappers import TrackSetDataWrapper, ListWrapper, DistanceWrapper
from matplotlib.path import Path


class TrackSet:

    def __init__(self, tracks=[]):
        self.tracks = tracks

    def __len__(self):
        return len(self.tracks)

    def __iter__(self):
        return iter(self.tracks)

    def __getitem__(self, item):
        return self.tracks[item]

    def __add__(self, other):
        if isinstance(other, TrackSet):
            return TrackSet(other.tracks.extend(self.tracks))
        else:
            raise TypeError("TrackSet objects can only be added with other TrackSets.")

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
        return TrackSetDataWrapper([track.point.list for track in self.tracks])

    @property
    def growths(self):
        return TrackSetDataWrapper([track.growth.list for track in self.tracks])

    @property
    def mortalities(self):
        return TrackSetDataWrapper([track.mortality.list for track in self.tracks])

    @property
    def habitat_qualities(self):
        return TrackSetDataWrapper([track.habitat_quality.list for track in self.tracks])

    @property
    def worths(self):
        return TrackSetDataWrapper([track.worth.list for track in self.tracks])

    @property
    def weights(self):
        return TrackSetDataWrapper([track.weight.list for track in self.tracks])

    @property
    def biomasses(self):
        return TrackSetDataWrapper([track.biomass.list for track in self.tracks])

    def extras(self, element_id):
        return TrackSetDataWrapper([track.extra[element_id].list for track in self.tracks])


# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:

    def __init__(self, data, extra):
        self.data = data
        self.extra = extra

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
        return ListWrapper(numpy.column_stack((self.x, self.y)))

    @property
    def habitat_quality(self):
        return ListWrapper(numpy.subtract(self.growth, self.mortality))

    @property
    def biomass(self):
        return ListWrapper(numpy.multiply(self.weight, self.worth))

    @property
    def id(self):
        return ListWrapper(self.data[0])
