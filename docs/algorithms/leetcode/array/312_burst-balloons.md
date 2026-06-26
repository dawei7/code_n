# Burst Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_205` |
| Frontend ID | 312 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [burst-balloons](https://leetcode.com/problems/burst-balloons/) |

## Problem Description & Examples
### Goal
You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `i`-th balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon painted with a `1` on it.

Return the maximum coins you can collect by bursting the balloons wisely.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - maximum coins collected

### Examples
**Example 1**

- Input: `nums = [3, 1, 5, 8]`
- Output: `167`

**Example 2**

- Input: `nums = [7, 1]`
- Output: `14`

**Example 3**

- Input: `nums = [10, 2]`
- Output: `30`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
