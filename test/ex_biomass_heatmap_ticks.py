import pytracks.input
import pytracks.track
import matplotlib.pyplot as plot
import math
import numpy

grid_wrapper = pytracks.input.GridWrapper("HMRC_100/grid.out", extra_ids=[3, 4])
tracks_wrapper = pytracks.input.TrackWrapper("HMRC_100/HMRC_20.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

grid = grid_wrapper.gen_grid()
trackset = tracks_wrapper.gen_trackset()

plots_data = numpy.array([numpy.zeros(grid.size) for _ in range(4)])

figure, axlist = plot.subplots(nrows=2, ncols=2, sharex="col", sharey="row", figsize=(6, 7))
titles = ["Biomass - Tick ", "Biomass - Tick ", "Biomass - Tick ", "Biomass - Tick "]

tl = len(trackset[0]) - 1

ticks = [0, int(round(tl * 0.33)), int(round(tl * 0.66)), tl]

for i in range(4):
    for track in trackset:
        x_coord = math.floor(track.x[ticks[i]]/100)
        y_coord = math.floor(track.y[ticks[i]]/100)
        plots_data[i][y_coord - 1][x_coord - 1] += track.biomasses[ticks[i]]
    titles[i] += str(ticks[i])

max_biomass = int(round(numpy.percentile(plots_data.flatten(), 99.75)))

for axis, plot_data, title in zip(axlist.flat, plots_data, titles):
    axis.set_xlim([0, 25])
    axis.set_ylim([0, 25])
    axis.set_title(title)
    cbar = axis.imshow(plot_data, interpolation='none', origin="lower", cmap=plot.get_cmap("hot"), vmin=0, vmax=max_biomass, extent=[0, 25, 0, 25], aspect="equal")

figure.subplots_adjust(bottom=0.235)
colorbar_axis = figure.add_axes([0.15, .12, .73, .05])

colorbar = plot.colorbar(cbar, cax=colorbar_axis, orientation="horizontal")
colorbar.set_ticks([0, max_biomass])
colorbar.set_ticklabels(["Low", "High"])
colorbar.set_label("Biomass Concentration")

plot.savefig("export/ticks_heatmap.pdf", bbox_inches='tight', transparent=True)
plot.show()
