class Grid:

    def __init__(self, cells):
        self.cells = cells

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        return iter(self.cells)

    def __getitem__(self, item):
        return self.cells[item]

    @property
    def size(self):
        return self.cells[-1].point

class Cell:

    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.__data = data

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    @property
    def point(self):
        return self.x, self.y