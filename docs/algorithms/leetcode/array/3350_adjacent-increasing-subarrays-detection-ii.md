# Adjacent Increasing Subarrays Detection II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3350 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [adjacent-increasing-subarrays-detection-ii](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/) |

## Problem Description & Examples
### Goal
Determine the maximum integer `k` such that there exist two contiguous, non-overlapping subarrays of length `k` within the input array, where both subarrays are strictly increasing and positioned immediately adjacent to each other.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to analyze.

**Return value**

- An integer representing the largest possible value of `k` that satisfies the condition.

### Examples
**Example 1**

- Input: `nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]`
- Output: `3`
- Explanation: The subarrays `[2, 5, 7]` and `[8, 9, 2]` are not the answer, but `[5, 7, 8]` and `[9, 2, 3]` are not adjacent. The correct subarrays are `[2, 5, 7]` and `[8, 9, 2]` (length 3).

**Example 2**

- Input: `nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]`
- Output: `2`
- Explanation: The longest adjacent increasing subarrays are `[3, 4]` and `[4, 4]` (invalid) or `[5, 6]` and `[7]` (invalid). The max `k` is 2.

**Example 3**

- Input: `nums = [1, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem can be solved by pre-calculating the length of the strictly increasing subarray ending at each index. Once these lengths are computed, we can use binary search on the answer `k` or a linear scan to check if there exists an index `i` such that the increasing subarray ending at `i` has length at least `k`, and the increasing subarray starting at `i+1` also has length at least `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass to compute lengths and another pass to check for the condition.
- **Space Complexity**: `O(n)` to store the lengths of increasing subarrays ending at each index.
