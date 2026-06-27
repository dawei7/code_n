# Minimum Cost to Reach Every Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3502 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [minimum-cost-to-reach-every-position](https://leetcode.com/problems/minimum-cost-to-reach-every-position/) |

## Problem Description & Examples
### Goal
Given an array of costs where `costs[i]` represents the price to visit position `i`, determine the minimum total cost required to visit every position in the array. Since you can start at any position and move to adjacent positions, the goal is to calculate the cumulative cost of visiting all indices exactly once, effectively summing all elements in the array.

### Function Contract
**Inputs**

- `costs`: A list of integers where `costs[i]` is the non-negative cost to visit position `i`.

**Return value**

- An integer representing the total sum of all costs in the input array.

### Examples
**Example 1**

- Input: `costs = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `costs = [5, 10, 15, 20]`
- Output: `50`

**Example 3**

- Input: `costs = [0, 0, 0]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem reduces to a simple summation of all elements in a linear array. Since every position must be visited exactly once, the order of traversal does not affect the total cost, making the summation operation the optimal approach.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the `costs` array, as we must iterate through each element exactly once.
- **Space Complexity**: `O(1)`, as we only require a single variable to store the running total.
