# Peeking Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 284 |
| Difficulty | Medium |
| Topics | Array, Design, Iterator |
| Official Link | [peeking-iterator](https://leetcode.com/problems/peeking-iterator/) |

## Problem Description & Examples
### Goal
Design an iterator class that extends the functionality of a standard iterator by allowing a "peek" operation. This operation retrieves the next element in the sequence without advancing the iterator's internal pointer, effectively allowing the user to preview the upcoming value before consuming it.

### Function Contract
**Inputs**

- `iterator`: An object providing `next()` (returns the next element) and `hasNext()` (returns a boolean indicating if more elements exist).

**Return value**

- `peek()`: Returns the next element without advancing the iterator.
- `next()`: Returns the next element and advances the iterator.
- `hasNext()`: Returns true if there are elements remaining.

### Examples
**Example 1**

- Input: `["PeekingIterator", "next", "peek", "next", "next", "hasNext"]`
  `[[[1, 2, 3]], [], [], [], [], []]`
- Output: `[null, 1, 2, 2, 3, false]`

**Example 2**

- Input: `["PeekingIterator", "hasNext", "peek", "next", "next", "hasNext"]`
  `[[[1, 2, 3]], [], [], [], [], []]`
- Output: `[null, true, 1, 1, 2, true]`

**Example 3**

- Input: `["PeekingIterator", "hasNext", "peek", "next", "hasNext"]`
  `[[[1]], [], [], [], []]`
- Output: `[null, true, 1, 1, false]`

---

## Underlying Base Algorithm(s)
The solution utilizes a "look-ahead" buffer strategy. By maintaining a cached variable that stores the next element to be returned, we can satisfy the `peek()` request immediately. The `next()` operation then returns the cached value and fetches the subsequent element from the underlying iterator to refill the buffer.

---

## Complexity Analysis
- **Time Complexity**: O(1) for all operations (`peek`, `next`, `hasNext`), as each operation performs a constant number of steps regardless of the iterator size.
- **Space Complexity**: O(1), as we only store a single cached element regardless of the total number of elements in the iterator.
