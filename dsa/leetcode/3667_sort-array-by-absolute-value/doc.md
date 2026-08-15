# Sort Array By Absolute Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3667 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-absolute-value/) |

## Problem Description

### Goal

Given an integer array `nums`, rearrange all of its elements so their absolute values appear in non-decreasing order.

The result must contain exactly the same multiset of signed integers as the input. When two values have equal absolute value, either relative order is valid; for example, `-1` may appear before or after `1`.

Return any rearranged array satisfying this absolute-value ordering. The numerical values themselves are not replaced by their magnitudes.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, where $1\le n\le100$ and $-100\le\texttt{nums[i]}\le100$.

**Return value**

Return a permutation of `nums` such that $\lvert\texttt{answer[i]}\rvert\le\lvert\texttt{answer[i+1]}\rvert$ at every adjacent pair. Equal-magnitude ties may use any order.

### Examples

#### Example 1

- **Input:** `nums = [3, -1, -4, 1, 5]`
- One valid output: `[-1, 1, 3, -4, 5]`
- The resulting magnitudes are `[1, 1, 3, 4, 5]`.

#### Example 2

- **Input:** `nums = [-100, 100]`
- One valid output: `[-100, 100]`
- Reversing these two values would also be valid because both magnitudes are `100`.

#### Example 3

- **Input:** `nums = [0, -2, 2, -1]`
- One valid output: `[0, -1, -2, 2]`.
