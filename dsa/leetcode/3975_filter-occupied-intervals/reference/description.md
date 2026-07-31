## Description

You receive a collection of inclusive integer intervals named `occupiedIntervals`. An interval `[start, end]` marks every integer point from `start` through `end` as occupied. The supplied intervals may overlap and may appear in any order.

First combine every pair or chain of occupied intervals that overlaps or touches. Here, touching has a discrete meaning: an interval beginning exactly one integer after another interval ends is contiguous with it. For example, `[1,1]` and `[2,2]` combine into `[1,2]`.

The inclusive interval from `freeStart` through `freeEnd` is free time. Remove every integer point in that interval from the merged occupied set. Return the occupied portions that remain, ordered by their starting points. They must be pairwise non-overlapping and represented with the fewest possible intervals. Return an empty list when the free interval removes every occupied point.
