.. input:

.. py:module:: pytracks.input

===============================
API - ``pytracks.input`` Module
===============================

This module helps inputting raw text data into pytracks's data wrappers. Please see the examples included to learn how to use it.

.. note::

   All of the ids you specify reference indexes in an array, so they always start at 0.

TrackWrapper
============

.. py:class:: TrackWrapper(data_file, sectioned, id_column, x_column, y_column, g_column, m_column, worth_column, weight_column, extra_ids)

   :param string data_file: Path to the datafile.
   :param boolean sectioned: If the file has multiple sets of data in it. Default is True.
   :param int id_column: The column index holding the id data. Default is 1.
   :param int x_column: The column index holding the x data. Default is 2.
   :param int y_column: The column index holding the y data. Default is 3.
   :param int g_column: The column index holding the growth data. Default is 4.
   :param int m_column: The column index holding the mortality data. Default is 5.
   :param int worth_column: The column index holding the worth data. Default is 6.
   :param int weight_column: The column index holding the weight data. Default is 7
   :param extra_ids: A list of indexes. The column indexes holding the the extra data desired. Default is None.
   :type extra_ids: list of ints

   .. py:data:: data

      The list holding all the raw data read in from the file.

   .. py:data:: data_ids

      The list holding the specified ids for the required columns.

   .. py:data:: extra_ids

      The list holding the specified ids for the extra columns desired by the user.

   .. py:classmethod:: gen_trackset(index)

      :param int index: The desired dataset if the data file is sectioned. Default is 0.
      :return: A generated :class:`pytracks.track.TrackSet`.

      Generates a :class:`pytracks.track.TrackSet` object from the raw data.

GridWrapper
===========

.. py:class:: GridWrapper(data_file, sectioned, x_column, y_column, extra_ids)

   :param string data_file: Path to the datafile.
   :param boolean sectioned: If the file has multiple sets of data in it. Default is True.
   :param int x_column: The column index holding the x data. Default is 1.
   :param int y_column: The column index holding the y data. Default is 2.
   :param extra_ids: A list of indexes. The column indexes holding the the extra data desired. Default is None.
   :type extra_ids: list of ints

   .. py:data:: data

      The list holding all the raw data read in from the file.

   .. py:data:: data_ids

      The list holding the specified ids for the required columns.

   .. py:data:: extra_ids

      The list holding the specified ids for the extra columns desired by the user.

   .. py:classmethod:: gen_grid(index)

      :param int index: The desired dataset if the data file is sectioned. Default is 0.
      :return: A generated :class:`pytracks.grid.Grid`.

      Generates a :class:`pytracks.grid.Grid` object from the raw data.

Extra Methods
=============

.. py:function:: split_data(data, split_id)

   :param data: 2D raw data.
   :type data: list of lists
   :param int split_id: The index on which to split the data.
   
   A method to split the data according to an ID specified. Possibly useful to the user.

.. py:function:: get_data(data_file, sectioned)

   :param string data_file: A path to a raw data file. Can be a relative or absolute path.
   :param boolean sectioned: If sectioned, split the data on the first column.

   A method to read in raw data. Not useful to the user.