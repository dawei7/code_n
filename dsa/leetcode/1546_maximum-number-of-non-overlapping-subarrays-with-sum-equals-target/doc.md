# Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1546 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, select as many contiguous subarrays as possible such that every selected subarray has sum exactly equal to `target`. Selected subarrays must be pairwise non-overlapping: no array position may belong to more than one of them.

Return the maximum possible number of selected subarrays. Values may be positive, negative, or zero, so a sliding window based on monotonic growth is not generally valid, and locally overlapping target-sum candidates may require choosing the one that leaves the most room for later selections.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `target`: the required sum of every selected subarray, where $-10^6 \le \texttt{target} \le 10^6$.

**Return value**

The largest number of pairwise non-overlapping contiguous subarrays whose sums equal `target`.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 2`
- Output: `2`
- Explanation: Two disjoint length-two subarrays can be selected; one element remains unused.

**Example 2**

- Input: `nums = [-1, 3, 5, 1, 4, 2, -9], target = 6`
- Output: `2`
- Explanation: Negative values allow several candidate boundaries, but at most two target-sum intervals can be disjoint.

**Example 3**

- Input: `nums = [3, 4, 7, 2, -3, 1, 4, 2], target = 7`
- Output: `3`
- Explanation: The subarrays `[3, 4]`, `[7]`, and `[1, 4, 2]` are pairwise non-overlapping and each sums to seven.
