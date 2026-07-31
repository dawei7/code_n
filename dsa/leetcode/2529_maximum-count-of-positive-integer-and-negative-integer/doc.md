# Maximum Count of Positive Integer and Negative Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2529 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) |

## Problem Description

### Goal

You are given an integer array `nums` sorted in non-decreasing order. Count how many elements are strictly positive and how many are strictly negative, then return the larger of those two counts.

Zero is neither positive nor negative, so any zero-valued block contributes to neither count. If `pos` is the positive count and `neg` is the negative count, the requested result is $\max(\texttt{pos},\texttt{neg})$.

### Function Contract

**Inputs**

- `nums`: A nonempty integer array sorted in non-decreasing order.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 2000$ and $-2000 \le \texttt{nums[i]} \le 2000$.

**Return value**

Return the maximum of the number of strictly positive elements and the number of strictly negative elements.

### Examples

**Example 1**

- Input: `nums = [-2, -1, -1, 1, 2, 3]`
- Output: `3`
- Explanation: There are three negative and three positive values.

**Example 2**

- Input: `nums = [-3, -2, -1, 0, 0, 1, 2]`
- Output: `3`
- Explanation: The three negatives outnumber the two positives; the zeros belong to neither group.

**Example 3**

- Input: `nums = [5, 20, 66, 1314]`
- Output: `4`
