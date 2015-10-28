.. data_format:

============================
Raw Data Format Requirements
============================

This article explains the format in which the data must be in.

File Requirements
=================

1. Raw text file
2. One entry per line
3. Tab or whitespace seperated
4. File can hold multiple sets of data. See the Sectioned parameter in the input methods in ``pytracks.input``.

.. note::

   The following tables describe the format of a valid data file with data in it. The values below are the default ids used in the program. Every column ID can be changed except ``Sec ID``, which must be the first column and thus have an ID of 0. You can have multiple extra data columns, which must be specified when wrapping the data file with the appropiate function.

Tracks File
===========

.. table::

   ====== ======== === === ====== ========= ===== ====== =====
   Sec ID Track ID  X   Y  Growth Mortality Worth Weight Extra
   ------ -------- --- --- ------ --------- ----- ------ -----
      0       1     2   3     4       5       6      7    8-N
   ====== ======== === === ====== ========= ===== ====== =====

Grid File
=========

.. table::

   ====== ======== === === =====
   Sec ID Track ID  X   Y  Extra
   ------ -------- --- --- -----
      0       1     2   3   4-N
   ====== ======== === === =====