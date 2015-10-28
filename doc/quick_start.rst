.. quick_start:

===========
Quick Start
===========

This is a short guide on how to quickly start using ``pytracks``. If you require more detail please read the API documents or examine the included examples.

Wrap Raw Data Files
===================

To initialize the data files, one could wrap the files like below. The tracks_wrapper has non default id columns specified. Example::

   grid_w = GridWrapper("grid.out", extra_ids=[3, 4])
   track_w = TrackWrapper("Event_5.out", id_column=2, x_column=5, y_column=7, extra_ids=[10, 11])

Generate a :class:`pytracks.grid.Grid` or :class:`pytracks.track.TrackSet`
==========================================================================

:class:`pytracks.input.GridWrapper` and :class:`pytracks.input.TrackWrapper` have methods which can be used to generate a :class:`pytracks.grid.Grid` or :class:`pytracks.track.TrackSet`::

   grid = grid_wrapper.gen_grid()
   trackset = tracks_wrapper.gen_trackset()

After Genereration
==================

Use your imagination! Reference the API to see all the build in methods.::

   for track in trackset:
      print("Did I (id {0}) survive? {1}".format(int(track.ids[0]), track.survived))

Output::

   Did I (id 30) survive? True
   Did I (id 60) survive? True
   Did I (id 90) survive? True
   ...

