import pytracks.input
import pytracks.track
import matplotlib.pyplot as plot
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy
import random

def codes(track):
    return [Path.MOVETO].extend([Path.LINETO] * (track.lifetime - 1))

grid_wrapper = pytracks.input.GridWrapper("event_25/grid.out", extra_ids=[3, 4])
tracks_wrapper = pytracks.input.TrackWrapper("event_25/Event_5.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

grid = grid_wrapper.gen_grid()
trackset = tracks_wrapper.gen_trackset()

plot_data = numpy.zeros(grid.size)
for cell in grid.cells:
    plot_data[cell.y - 1][cell.x - 1] = (cell[0] - cell[1])

figure, axis = plot.subplots(figsize=(5, 5))

x,y = zip(*trackset.points(pytracks.track.last))
xx = [l / 25 for l in x]
yy = [l / 25 for l in y]
N = len(trackset)
area = numpy.pi * (3)**2 # radius of 5

plot.scatter(xx, yy, c="red", s=area)

axis.set_title("TrackSet End Points")
axis.set_xlim([0, 100])
axis.set_ylim([0, 100])

grid_image = axis.imshow(plot_data, interpolation='none', origin="lower", cmap=plot.get_cmap("Blues_r"), vmin=-1, vmax=1, extent=[0, 100, 0, 100], aspect="equal")
colorbar = plot.colorbar(grid_image)
colorbar.set_ticks([-1, 0, 1])
colorbar.set_ticklabels([-1, 0, 1])
colorbar.set_label("Habitat Quality")

plot.savefig("export/end_points.png", bbox_inches='tight', transparent=True)
plot.show()
