.. track:

.. py:module:: pytracks.track

===============================
API - ``pytracks.track`` Module
===============================

This is the main module of pytracks which wraps data descibing movement tracks. Please see the examples included to learn how to use it.

.. note::

   In the documentation below a few private methods (methods which begin with an underscore) are documented. Most people can ignore these as they are only useful if the developer wishes to override them. (Which I wouldn't advise as they work perfectly well!)

TrackSet
========

.. py:class:: TrackSet(tracks)

   :param list tracks: The :class:`Track` objects to seed the current :class:`TrackSet` with.

   Encapsulates a set of :class:`Track` objects with helper methods to more easily manipulate them. Other features besides the internal methods are shown below.

   The :class:`Track` objects encapsulated can also be accessed by specifying an index after the object::

      >>> ts
      <pytracks.track.TrackSet object at 0x7f9f4eb9ce10>
      >>> ts.tracks[0]
      <pytracks.track.Track object at 0x7f9f3f8b5908>
      >>> ts[0]
      <pytracks.track.Track object at 0x7f9f3f8b5908>

   The number of :class:`Track` objects in the current :class:`TrackSet` can be measured by len()::

      >>> len(ts)
      100

   The :class:`TrackSet` class has the ability to iterate over every :class:`Track` object in the current :class:`TrackSet`::

      >>> for t in ts:
      ...     print(t.distance_net)
      ... 
      1980.999839794037
      ...
      739.8863745751776

   :class:`TrackSet` objects can be combined with other :class:`TrackSet` objects via the addition operator::

      >>> ts_new = ts + ts
      >>> len(ts_new)
      200

   .. py:data:: tracks

      A list which composes of multiple :class:`Track` objects in the current :class:`TrackSet`.

   .. py:staticmethod:: _point_in_rectangle(point, p1, p2)

      :param tuple point: The point to be tested.
      :param tuple p1: The first point of the rectangle.
      :param tuple p2: The other point of the rectangle.
      :return: True/False if the point is within the defined rectangle.

      An internal method which tests if a point is within a defined rectangle.

   .. py:staticmethod:: _point_in_circle(point, center, radius)

      :param tuple point: The point to be tested.
      :param tuple center: The center point of the desired circle.
      :param float radius: The radius of the desired circle.
      :return: True/False if the point is within the defined circle.
  
      An internal method which tests if a point is within a defined circle.

   .. py:classmethod:: append(other)

      :param TrackSet other: The other :class:`TrackSet` to append.
      :return: A combined :class:`TrackSet`.
      :raises: TypeError: If other is not of type :class:`TrackSet`.
      
      Append a :class:`TrackSet` class to the current one.

   .. py:classmethod:: points(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every points attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: growths(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every growths attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: mortalities(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every mortalities attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: habitat_qualities(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every habitat_qualities attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: worths(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every worths attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: weights(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every weights attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: biomasses(f)

      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every biomasses array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: extras(element_id, f)

      :param int element_id: The extras id desired.
      :param method f: The method to run on each attribute array. Default returns the whole array.
      :return: A list of values for every :class:`Track` class in the current :class:`TrackSet`.
      
      Return every specified by index extras attribute array from each :class:`Track` object in the current :class:`TrackSet` and optionally run a method on each attribute array.

   .. py:classmethod:: get_tracks_id(indexes)

      :param indexes: A list of indexes. Indexes must refer to Tracks stored in the current :class:`TrackSet`.
      :type indexes: list of ints.
      :return: A new :class:`TrackSet`.
      
      Fetch specific Tracks from the current :class:`TrackSet`.

   .. py:classmethod:: get_tracks_random(num)

      :param int num: Number to randomly fetch. Default is 1. Must not be larger than the size of the :class:`TrackSet`.
      :return: A new :class:`TrackSet`.
      
      Fetch a random number of :class:`Track` objects from the current :class:`TrackSet`.

   .. py:classmethod:: get_tracks_circle(center, radius, index)

      :param tuple center: A tuple which is of the form (x, y).
      :param float radius: The search radius.
      :param int index: Which tick to look at. Default is (-1), which is the last tick.
      :return: A new :class:`TrackSet`.
      
      Get the :class:`Track` objects which are in the area specified during the tick specified.

   .. py:classmethod:: get_tracks_rectangle(p1, p2, index)

      :param tuple p1: The first point of the rectangle.
      :param tuple p2: The other point of the rectangle.
      :param int index: Which tick to look at. Default is (-1), which is the last tick.
      :return: A new :class:`TrackSet`.
      
      Get the :class:`Track` objects which are in the area specified during the tick specified.

   .. py:classmethod:: get_tracks_mortality(min_mortality, max_mortality, index)

      :param float min_mortality: The minimum mortality to search for. Default is 0.
      :param float max_mortality: The maximum mortality to search for. Default is 1.
      :param int index: Which tick to look at. Default is -1, which is the last tick.
      :return: A new :class:`TrackSet`.
      :raises: ValueError: If the minimum specified is greater than the maximum specified.
      
      Get the :class:`Track` objects which are experiencing a specified range of mortalities during the tick specified.

   .. py:classmethod:: get_tracks_growth(min_growth, max_growth, index)

      :param float min_growth: The minimum growth to search for. Default is 0.
      :param float max_growth: The maximum growth to search for. Default is 1.
      :param int index: Which tick to look at. Default is -1, which is the last tick.
      :return: A new :class:`TrackSet`.
      :raises: ValueError: If the minimum specified is greater than the maximum specified.
      
      Get the :class:`Track` objects which are experiencing a specified range of growths during the tick specified.

   .. py:classmethod:: get_tracks_growth_mortality(min_growth, max_growth, min_mortality, max_mortality, index)

      :param float min_growth: The minimum growth to search for. Default is 0.
      :param float max_growth: The maximum growth to search for. Default is 1.
      :param float min_mortality: The minimum mortality to search for. Default is 0.
      :param float max_mortality: The maximum mortality to search for. Default is 1.
      :param int index: Which tick to look at. Default is -1, which is the last tick.
      :return: A new :class:`TrackSet`.
      :raises: ValueError: If the minimum specified is greater than the maximum specified.

      Get the :class:`Track` objects which are experiencing a specified range of mortalities and growths during the tick specified.

   .. py:classmethod:: get_tracks_habitat_quality(min_quality, max_quality, index)

      :param float min_quality: The minimum habitat quality to search for. Default is -1.
      :param float max_quality: The maximum habitat quality to search for. Default is 1.
      :param int index: Which tick to look at. Default is -1, which is the last tick.
      :return: A new :class:`TrackSet`.
      :raises: ValueError: If the minimum specified is greater than the maximum specified.
      
      Get the :class:`Track` objects which are experiencing a specified habitat qualities during the tick specified.

   .. py:classmethod:: get_tracks_biomass(min_biomass, max_biomass, index)

      :param float min_biomass: The minimum biomass to search for.
      :param float max_biomass: The maximum biomass to search for.
      :param int index: Which tick to look at. Default is -1, which is the last tick.
      :return: A new :class:`TrackSet`.
      :raises: ValueError: If the minimum specified is greater than the maximum specified.
      
      Get the :class:`Track` objects which are experiencing a specified biomasses during the tick specified.

Track
=====

.. py:class:: Track

   Wraps the data describing the lifetime of a single Track.

   The data encapsulated can also be accessed as if the current :class:`Track` object was the extra data list itself by specifying an index::

      >>> t
      <pytracks.track.Track object at 0x7f9f3f8b5908>
      >>> max(t.extra[1])
      6.2800000000000002
      >>> max(t[1])
      6.2800000000000002
   
   The number of ticks the current :class:`Track` object holds can be measured by len()::
   
      >>> len(t)
      864

   .. py:data:: SURVIVAL_THRESHOLD

      A constant which defines the threshold of if the individual is still alive.

   .. py:data:: ids

      The ids column.

   .. py:data:: x

      The x coordinate for each tick.

   .. py:data:: y

      The x coordinate for each tick.

   .. py:data:: growths

      The growth attribute for each tick.

   .. py:data:: mortalities

      The mortality attribute for each tick.

   .. py:data:: worths

      The worth attribute for each tick.

   .. py:data:: weights

      The weight attribute for each tick.

   .. py:data:: distances

      The Euclidean distances between each tick.

   .. py:data:: distance_net

      The net Euclidean distance travelled.

   .. py:data:: distance_total

      The total Euclidean distance travelled.

   .. py:data:: points

      The coordinate of each tick.

   .. py:data:: habitat_qualities

      The habitat_quality attribute for each tick.

   .. py:data:: biomasses

      The biomass attribute for each tick.

   .. py:data:: survived

      If the individual survived to the end of its lifetime.

   .. py:data:: lifetime

      The tick the individual went below the :data:`SURVIVAL_THRESHOLD` constant.

   .. py:staticmethod:: distance(p1, p2)

      :param tuple p1: The first point.
      :param tuple p2: The second point.
      :return: The Euclidean distance between the two points.

      Calculate the Euclidean distance between two points.

Extra Methods
=============

.. py:function:: dummy(o)

   :param object o: An object.
   
   A method to simply return the object itself. Used to shorten code in the :class:`TrackSet` methods.

.. py:function:: first(l)

   :param list l: A list.
   
   A method to simply return the first element of the passed list. Useful in various :class:`TrackSet` methods.

.. py:function:: last(l)

   :param list l: A list.
   
   A method to simply return the last element of the passed list. Useful in various :class:`TrackSet` methods.