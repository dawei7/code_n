# Assign Cookies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 455 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/assign-cookies/) |

## Problem Description
### Goal
Each child has a greed requirement `g[i]`, and each available cookie has a size `s[j]`. A child is satisfied only when assigned one cookie whose size is at least that child's requirement.

Assign each cookie to at most one child and each child at most one cookie. Return the maximum number of satisfied children. Unused cookies and unsatisfied children are allowed, and a larger cookie may satisfy a less greedy child but then cannot be reused. The function returns only the optimal count rather than a concrete assignment. An empty cookie list yields zero satisfied children.

### Function Contract
**Inputs**

- `g`: greed requirements for the children
- `s`: sizes of the available cookies

**Return value**

- The maximum number of children that can be satisfied by a one-to-one assignment

### Examples
**Example 1**

- Input: `g = [1, 2, 3], s = [1, 1]`
- Output: `1`

**Example 2**

- Input: `g = [1, 2], s = [1, 2, 3]`
- Output: `2`

**Example 3**

- Input: `g = [10, 9, 8, 7], s = [5, 6, 7, 8]`
- Output: `2`
