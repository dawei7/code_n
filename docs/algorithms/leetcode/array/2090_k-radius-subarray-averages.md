# K Radius Subarray Averages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2090 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [k-radius-subarray-averages](https://leetcode.com/problems/k-radius-subarray-averages/) |

## Problem Description & Examples
### Goal
For each index, compute the average of the subarray centered there with radius `k`. If the full window would fall outside the array, use `-1`.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `k`: radius on each side.

**Return value**

Return an array of centered integer averages using floor division.

### Examples
**Example 1**

- Input: `nums = [7,4,3,9,1,8,5,2,6], k = 3`
- Output: `[-1,-1,-1,5,4,4,-1,-1,-1]`

**Example 2**

- Input: `nums = [100000], k = 0`
- Output: `[100000]`

**Example 3**

- Input: `nums = [8], k = 100000`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
The window length is `2k + 1`. Use a sliding window sum or prefix sums to compute each full window average in constant time, writing `-1` for indices without a complete window.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` beyond the result.
