import numpy
import os
from pytracks.track import TrackSet, Track
from pytracks.grid import Grid, Cell


# A method to section the data according to an ID specified
def split_data(data, split_id):
    # Sort the incoming data according to the specific column index. Mergesort used to keep original order.
    sorted_data = data[data[:, split_id].argsort(kind="mergesort")]

    # Get the column which we are interested in sorting to
    ids = sorted_data[:, split_id]

    # Find where each element is different from it's neighbor and add 1 to get the right splitting point
    id_indexes = [j + 1 for j in numpy.where(ids[:-1] != ids[1:])[0]]

    return numpy.split(sorted_data, id_indexes)


def get_data(data_file, sectioned):
    try:
        raw_input = numpy.loadtxt(os.path.abspath(data_file))
    except (IOError, FileNotFoundError):
        raise
    if sectioned:
        return split_data(raw_input, 0)
    else:
        return [raw_input]


class TrackWrapper:

    def __init__(self, data_file, sectioned=True, id_column=1, x_column=2, y_column=3, g_column=4, m_column=5, worth_column=6, weight_column=7, extra_ids=None):
        self.data = get_data(data_file, sectioned)
        self.data_ids = [id_column, x_column, y_column, g_column, m_column, worth_column, weight_column]
        self.extra_ids = extra_ids

    # Get trackset of id. If nothing passed get first
    def gen_trackset(self, index=0):
        new_tracks = []
        for raw_track in split_data(self.data[index], self.data_ids[0]):
            new_track_data = []
            new_track_data_extra = []
            for element in self.data_ids:
                new_track_data.append(raw_track[:, element])
            if self.extra_ids is not None:
                for element in self.extra_ids:
                    new_track_data_extra.append(raw_track[:, element])
            new_tracks.append(Track(new_track_data, new_track_data_extra))
        return TrackSet(new_tracks)


class GridWrapper:

    def __init__(self, data_file, sectioned=True, x_column=1, y_column=2, extra_ids=None):
        self.data = get_data(data_file, sectioned)
        self.data_ids = [x_column, y_column]
        self.extra_ids = extra_ids

    def gen_grid(self, index=0):
        grid_builder = []
        for cell in self.data[index]:
            data_extra = None
            if self.extra_ids is not None:
                data_extra = [cell[e] for e in self.extra_ids]
            grid_builder.append(Cell(cell[self.data_ids[0]], cell[self.data_ids[1]], data_extra))
        return Grid(grid_builder)
