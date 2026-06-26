# Maximum Score of a Good Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1793 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Binary Search, Stack, Monotonic Stack |
| Official Link | [maximum-score-of-a-good-subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) |

## Problem Description & Examples
### Goal
Find a subarray that must include index `k`. Its score is the minimum value in the subarray multiplied by the subarray length. Maximize this score.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.
- `k`: an index that must be included in the chosen subarray.

**Return value**

Return the maximum score of any valid subarray.

### Examples
**Example 1**

- Input: `nums = [1,4,3,7,4,5], k = 3`
- Output: `15`

**Example 2**

- Input: `nums = [5,5,4,5,4,1,1,1], k = 0`
- Output: `20`

**Example 3**

- Input: `nums = [2,3,3,1], k = 1`
- Output: `6`

---

## Underlying Base Algorithm(s)
Expand a window from index `k`. Track the current minimum. At each step, extend toward the side with the larger neighboring value, because that choice preserves a higher possible minimum for longer. Update `current_min * window_length` after every expansion. A monotonic-stack formulation with previous/next smaller elements is also possible.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
