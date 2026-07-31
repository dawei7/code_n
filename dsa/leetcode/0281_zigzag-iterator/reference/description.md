## Description

Create an iterator for two integer vectors, `v1` and `v2`, that returns their elements alternately, beginning with `v1`. When one vector has no remaining element, iteration continues through the other vector without discarding any values.

The `ZigzagIterator` class provides these operations:

- `ZigzagIterator(List<int> v1, List<int> v2)` initializes the iterator with the two vectors.
- `boolean hasNext()` reports whether another element can be returned.
- `int next()` returns the next element in the alternating traversal.
