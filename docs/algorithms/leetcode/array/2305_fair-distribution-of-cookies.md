# Fair Distribution of Cookies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2305 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [fair-distribution-of-cookies](https://leetcode.com/problems/fair-distribution-of-cookies/) |

## Problem Description & Examples
### Goal
Assign every indivisible cookie bag to one of `k` children. Minimize unfairness, defined as the largest total number of cookies received by any child.

### Function Contract
**Inputs**

- `cookies`: cookie counts in the bags.
- `k`: the number of children.

**Return value**

The minimum possible unfairness.

### Examples
**Example 1**

- Input: `cookies = [8, 15, 10, 20, 8]`, `k = 2`
- Output: `31`

**Example 2**

- Input: `cookies = [6, 1, 3, 2, 2, 4, 1, 2]`, `k = 3`
- Output: `7`

**Example 3**

- Input: `cookies = [1, 2]`, `k = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
Backtrack over bags, assigning each to a child and tracking current loads. Prune any branch whose current maximum already reaches the best known result. Skip children with duplicate current loads to avoid symmetric assignments, and after trying one empty child do not try other empty children.

---

## Complexity Analysis
- **Time Complexity**: `O(k^n)` in the worst case
- **Space Complexity**: `O(k + n)`
