.. ex_biomass_heatmap_movie:

===============================
Example - Biomass Heatmap Movie
===============================

This example will create a graph for every tick. We will then use `ffmpeg <https://www.ffmpeg.org/>`_ to encode it into a movie which can then be played in any media player.

Code
====

.. literalinclude:: ../../pytracks/test_suite/ex_biomass_heatmap_ticks.py
   :language: python

Post-Processing
===============

`ffmpeg <https://www.ffmpeg.org/>`_ is used to assemble the png files saved by the python script into a m4v video::

   $ ffmpeg -r 10 -f image2 -i %04d.png -vcodec libx264 -b 500k biomass_heatmap_movie_out.m4v

or in gif format::

   $ ffmpeg -r 10 -f image2 -i %04d.png biomass_heatmap_movie_out.gif

Output
======

#.. image:: example_images/biomass_heatmap_movie_out.gif
