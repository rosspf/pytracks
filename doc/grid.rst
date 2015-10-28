.. grid:

.. py:module:: pytracks.grid

==============================
API - ``pytracks.grid`` Module
==============================

This module helps wrap data describing a Grid. Please see the examples included to learn how to use it.

Grid
====

.. py:class:: Grid(cells)

   :param Cell cells: A list of :class:`Cell` objects to seed the current :class:`Grid` with.

   Encapsulates a set of :class:`Cell` objects with helper methods to more easily manipulate them. Other features besides the internal methods are shown below.

   The :class:`Cell` objects encapsulated can also be accessed by specifying an index::

      >>> c1 = Cell(1, 1, [1.4, 5.3])
      >>> c2 = Cell(1, 2, [1.5, 5.0])
      >>> c3 = Cell(1, 3, [1.0, 4.8])
      >>> g = Grid([c1, c2, c3])
      >>> g[0]
      <pytracks.grid.Cell object at 0x7f86b1704908>
      >>> c1
      <pytracks.grid.Cell object at 0x7f86b1704908>

   The number of :class:`Cell` objects in the current :class:`Grid` can be measured by len()::

      >>> len(g)
      3

   The :class:`Grid` class has the ability to iterate over every :class:`Cell` object in the current :class:`Grid`::

      >>> for c in g:
      ...    print(c.point)
      ... 
      (1, 1)
      (1, 2)
      (1, 3)

   .. py:data:: cells

      A list which composes of multiple :class:`Cell` classes in the current :class:`Grid`.

   .. py:data:: size

      The size of the current :class:`Grid` which is a tuple of form (w, h).

Cell
====

.. py:class:: Cell(x, y, data)

   :param int x: The x coordinate of the cell.
   :param int y: The y coordinate of the cell.
   :param list data: The extra data describing the cell.

   Wraps the data describing a single cell. Other features besides the internal methods are shown below.

   The data encapsulated can also be accessed as if the current :class:`Cell` class was the data list itself by specifying an index::

      >>> c = Cell(0, 10, [1.4, 5.3])
      >>> c.data[1]
      5.3
      >>> c[1]
      5.3
   
   The amount of data stored in the current :class:`Cell` can be measured by len()::
   
      >>> len(c)
      2

   .. py:data:: x

      The x coordinate of the current :class:`Cell`.

   .. py:data:: y

      The y coordinate of the current :class:`Cell`.

   .. py:data:: data

      An array of the data specified to be included.

   .. py:data:: point

      The coordinate of the current :class:`Cell` in a tuple of form (x, y).
