# Maximum Beauty of an Array After Applying Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2779 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a non-negative integer `k`. In one operation, choose an index that has not been chosen before and replace its value with any integer in the inclusive interval from `nums[i] - k` through `nums[i] + k`.

You may apply the operation any number of times, including zero times, but each index can be selected at most once. The beauty of the resulting array is the length of its longest subsequence whose elements are all equal. A subsequence may delete elements without changing the relative order of those retained.

Return the greatest beauty that can be achieved by choosing the operations and replacement values optimally.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.
- `k`: The maximum distance an operated value may move in either direction, where $0 \le k \le 10^5$.

**Return value**

Return the maximum number of elements that can be made equal after applying valid operations. Elements outside the chosen subsequence need not be changed.

### Examples

**Example 1**

- Input: `nums = [4,6,1,2]`, `k = 2`
- Output: `3`
- Explanation: Keep the first `4`, change `6` to `4`, and change `2` to `4`. Those three equal values form a subsequence, and no four-element common target exists.

**Example 2**

- Input: `nums = [1,1,1,1]`, `k = 10`
- Output: `4`
- Explanation: The entire array is already equal, so using no operations achieves the maximum possible beauty.

**Example 3**

- Input: `nums = [5,1,5,2,5]`, `k = 0`
- Output: `3`
- Explanation: No value can move when `k` is zero, so the three existing copies of `5` form the longest equal subsequence.
