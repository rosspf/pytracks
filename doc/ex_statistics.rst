.. ex_statistics:

==============================
Example - Statistic Generation
==============================

This example simply uses the built in statistic generation method to survey the data you will be processing.

Code
====

.. literalinclude:: ../../pytracks/test_suite/ex_statistics.py
   :language: python

Output
======

Raw Output::

   +------------+-----------+-----------+-----------+----------+-------------+
   |  Variable  |    Min    |    Max    |   Median  | Average  |   Variance  |
   +------------+-----------+-----------+-----------+----------+-------------+
   |   Growth   |    0.0    |   0.926   |   0.462   |  0.454   |    0.052    |
   | Mortality  |    0.0    |    1.0    |    0.0    |  0.016   |    0.009    |
   |   Worth    |   95.582  |   100.0   |   99.269  |  99.105  |    0.546    |
   |   Weight   |   4.008   |   5.286   |   4.464   |  4.479   |    0.087    |
   |  Net Dist  |  158.146  |  2599.657 |  944.418  | 1056.299 |  380391.991 |
   | Total Dist | 26297.969 | 39211.338 | 31297.829 | 31385.11 | 7967645.867 |
   | Tick Dist  |   7.014   |  188.468  |   28.811  |  36.367  |   311.847   |
   |  Lifetime  |    864    |    864    |   864.0   |  864.0   |     0.0     |
   |  Extra 0   |    0.0    |   0.926   |   0.462   |  0.454   |    0.052    |
   +------------+-----------+-----------+-----------+----------+-------------+