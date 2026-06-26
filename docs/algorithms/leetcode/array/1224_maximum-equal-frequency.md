# Maximum Equal Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1224 |
| Difficulty | Hard |
| Topics | Array, Hash Table |
| Official Link | [maximum-equal-frequency](https://leetcode.com/problems/maximum-equal-frequency/) |

## Problem Description & Examples
### Goal
Find the longest prefix such that, after removing exactly one element from that prefix, every remaining distinct number appears the same number of times.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The maximum valid prefix length.

### Examples
**Example 1**

- Input: `nums = [2,2,1,1,5,3,3,5]`
- Output: `7`

**Example 2**

- Input: `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`
- Output: `13`

**Example 3**

- Input: `nums = [1,1,1,2,2,2]`
- Output: `5`

---

## Underlying Base Algorithm(s)
Frequency counting with frequency-of-frequency invariants.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
