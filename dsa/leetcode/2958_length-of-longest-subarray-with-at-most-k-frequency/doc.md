# Length of Longest Subarray With at Most K Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2958 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) |

## Problem Description
### Goal
You are given an integer array `nums` and an integer `k`. The frequency of a
value within an array is the number of positions at which that value occurs.
Call an array good when every value in it has frequency at most `k`.

Find the greatest length among all good subarrays of `nums`. A subarray must be
a contiguous, non-empty sequence of the original array; elements cannot be
skipped or reordered.

### Function Contract
**Inputs**

- `nums`: the integer array whose contiguous ranges are considered
- `k`: the maximum permitted frequency of every value in a good subarray

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$, $1\le\texttt{nums[i]}\le10^9$, and $1\le k\le N$.

**Return value**

The length of the longest contiguous subarray in which no value occurs more
than `k` times.

### Examples
**Example 1**

- Input: `nums = [1,2,3,1,2,3,1,2], k = 2`
- Output: `6`
- Explanation: `[1,2,3,1,2,3]` is good, and no longer subarray keeps every frequency at most two.

**Example 2**

- Input: `nums = [1,2,1,2,1,2,1,2], k = 1`
- Output: `2`
- Explanation: Any adjacent `1,2` pair is good, while every longer range repeats at least one value.

**Example 3**

- Input: `nums = [5,5,5,5,5,5,5], k = 4`
- Output: `4`
- Explanation: Four consecutive copies meet the limit, but any fifth copy exceeds it.
