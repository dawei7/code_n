# Maximum Number of Groups Getting Fresh Donuts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1815 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Memoization, Bitmask |
| Official Link | [maximum-number-of-groups-getting-fresh-donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/) |

## Problem Description & Examples
### Goal
A bakery makes donuts in batches of size `batchSize`. Groups arrive and take their group size in donuts. A group is happy if the first donut they get is fresh from a new batch. Reorder groups to maximize happy groups.

### Function Contract
**Inputs**

- `batchSize`: the donut batch size.
- `groups`: group sizes.

**Return value**

Return the maximum number of happy groups.

### Examples
**Example 1**

- Input: `batchSize = 3, groups = [1,2,3,4,5,6]`
- Output: `4`

**Example 2**

- Input: `batchSize = 4, groups = [1,3,2,5,2,2,1,6]`
- Output: `4`

**Example 3**

- Input: `batchSize = 2, groups = [1,1,1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Only group sizes modulo `batchSize` matter. Groups with remainder `0` are always happy. Pair complementary remainders greedily where possible, then solve the remaining counts with memoized DFS over remainder-count state and current leftover batch remainder. A group is happy when the current leftover is `0` before serving it.

---

## Complexity Analysis
- **Time Complexity**: `O(states * batchSize)`
- **Space Complexity**: `O(states)`
