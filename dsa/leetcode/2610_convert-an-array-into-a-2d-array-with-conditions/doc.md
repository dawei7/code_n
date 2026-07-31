# Convert an Array Into a 2D Array With Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2610 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/) |

## Problem Description

### Goal

Given an integer array `nums`, rearrange all of its elements into a two-dimensional array. Every occurrence from `nums` must appear exactly once in the result, and no result row may contain the same integer more than once.

Use as few rows as possible. Rows do not need to have equal lengths, and when several minimum-row arrangements satisfy the conditions, any one of them may be returned.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 200$ and $1 \leq \texttt{nums[i]} \leq n$.

**Return value**

Return any two-dimensional array that contains exactly the multiset of values from `nums`, has distinct integers within every row, and uses the minimum possible number of rows.

### Examples

**Example 1**

- Input: `nums = [1, 3, 4, 1, 2, 3, 1]`
- Output: `[[1, 3, 4, 2], [1, 3], [1]]`
- Explanation: Three copies of `1` force at least three rows, and the displayed arrangement achieves that bound while keeping every row distinct.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `[[4, 3, 2, 1]]`
- Explanation: Because all values are distinct, a single row is valid and therefore minimal.
