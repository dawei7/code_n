# Minimum Cost to Merge Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1000 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-cost-to-merge-stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) |

## Problem Description & Examples
### Goal
Given stone piles in a row, each operation may merge exactly `k` consecutive piles into one pile whose weight is their sum. Return the minimum total merge cost needed to end with one pile, or `-1` if the merge count can never reach one pile.

### Function Contract
**Inputs**

- `stones`: List[int] pile weights
- `k`: int number of adjacent piles merged per operation

**Return value**

int - minimum total cost, or `-1` if impossible

### Examples
**Example 1**

- Input: `stones = [3, 2, 4, 1], k = 2`
- Output: `20`

**Example 2**

- Input: `stones = [3, 2, 4, 1], k = 3`
- Output: `-1`

**Example 3**

- Input: `stones = [3, 5, 1, 2, 6], k = 3`
- Output: `25`

---

## Underlying Base Algorithm(s)
Interval dynamic programming with prefix sums.

---

## Complexity Analysis
- **Time Complexity**: `O(n^3 / k)` in the direct interval DP form
- **Space Complexity**: `O(n^2)`
