# K Empty Slots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 683 |
| Difficulty | Hard |
| Topics | Array, Binary Indexed Tree, Segment Tree, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/k-empty-slots/) |

## Problem Description
### Goal
There are `n` bulbs arranged at positions `1` through `n`, initially all off. On day `i`, the bulb at position `bulbs[i]` turns on, and the array is a permutation so exactly one previously unlit bulb is activated each day.

Return the earliest one-based day on which two turned-on bulbs have exactly `k` bulbs between them and all `k` intermediate bulbs are still off. The endpoint positions therefore differ by $k + 1$. Return `-1` if no day ever satisfies this condition.

### Function Contract
**Inputs**

- `bulbs`: a permutation where `bulbs[day - 1]` is the position switched on that day
- `k`: the required number of unlit positions strictly between the two lit endpoints

**Return value**

- The earliest 1-based day satisfying the condition, or `-1` when no such day exists

### Examples
**Example 1**

- Input: `bulbs = [1,3,2], k = 1`
- Output: `2`

**Example 2**

- Input: `bulbs = [1,2,3], k = 1`
- Output: `-1`

**Example 3**

- Input: `bulbs = [2,1,3], k = 0`
- Output: `2`
