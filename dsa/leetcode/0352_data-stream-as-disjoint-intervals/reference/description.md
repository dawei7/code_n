## Description

A stream supplies nonnegative integers $a_1,a_2,\ldots,a_n$. Summarize all values observed so far as a sorted list of disjoint intervals.

Implement the `SummaryRanges` class:

- `SummaryRanges()` creates an object whose stream is initially empty.
- `void addNum(int value)` adds `value` to the stream.
- `int[][] getIntervals()` returns the currently observed integers as disjoint inclusive intervals `[start_i,end_i]`, ordered by increasing `start_i`.
