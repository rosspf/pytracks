import numpy

class Grid:

    def __init__(self, cells):
        self._cells = cells

    @property
    def size(self):
        return self._cells[-1].point

    @property
    def cells(self):
        return self._cells

class Cell:

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self._data = data

    @property
    def point(self):
        return (self.x, self.y)

    def get_data(self, id):
        return self._data[id]

"""
        grid_builder = numpy.full(self.get_required_size(id), None).tolist()
        for cell in self.data[id]:
            data_extra = []
            if self.extra_ids is not None:
                data_extra = [cell[e] for e in self.extra_ids]
            print(int(cell[self.data_ids[0]]) - 1)
            print(int(cell[self.data_ids[1]]) - 1)
            grid_builder[int(cell[self.data_ids[0]]) - 1][int(cell[self.data_ids[1]]) - 1] = data_extra
        return pytracks.grid.Grid(grid_builder)
"""