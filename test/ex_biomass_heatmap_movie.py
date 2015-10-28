import pytracks.input
import pytracks.track
import matplotlib.pyplot as mplot
import math
import numpy

grid_wrapper = pytracks.input.GridWrapper("HMRC_100/grid.out", extra_ids=[3, 4])
tracks_wrapper = pytracks.input.TrackWrapper("HMRC_100/HMRC_20.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

grid = grid_wrapper.gen_grid()
trackset = tracks_wrapper.gen_trackset()

plots_data = []

for tick in range(len(trackset[0])):
    image_data = numpy.zeros(grid.size)
    for track in trackset:
        x_coord = math.floor(track.x[tick]/100)
        y_coord = math.floor(track.y[tick]/100)
        image_data[y_coord - 1][x_coord - 1] += track.biomasses[tick]
    plots_data.append(image_data)

max_biomass = int(round(numpy.amax(plots_data)))

for (data, tick) in zip(plots_data, range(len(trackset[0]))):
    figure, axis = mplot.subplots(figsize=(7, 7))
    axis.set_xlim([0, 25])
    axis.set_ylim([0, 25])
    axis.set_title("Biomass - Tick {0}".format(tick))
    cbar = axis.imshow(data, interpolation='none', origin="lower", cmap=mplot.get_cmap("afmhot"), vmin=0, vmax=max_biomass, extent=[0, 25, 0, 25], aspect="equal")
    colorbar = mplot.colorbar(cbar)
    colorbar.set_ticks([0, max_biomass])
    colorbar.set_ticklabels(["Low", "High"])
    colorbar.set_label("Biomass Concentration")
    mplot.savefig("movie_HMRC_100_out/{0}.png".format(str(tick).zfill(4)))
    mplot.close()
