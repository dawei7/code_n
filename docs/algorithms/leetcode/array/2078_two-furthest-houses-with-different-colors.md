# Two Furthest Houses With Different Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2078 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [two-furthest-houses-with-different-colors](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) |

## Problem Description & Examples
### Goal
Find the greatest distance between two house indices whose colors are different.

### Function Contract
**Inputs**

- `colors`: color id for each house in order.

**Return value**

Return the maximum absolute index difference between differently colored houses.

### Examples
**Example 1**

- Input: `colors = [1,1,1,6,1,1,1]`
- Output: `3`

**Example 2**

- Input: `colors = [1,8,3,8,3]`
- Output: `4`

**Example 3**

- Input: `colors = [0,1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The farthest pair must involve one end if possible. Check from the right for the first color different from `colors[0]`, and from the left for the first color different from `colors[n - 1]`; take the larger distance.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
