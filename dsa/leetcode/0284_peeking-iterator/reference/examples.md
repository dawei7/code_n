## Examples

**Example 1**

- Input: `operations = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"], arguments = [[[1, 2, 3]], [], [], [], [], []]`
- Output: `[null, 1, 2, 2, 3, false]`
- Explanation: Constructing the iterator over `[1, 2, 3]` produces no return value. The first `next()` returns `1` and advances. `peek()` then reports `2` without moving. The following two `next()` calls return `2` and `3`, respectively. Finally, `hasNext()` returns `false` because no elements remain.
