# Pairs of Songs With Total Durations Divisible by 60

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1010 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [pairs-of-songs-with-total-durations-divisible-by-60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) |

## Problem Description & Examples
### Goal
Given song durations in seconds, count pairs whose total duration is divisible by `60`.

### Function Contract
**Inputs**

- `time`: List[int]

**Return value**

int - number of valid index pairs

### Examples
**Example 1**

- Input: `time = [30, 20, 150, 100, 40]`
- Output: `3`

**Example 2**

- Input: `time = [60, 60, 60]`
- Output: `3`

**Example 3**

- Input: `time = [10, 50, 90, 30]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Modulo-complement counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` because there are only 60 remainders
