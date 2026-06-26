# Minimum Adjacent Swaps for K Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1703 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Official Link | [minimum-adjacent-swaps-for-k-consecutive-ones](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) |

## Problem Description & Examples
### Goal
Given a binary array, use adjacent swaps to make some `k` ones appear consecutively. Find the minimum number of swaps.

### Function Contract
**Inputs**

- `nums`: a binary array.
- `k`: the number of ones to group.

**Return value**

Return the minimum adjacent swaps required.

### Examples
**Example 1**

- Input: `nums = [1,0,0,1,0,1], k = 2`
- Output: `1`

**Example 2**

- Input: `nums = [1,0,0,0,0,0,1,1], k = 3`
- Output: `5`

**Example 3**

- Input: `nums = [1,1,0,1], k = 2`
- Output: `0`

---

## Underlying Base Algorithm(s)
Record the indices of all ones, then remove their natural spacing by using adjusted positions `pos[i] - i`. For any window of `k` ones, the best final block is centered at the median adjusted position. Prefix sums over adjusted positions compute the movement cost for each window in constant time.

---

## Complexity Analysis
- **Time Complexity**: `O(m)`, where `m` is the number of ones
- **Space Complexity**: `O(m)`
