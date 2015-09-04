import numpy
import random
from pytracks.functions import distance, point_in_area_circle, point_in_area_square, dummy
from matplotlib.path import Path


class TrackSet:

    def __init__(self, tracks=None):
        if tracks is None:
            self.tracks = []
        else:
            self.tracks = tracks

    def __len__(self):
        return len(self.tracks)

    def __iter__(self):
        return iter(self.tracks)

    def __getitem__(self, item):
        return self.tracks[item]

    def __add__(self, other):
        if isinstance(other, TrackSet):
            return TrackSet(other.tracks + self.tracks)
        else:
            raise TypeError("TrackSet objects can only be added with other TrackSets.")

    def get_ids(self, ids):
        return TrackSet([self.tracks[id] for id in ids])

    def get_random(self, num=1):
        return TrackSet(random.sample(self.tracks, num))

    def get_tracks_end_point_in_circle(self, center, radius):
        return TrackSet([track for track in self.tracks if point_in_area_circle(track.start_point, center, radius)])

    # Return a TrackSet of tracks which started in a given area.
    def get_tracks_start_point_in_circle(self, center, radius):
        return TrackSet([track for track in self.tracks if point_in_area_circle(track.end_point, center, radius)])

    # Return a TrackSet of tracks which ended in a given area.
    def get_tracks_end_point_in_square(self, center, radius):
        return TrackSet([track for track in self.tracks if point_in_area_square(track.start_point, center, radius)])

    # Return a TrackSet of tracks which started in a given area.
    def get_tracks_start_point_in_square(self, center, radius):
        return TrackSet([track for track in self.tracks if point_in_area_square(track.end_point, center, radius)])

    def get_points(self, f=dummy):
        return [f(track.points) for track in self.tracks]

    def get_growths(self, f=dummy):
        return [f(track.growths) for track in self.tracks]

    def get_mortalities(self, f=dummy):
        return [f(track.mortalities) for track in self.tracks]

    def get_habitat_qualities(self, f=dummy):
        return [f(track.habitat_qualities) for track in self.tracks]

    def get_worths(self, f=dummy):
        return [f(track.worths) for track in self.tracks]

    def get_weights(self, f=dummy):
        return [f(track.weights) for track in self.tracks]

    def get_biomasses(self, f=dummy):
        return [f(track.biomasses) for track in self.tracks]

    def get_extras(self, element_id, f=dummy):
        return [f(track[element_id]) for track in self.tracks]


# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:
    def __init__(self, data, extra):
        self.ids, self.x, self.y, self.growths, self.mortalities, self.worths, self.weights = tuple(data)
        self.extra = extra

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, item):
        return self.extra[item]

    @property
    def codes(self):
        return [Path.MOVETO].extend([Path.LINETO] * (len(self) - 1))

    @property
    def distances(self):
        return [distance(self.points[e], self.points[e + 1]) for e in range(len(self) - 1)]

    @property
    def distance_net(self):
        return distance(self.points[0], self.points[-1])

    @property
    def distance_total(self):
        return numpy.sum(self.distances)

    @property
    def points(self):
        return numpy.column_stack((self.x, self.y))

    @property
    def habitat_qualities(self):
        return numpy.subtract(self.growths, self.mortalities)

    @property
    def biomasses(self):
        return numpy.multiply(self.weights, self.worths)
