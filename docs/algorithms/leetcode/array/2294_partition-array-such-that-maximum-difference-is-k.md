# Partition Array Such That Maximum Difference Is K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2294 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [partition-array-such-that-maximum-difference-is-k](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/) |

## Problem Description & Examples
### Goal
Partition all array elements into the fewest nonempty subsequences such that each group's maximum minus minimum is at most `k`. Original ordering within subsequences imposes no restriction on grouping.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: the maximum spread allowed within a group.

**Return value**

The minimum number of subsequences required.

### Examples
**Example 1**

- Input: `nums = [3, 6, 1, 2, 5]`, `k = 2`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 3]`, `k = 0`
- Output: `3`

**Example 3**

- Input: `nums = [4, 4, 4]`, `k = 0`
- Output: `1`

---

## Underlying Base Algorithm(s)
Sort the values. Start a group at the smallest unassigned value and include every following value no more than `k` above it. When one exceeds that bound, start the next group there. Taking the widest valid group from each smallest remaining value is greedily optimal.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place
