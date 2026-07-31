# Make the Prefix Sum Non-negative

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2599 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-the-prefix-sum-non-negative/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums`. In one operation, choose any element, remove it from its current position, and place it at the end of the array. You may repeat this operation as needed.

For the resulting order, the prefix sum at index `i` is the sum of all elements from index zero through `i`, inclusive. Every one of these prefix sums must be non-negative.

Return the minimum number of move-to-the-end operations required. The input is guaranteed to admit a valid ordering.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \leq n \leq 10^5$ and $-10^9 \leq \texttt{nums[i]} \leq 10^9$.

The total sum is guaranteed to make a valid result possible.

**Return value**

- The minimum number of elements that must be moved to the end so that no prefix sum is negative.

### Examples

**Example 1**

- Input: `nums = [2,3,-5,4]`
- Output: `0`

The original prefix sums are `2`, `5`, `0`, and `4`, so no operation is needed.

**Example 2**

- Input: `nums = [3,-5,-2,6]`
- Output: `1`

Moving `-5` to the end produces `[3,-2,6,-5]`, whose prefix sums are `3`, `1`, `7`, and `2`.
