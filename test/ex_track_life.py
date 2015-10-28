import pytracks.input
import pytracks.track
import matplotlib.pyplot as plot
from matplotlib.path import Path
from matplotlib.collections import LineCollection
import numpy

# Add in start and end points
# add in biomass at start and end


def colorline(x, y, data, normalize=plot.Normalize(0.0, 1.0)):

    z = numpy.asarray(data)

    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=plot.get_cmap('copper'), norm=normalize)

    ax = plot.gca()
    ax.add_collection(lc)

    return lc

def make_segments(x, y):

    points = numpy.array([x, y]).T.reshape(-1, 1, 2)
    segments = numpy.concatenate([points[:-1], points[1:]], axis=1)
    return segments

grid_wrapper = pytracks.input.GridWrapper("event_25/grid.out", extra_ids=[3, 4])
tracks_wrapper = pytracks.input.TrackWrapper("event_25/Event_5.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

grid = grid_wrapper.gen_grid()
trackset = tracks_wrapper.gen_trackset()

plot_data = numpy.zeros(grid.size)
for cell in grid.cells:
    plot_data[cell.y - 1][cell.x - 1] = (cell[0] - cell[1])

figure, (gridax, lineax) = plot.subplots(2, figsize=(5, 10))

newset = trackset.get_tracks_random(1)

max_biomass = numpy.amax(newset.biomasses())

track = newset[0]

path = Path(numpy.column_stack([track.x/25, track.y/25]))
verts = path.interpolated(steps=3).vertices
x, y = verts[:, 0], verts[:, 1]
data = numpy.true_divide(track.biomasses, max_biomass)
gridax.add_collection(colorline(x, y, data))

gridax.set_title("Random Tracks Example")
gridax.set_xlim([0, 100])
gridax.set_ylim([0, 100])

grid_image = gridax.imshow(plot_data, interpolation='none', origin="lower", cmap=plot.get_cmap("Blues_r"), vmin=-1, vmax=1, extent=[0, 100, 0, 100], aspect="equal")
colorbar = plot.colorbar(grid_image, ax=gridax)
colorbar.set_ticks([-1, 0, 1])
colorbar.set_ticklabels([-1, 0, 1])
colorbar.set_label("Habitat Quality")

plot.savefig("export/tracks_lifetime.png", bbox_inches='tight', transparent=True)
plot.show()
