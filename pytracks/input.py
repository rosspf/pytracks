import numpy
import os
import pytracks.tracks
try:
    import configparser
except ImportError:
    print("Module: configparser not found.")


def make_track_set(raw_set, x_id, y_id, x_move_id, y_move_id, extra_ids=None):
    new_tracks = []
    for raw_track in raw_set:
        track = pytracks.tracks.Track(extra_ids)
        track.origin = (raw_track[0][x_id] - raw_track[0][x_move_id], raw_track[0][y_id] - raw_track[0][y_move_id])
        for raw_tick in raw_track:
            track.x = numpy.append(track.x, raw_tick[x_id])
            track.y = numpy.append(track.y, raw_tick[y_id])
            if extra_ids is not None:
                for current_extra_id in range(len(extra_ids)):
                    numpy.append(track.extra[current_extra_id], raw_tick[extra_ids[current_extra_id]])
        new_tracks.append(track)
    return pytracks.tracks.TrackSet(new_tracks)


def get_grid_size(grid_set, x_id, y_id):
    return grid_set[-1][x_id], grid_set[-1][y_id]


class DataWrapper:

    # The config file parser class
    config = configparser.ConfigParser()

    # The formatted data
    data = None

    raw_data = None

    # Read and format everything in on class init
    def __init__(self, config_file):
        fixed_config_file = os.path.abspath(config_file)

        # Read config file
        try:
            self.config.read(fixed_config_file)
        except (IOError, FileNotFoundError):
            print("Config file not found: ", fixed_config_file)

        # Load the raw data from the file using numpy.loadtxt
        self.raw_data = numpy.loadtxt(os.path.abspath(self.config.get("Main", "Source")))

        # Start splitting the data into sets according to the SectionID config option. Split data again if needed.
        if self.config.has_option("Main", "SectionID"):
            sectioned_data = self.__split_data(self.raw_data, self.config.getint("Main", "SectionID"))
            if self.config.has_option("Main", "SubSplitID"):
                sections_builder = []
                for section in sectioned_data:
                    sections_builder.append(self.__split_data(section, self.config.getint("Main", "SubSplitID")))
                self.data = sections_builder
            else:
                self.data = sectioned_data
        else:
            self.data = self.raw_data

    # An internal method to split data according to an ID specified
    def __split_data(self, _data, id):
            # Sort the incoming data according to the specific column index. Mergesort used to keep original order.
            sorted_data = _data[_data[:,id].argsort(kind="mergesort")]

            # Get the column which we are interested in sorting to
            ids = sorted_data[:,id]

            # Find where each element is different from it's neighbor and add 1 to get the right splitting point
            id_indexes = [j + 1 for j in numpy.where(ids[:-1] != ids[1:])[0]]

            return numpy.split(sorted_data, id_indexes)
