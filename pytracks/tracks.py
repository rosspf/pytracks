import numpy
import random
import math
from matplotlib.path import Path
try:
    import configparser
except ImportError:
    print("Module: configparser not found.")
class TrackSet:

    tracks = None

    def __init__(self, tracks=[]):
        self.tracks = tracks

    @property
    def count(self):
        return len(self.tracks)

    # Get the start points of every track. list comprehension
    @property
    def start_points(self):
        return [track.start_point for track in self.tracks]

    # Get the ending points of every track
    @property
    def end_points(self):
        return [track.end_point for track in self.tracks]

    @property
    def total_distances(self):
        return [track.total_distance for track in self.tracks]

    @property
    def distances(self):
        return [track.distances for track in self.tracks]

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


class Track:
    x = numpy.array([], dtype=float)
    y = numpy.array([], dtype=float)
    origin = None
    extra = []

    def __init__(self, extra_ids):
        if extra_ids is not None:
            for _ in range(len(extra_ids)):
                self.extra.append(numpy.array([], dtype=float))

    # Make the first code MOVETO then the rest LINETO
    @property
    def codes(self):
        return [Path.MOVETO].extend([Path.LINETO] * self.ticks)

    # Generate points in the format of a list of tuples (x.y)
    @property
    def points(self):
        return numpy.append([list(self.origin)], numpy.column_stack((self.x, self.y)), axis=0)

    @property
    def end_point(self):
        return self.x[-1], self.y[-1]

    @property
    def start_point(self):
        return self.origin

    @property
    def ticks(self):
        return len(self.x)

    @property
    def distances(self):
        distances_worker = numpy.array([], dtype=float)
        for i in range(len(self.points) - 1):
            distances_worker = numpy.append(distances_worker, [math.hypot(self.points[i + 1][0] - self.points[i][0], self.points[i + 1][1] - self.points[i][1])])
        return distances_worker

    # Loop over every track except last as we do not want out of bounds
    @property
    def total_distance(self):
        return numpy.sum(self.distances)
