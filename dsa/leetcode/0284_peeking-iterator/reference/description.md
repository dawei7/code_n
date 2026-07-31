## Description

Design a wrapper around an existing iterator that adds a `peek` operation while retaining `next` and `hasNext`.

Implement the `PeekingIterator` class with these operations:

- `PeekingIterator(Iterator<int> nums)` initializes the wrapper from the supplied integer iterator.
- `int next()` returns the next value and advances to the following element.
- `boolean hasNext()` returns `true` when at least one element remains.
- `int peek()` returns the next value without advancing the iterator.
