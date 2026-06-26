# Minimum Distance to the Target Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1848 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [minimum-distance-to-the-target-element](https://leetcode.com/problems/minimum-distance-to-the-target-element/) |

## Problem Description & Examples
### Goal
Given a starting index, find the closest index whose value equals `target`.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `target`: the value to find.
- `start`: the starting index.

**Return value**

Return the minimum absolute distance from `start` to an index containing `target`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5], target = 5, start = 3`
- Output: `1`

**Example 2**

- Input: `nums = [1], target = 1, start = 0`
- Output: `0`

**Example 3**

- Input: `nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
Scan all indices and compute `abs(i - start)` for every occurrence of `target`, keeping the smallest distance. A two-direction expansion from `start` also works because the first found target is nearest.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
