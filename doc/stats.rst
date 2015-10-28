.. stats:

.. py:module:: pytracks.stats

===============================
API - ``pytracks.stats`` Module
===============================

This module has the ability to call methods to help with the creation of statistics. It is useful to see what range of data your file contains.

Methods
=======

.. py:method:: gen_stats_trackset(trackset)

   :param TrackSet trackset: The trackset to perform analysis on.
   :return: A table in string form.
   :raises: TypeError: If a :class:`pytracks.track.TrackSet` object is not passed.

   Takes a :class:`pytracks.track.TrackSet` object and generates statistics on it.