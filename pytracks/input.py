import numpy
import os
import pytracks.tracks
try:
    import configparser
except ImportError:
    print("Module: configparser not found.")


def read_data(data_file):
    try:
        return numpy.loadtxt(os.path.abspath(data_file))
    except (IOError, FileNotFoundError):
        raise


# A method to section the data according to an ID specified
def split_data(data, split_id):
    # Sort the incoming data according to the specific column index. Mergesort used to keep original order.
    sorted_data = data[data[:,split_id].argsort(kind="mergesort")]

    # Get the column which we are interested in sorting to
    ids = sorted_data[:,split_id]

    # Find where each element is different from it's neighbor and add 1 to get the right splitting point
    id_indexes = [j + 1 for j in numpy.where(ids[:-1] != ids[1:])[0]]

    return numpy.split(sorted_data, id_indexes)

class TrackWrapper:
    def __init__(self, data_file, extra_ids=None, sectioned=True, id_column=1, x_column=2, y_column=3):
        input = read_data(data_file)
        self.extra_ids = extra_ids
        if sectioned:
            self.data_ids = [id_column, x_column, y_column]
            self.data = split_data(input, 0)
        else:
            # Subtract 1 from each id to compensate for no section id
            self.data_ids = [v - 1 for v in [id_column, x_column, y_column]]
            self.data = [input]

    # Get trackset of id. If nothing passed get first
    def get_trackset(self, id=0):
        new_tracks = []
        for raw_track in split_data(self.data[id], self.data_ids[0]):
            track = pytracks.tracks.Track(self.extra_ids)
            for raw_tick in raw_track:
                track.x = numpy.append(track.x, raw_tick[self.data_ids[1]])
                track.y = numpy.append(track.y, raw_tick[self.data_ids[2]])
                if self.extra_ids is not None:
                    for current_extra_id in range(len(self.extra_ids)):
                        numpy.append(track.extra[current_extra_id], raw_tick[self.extra_ids[current_extra_id]])
            new_tracks.append(track)
        return pytracks.tracks.TrackSet(new_tracks)

class GridWrapper:
    def __init__(self, data_file, extra_ids=None, sectioned=True, x_column=1, y_column=2):
        input = read_data(data_file)
        self.extra_ids = extra_ids
        if sectioned:
            self.data_ids = [x_column, y_column]
            self.data = split_data(input, 0)
        else:
            # Subtract 1 from each id to compensate for no section id
            self.data_ids = [v - 1 for v in [x_column, y_column]]
            self.data = [input]

    def get_grid(self, id=0):
        return self.data[id]

    def size(self, id=0):
        return self.data[id][-1][self.data_ids[0]], self.data[id][-1][self.data_ids[1]]