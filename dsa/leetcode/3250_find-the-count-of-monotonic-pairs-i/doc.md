# Find the Count of Monotonic Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3250 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/) |

## Problem Description

### Goal

Given an array `nums` of $n$ positive integers, count pairs of non-negative integer arrays `(arr1, arr2)`, both of length $n$, that meet all three conditions:

- `arr1` is monotonically non-decreasing.
- `arr2` is monotonically non-increasing.
- At every index `i`, `arr1[i] + arr2[i] == nums[i]`.

Different choices of either array form different pairs. Count every admissible decomposition and return the total modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 2000$ and $1 \le \texttt{nums[i]} \le 50$.

Let $m=\max(\texttt{nums})$.

**Return value**

- The number of valid monotonic array pairs, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [2,3,2]`
- Output: `4`

The valid first arrays are `[0,1,1]`, `[0,1,2]`, `[0,2,2]`, and `[1,2,2]`; subtracting each from `nums` produces its corresponding non-increasing second array.

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `126`

**Example 3**

- Input: `nums = [1]`
- Output: `2`

The two decompositions are `([0],[1])` and `([1],[0])`.
