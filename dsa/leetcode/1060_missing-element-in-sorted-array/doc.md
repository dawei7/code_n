# Missing Element in Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1060 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/missing-element-in-sorted-array/) |

## Problem Description

### Goal

Given an integer array `nums` whose unique elements are sorted in **ascending order**, and a positive integer `k`, consider the integers absent while counting upward from the array's leftmost value.

Return the `k`th missing number in that sequence. The count starts strictly after `nums[0]`, so values smaller than the leftmost array element are irrelevant. Gaps between consecutive array elements contribute their absent integers in ascending order, and if those internal gaps contain fewer than `k` missing numbers, the sequence continues beyond the last array element along the integer line.

### Function Contract

**Inputs**

- `nums`: an array of $N$ unique integers in ascending order, where $1 \le N \le 5 \cdot 10^4$ and $1 \le \texttt{nums[i]} \le 10^7$.
- `k`: a missing-number index satisfying $1 \le k \le 10^8$.

**Return value**

- The `k`th integer missing after `nums[0]`.

### Examples

**Example 1**

- Input: `nums = [4, 7, 9, 10], k = 1`
- Output: `5`
- Explanation: The first missing number after 4 is 5.

**Example 2**

- Input: `nums = [4, 7, 9, 10], k = 3`
- Output: `8`
- Explanation: The missing sequence begins `[5, 6, 8, ...]`.

**Example 3**

- Input: `nums = [1, 2, 4], k = 3`
- Output: `6`
- Explanation: The missing sequence begins `[3, 5, 6, 7, ...]`.
