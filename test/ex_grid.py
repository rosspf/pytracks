import pytracks.input
import pytracks.track
import matplotlib.pyplot as plot
import numpy

grid_wrapper = pytracks.input.GridWrapper("event_25/grid.out", extra_ids=[3, 4])

grid = grid_wrapper.gen_grid()

plot_data = numpy.zeros(grid.size)
for cell in grid.cells:
    plot_data[cell.y - 1][cell.x - 1] = (cell[0] - cell[1])

figure, axis = plot.subplots(figsize=(6, 7))

grid_image = axis.imshow(plot_data, interpolation='none', origin="lower", cmap=plot.get_cmap("Blues_r"), vmin=-1, vmax=1, extent=[0, 100, 0, 100], aspect="equal")

figure.subplots_adjust(bottom=0.235)
colorbar_axis = figure.add_axes([0.15, .12, .73, .05])

axis.set_title("Grid Visualization")
colorbar = plot.colorbar(grid_image, cax=colorbar_axis, orientation='horizontal')
colorbar.set_ticks([-1, 0, 1])
colorbar.set_ticklabels([-1, 0, 1])
colorbar.set_label("Habitat Quality")

plot.savefig("export/grid.pdf", bbox_inches='tight', transparent=True)
plot.show()