# Combination Sum III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 216 |
| Difficulty | Medium |
| Topics | Array, Backtracking |
| Official Link | [combination-sum-iii](https://leetcode.com/problems/combination-sum-iii/) |

## Problem Description & Examples
### Goal
Find every combination of exactly `k` distinct numbers from `1` through `9` whose sum is `n`. Each combination is returned once.

### Function Contract
**Inputs**

- `k`: the required number of selected values.
- `n`: the required sum.

**Return value**

A list of all valid combinations, in any order.

### Examples
**Example 1**

- Input: `k = 3`, `n = 7`
- Output: `[[1, 2, 4]]`

**Example 2**

- Input: `k = 3`, `n = 9`
- Output: `[[1, 2, 6], [1, 3, 5], [2, 3, 4]]`

**Example 3**

- Input: `k = 4`, `n = 1`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Backtrack with the next allowed number, remaining slots, and remaining sum. Choose candidates in increasing order so values cannot repeat and combinations are not permuted. Stop when exactly `k` values sum to the target, and prune when the remaining sum cannot fit within the smallest or largest possible choices.

---

## Complexity Analysis
- **Time Complexity**: `O(C(9, k) * k)` including emitted combinations
- **Space Complexity**: `O(k)` auxiliary recursion space, excluding the output
