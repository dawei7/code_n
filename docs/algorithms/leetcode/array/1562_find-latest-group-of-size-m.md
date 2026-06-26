# Find Latest Group of Size M

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1562 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Simulation |
| Official Link | [find-latest-group-of-size-m](https://leetcode.com/problems/find-latest-group-of-size-m/) |

## Problem Description & Examples
### Goal
Bits are turned from `0` to `1` in the order given by `arr`. Find the latest step
where there exists a contiguous group of exactly `m` ones.

### Function Contract
**Inputs**

- `arr`: the 1-based positions turned on at each step.
- `m`: the target group length.

**Return value**

The latest step containing a group of exactly `m` ones, or `-1` if it never
happens.

### Examples
**Example 1**

- Input: `arr = [3, 5, 1, 2, 4], m = 1`
- Output: `4`

**Example 2**

- Input: `arr = [3, 1, 5, 4, 2], m = 2`
- Output: `-1`

**Example 3**

- Input: `arr = [1, 2, 3], m = 3`
- Output: `3`

---

## Underlying Base Algorithm(s)
Maintain the lengths of one-groups at their boundary positions and a count of
how many groups currently have each length. When turning on position `x`, merge
the group ending at `x - 1` and the group starting at `x + 1`, update the length
counts, and record the step whenever the count for length `m` is positive.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.
