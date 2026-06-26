# Count Number of Teams

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1395 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Segment Tree |
| Official Link | [count-number-of-teams](https://leetcode.com/problems/count-number-of-teams/) |

## Problem Description & Examples
### Goal
Count teams of three soldiers chosen in increasing index order where ratings are either strictly increasing or strictly decreasing.

### Function Contract
**Inputs**

- `rating`: a list of distinct soldier ratings.

**Return value**

The number of valid three-person teams.

### Examples
**Example 1**

- Input: `rating = [2,5,3,4,1]`
- Output: `3`

**Example 2**

- Input: `rating = [2,1,3]`
- Output: `0`

**Example 3**

- Input: `rating = [1,2,3,4]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Middle-index counting. Treat each soldier as the middle member, count smaller/larger ratings on the left and right, then add increasing and decreasing combinations.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` with direct counting around each middle index.
- **Space Complexity**: `O(1)` extra.
