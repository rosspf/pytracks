import numpy
import random
import math
from matplotlib.path import Path


def dummy(p):
    return p


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
            raise TypeError("TrackSet objects can only be added to other TrackSets.")

    def __iadd__(self, other):
        return self + other

    def append(self, other):
        return self + other

    @staticmethod
    def point_in_rectangle(point, p1, p2):
        testpath = Path(numpy.array([[p1[0], p1[1]], [p1[1], p2[0]], [p2[0], p2[1]], [p2[1], p1[0]]]))
        return testpath.contains_point(point)

    @staticmethod
    def point_in_circle(point, center, radius):
        return radius >= math.hypot(point[0] - center[0], point[1] - center[1])

    def get_tracks_ids(self, indexes):
        return TrackSet([self.tracks[index] for index in indexes])

    def get_tracks_random(self, num=1):
        if 1 <= num <= len(self):
            return TrackSet(random.sample(self.tracks, num))
        else:
            raise ValueError("Desired tracks not between 1 and population size.")

    def get_tracks_circle(self, center, radius, index=(-1)):
        return TrackSet([track for track in self.tracks if self.point_in_circle(track.points[index], center, radius)])

    def get_tracks_rectangle(self, p1, p2, index=(-1)):
        return TrackSet([track for track in self.tracks if self.point_in_rectangle(track.points[index], p1, p2)])

    def get_tracks_mortality(self, min_mortality=0, max_mortality=1, index=(-1)):
        if min_mortality <= max_mortality:
            return TrackSet([track for track in self.tracks if min_mortality <= track.mortalities[index] <= max_mortality])
        else:
            raise ValueError("Minimum mortality can not be greater than maximum mortality.")

    def get_tracks_growth(self, min_growth=0, max_growth=1, index=(-1)):
        if min_growth <= max_growth:
            return TrackSet([track for track in self.tracks if min_growth <= track.growths[index] <= max_growth])
        else:
            raise ValueError("Minimum growth can not be greater than maximum growth.")

    def get_tracks_growth_mortality(self, min_growth=0, max_growth=1, min_mortality=0, max_mortality=1, index=(-1)):
        return set(self.get_tracks_growth(min_growth, max_growth, index)) & set(self.get_tracks_mortality(min_mortality, max_mortality, index))

    def get_tracks_habitat_quality(self, min_quality=(-1), max_quality=1, index=(-1)):
        if min_quality <= max_quality:
            return TrackSet([track for track in self.tracks if min_quality <= track.habitat_qualities[index] <= max_quality])
        else:
            raise ValueError("Minimum habitat quality can not be greater than maximum habitat quality.")

    def get_tracks_biomass(self, min_biomass, max_biomass, index=(-1)):
        if min_biomass <= max_biomass:
            return TrackSet([track for track in self.tracks if min_biomass <= track.habitat_qualities[index] <= max_biomass])
        else:
            raise ValueError("Minimum biomass can not be greater than maximum biomass.")

    def points(self, f=dummy):
        return [f(track.points) for track in self.tracks]

    def growths(self, f=dummy):
        return [f(track.growths) for track in self.tracks]

    def mortalities(self, f=dummy):
        return [f(track.mortalities) for track in self.tracks]

    def habitat_qualities(self, f=dummy):
        return [f(track.habitat_qualities) for track in self.tracks]

    def worths(self, f=dummy):
        return [f(track.worths) for track in self.tracks]

    def weights(self, f=dummy):
        return [f(track.weights) for track in self.tracks]

    def biomasses(self, f=dummy):
        return [f(track.biomasses) for track in self.tracks]

    def extras(self, element_id, f=dummy):
        return [f(track[element_id]) for track in self.tracks]


# 0 - id, 1 - x, 2 - y, 3 - g, 4 - m, 5 - worth, 6 - weight
class Track:

    SURVIVAL_THRESHOLD = 0.001

    def __init__(self, data, extra):
        self.ids, self.x, self.y, self.growths, self.mortalities, self.worths, self.weights = tuple(data)
        self.extra = extra

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, item):
        return self.extra[item]

    @staticmethod
    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    @property
    def distances(self):
        return [self.distance(self.points[e], self.points[e + 1]) for e in range(len(self) - 1)]

    @property
    def distance_net(self):
        return self.distance(self.points[0], self.points[-1])

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

    @property
    def survived(self):
        return self.SURVIVAL_THRESHOLD > self.worths[-1]

    @property
    def lifetime(self):
        ticks = numpy.where(self.SURVIVAL_THRESHOLD > self.worths)[0]
        if len(ticks) >= 1:
            return ticks[0]
        else:
            return len(self)
