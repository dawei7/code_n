# Best Sightseeing Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1014 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [best-sightseeing-pair](https://leetcode.com/problems/best-sightseeing-pair/) |

## Problem Description & Examples
### Goal
Choose two sightseeing spots `i < j` to maximize `values[i] + values[j] + i - j`.

### Function Contract
**Inputs**

- `values`: List[int]

**Return value**

int - maximum pair score

### Examples
**Example 1**

- Input: `values = [8, 1, 5, 2, 6]`
- Output: `11`

**Example 2**

- Input: `values = [1, 2]`
- Output: `2`

**Example 3**

- Input: `values = [4, 7, 5, 8]`
- Output: `13`

---

## Underlying Base Algorithm(s)
One-pass dynamic tracking of the best left contribution.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
