## Description

You receive non-overlapping intervals `intervals`, where `intervals[i] = [start_i, end_i]`. They are already sorted in ascending order by `start_i`. A separate pair `newInterval = [start, end]` describes one more interval.

Insert `newInterval` so that the resulting intervals remain sorted by their starts and remain mutually non-overlapping. Merge any intervals that overlap because of the insertion, then return the resulting array.

The input does not need to be modified in place; returning a newly allocated array is allowed.
