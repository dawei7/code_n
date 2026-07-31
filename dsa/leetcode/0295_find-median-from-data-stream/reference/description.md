## Description

The median of an ordered integer list is its middle value. When the list length is even, use the mean of the two middle values instead. For example, `[2,3,4]` has median `3`, while `[2,3]` has median `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` creates an empty median tracker.
- `void addNum(int num)` adds `num` from the data stream.
- `double findMedian()` returns the median of every value received so far. Answers within $10^{-5}$ of the exact result are accepted.
