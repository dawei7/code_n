# Jump Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1696 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Official Link | [jump-game-vi](https://leetcode.com/problems/jump-game-vi/) |

## Problem Description & Examples
### Goal
Starting at index `0`, jump forward at most `k` positions at a time until reaching the last index. The score is the sum of visited values. Maximize the score.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the maximum jump length.

**Return value**

Return the largest score obtainable at the final index.

### Examples
**Example 1**

- Input: `nums = [1,-1,-2,4,-7,3], k = 2`
- Output: `7`

**Example 2**

- Input: `nums = [10,-5,-2,4,0,3], k = 3`
- Output: `17`

**Example 3**

- Input: `nums = [1,-5,-20,4,-1,3,-6,-3], k = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
Let `dp[i]` be the best score when landing on index `i`. It equals `nums[i]` plus the maximum `dp[j]` among the previous `k` indices. Maintain those candidate scores in a decreasing deque, dropping expired indices and dominated scores as the scan advances.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
