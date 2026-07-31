# Minimum Stability Factor of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3605 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Segment Tree, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-stability-factor-of-array/) |

## Problem Description
### Goal

You are given an integer array `nums` and an integer `maxC`. A subarray is **stable** when the highest common factor (HCF), equivalently the greatest common divisor, of all its elements is at least $2$. The array's **stability factor** is the length of its longest stable subarray.

You may change at most `maxC` array elements, and each chosen element may be replaced by any integer. Minimize the stability factor after those changes.

Length-one subarrays follow the same rule: `[x]` is stable exactly when $x \ge 2$, because its HCF is $x$. Return $0$ when the final array has no stable subarray at all.

### Function Contract

**Inputs**

- `nums`: An array of $n$ positive integers.
- `maxC`: The maximum number of elements that may be changed.

The constraints are $1 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le 10^9$, and $0 \le \texttt{maxC} \le n$.

**Return value**

Return the minimum possible length of the longest stable subarray after at most `maxC` modifications.

### Examples

**Example 1**

- Input: `nums = [3, 5, 10], maxC = 1`
- Output: `1`
- Explanation: `[5, 10]` initially has HCF $5$. Changing the middle element can eliminate every stable subarray longer than one.

**Example 2**

- Input: `nums = [2, 6, 8], maxC = 2`
- Output: `1`
- Explanation: Two changes can break the common factor shared by every multi-element stable subarray, but the unchanged value `2` still forms a stable length-one subarray.

**Example 3**

- Input: `nums = [2, 4, 9, 6], maxC = 1`
- Output: `2`
- Explanation: `[2, 4]` and `[9, 6]` are disjoint stable pairs, so one change cannot destroy both.
