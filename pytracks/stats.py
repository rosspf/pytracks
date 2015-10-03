import numpy
import pytracks.track
from prettytable import PrettyTable


def gen_stats_trackset(trackset):
    if isinstance(trackset, pytracks.track.TrackSet):
        names = ["Growth", "Mortality", "Worth", "Weight", "Net Dist", "Total Dist", "Tick Dist", "Lifetime"]
        extra_ids = range(len(trackset[0].extra))
        names.extend(["Extra {0}".format(id) for id in extra_ids])
        data = [trackset.growths(),
                trackset.mortalities(),
                trackset.worths(),
                trackset.weights(),
                [track.distance_net for track in trackset],
                [track.distance_total for track in trackset],
                [track.distances for track in trackset],
                [track.lifetime for track in trackset]]
        data.extend(trackset.extras(id) for id in extra_ids)
        table = PrettyTable()
        functions = {"Max": numpy.amax, "Min": numpy.amin, "Average": numpy.average, "Median": numpy.median, "Variance": numpy.var}

        table.add_column("Variable", names)

        for key in functions:
            column = [round(functions[key](d), 3) for d in data]
            table.add_column(key, column)

        return table

    else:
        raise TypeError("Statistics can only be generated with TrackSets.")
