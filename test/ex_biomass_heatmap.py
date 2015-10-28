import pytracks.input
import pytracks.track
import matplotlib.pyplot as plot
import math
import numpy

grid_wrapper = pytracks.input.GridWrapper("event_25/grid.out", extra_ids=[3, 4])
tracks_wrapper = pytracks.input.TrackWrapper("event_25/Event_5.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

grid = grid_wrapper.gen_grid()
trackset = tracks_wrapper.gen_trackset()

plot_data = numpy.zeros(grid.size)
print(plot_data)

figure, axis = plot.subplots(figsize=(5, 5))

for track in trackset:
    for tick in range(len(track)):
        x_coord = math.floor(track.x[tick]/25)
        y_coord = math.floor(track.y[tick]/25)
        plot_data[y_coord - 1][x_coord - 1] += track.biomasses[tick]

max_biomass = int(round(numpy.amax(plot_data)))

axis.set_title("Cumulative Biomass Heatmap")
axis.set_xlim([0, 100])
axis.set_ylim([0, 100])
print(plot_data.size)

grid_image = axis.imshow(plot_data, interpolation='none', origin="lower", cmap=plot.get_cmap("afmhot"), vmin=0, vmax=max_biomass, extent=[0, 100, 0, 100], aspect="equal")
colorbar = plot.colorbar(grid_image)
colorbar.set_ticks([0, max_biomass])
colorbar.set_ticklabels(["Low", "High"])
colorbar.set_label("Biomass Concentration")

plot.savefig("export/cumulative_heatmap.png", bbox_inches='tight', transparent=True)
plot.show()
