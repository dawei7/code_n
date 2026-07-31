# Adjacent Increasing Subarrays Detection II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3350 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/) |

## Problem Description

### Goal

Given an integer array `nums`, choose two non-empty contiguous subarrays having the same length `k`. Both chosen subarrays must be strictly increasing: within each one, every element after the first must be greater than its immediate predecessor.

The two subarrays must be adjacent and non-overlapping. If the first starts at index `a`, the second must start at `a + k`; no comparison is required between the final element of the first block and the initial element of the second. Among every valid adjacent pair, return the maximum possible value of `k`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers.

The source guarantees $2 \le n \le 2 \cdot 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the largest positive integer `k` for which two adjacent strictly increasing subarrays of length `k` exist.

### Examples

**Example 1**

- Input: `nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]`
- Output: `3`
- Explanation: `[7, 8, 9]` and `[2, 3, 4]` begin at indices 2 and 5. Both are strictly increasing and adjacent, and no valid pair has length greater than three.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]`
- Output: `2`
- Explanation: `[1, 2]` and `[3, 4]` are adjacent strictly increasing blocks. No adjacent pair of length three or more satisfies both conditions.

**Boundary example**

- Input: `nums = [1, 2, 2, 3]`
- Output: `2`
- Explanation: `[1, 2]` and `[2, 3]` are independently strictly increasing. Equality across their shared boundary is allowed.
