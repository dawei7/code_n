# Check If N and Its Double Exist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1346 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |

## Problem Description

### Goal

Given an integer array `arr`, determine whether it contains two elements at different indices such that one element is exactly twice the other. More precisely, decide whether there are indices `i` and `j` with $i \ne j$ and `arr[i] == 2 * arr[j]`.

Return `true` when such a pair exists and `false` otherwise. The distinct-index requirement matters for zero and duplicate values: one occurrence cannot be paired with itself.

### Function Contract

**Inputs**

- `arr`: an integer array. Let $n$ be its length.

**Return value**

- Return `true` if two different indices hold values related by an exact factor of two; otherwise return `false`.

### Examples

**Example 1**

- Input: `arr = [10, 2, 5, 3]`
- Output: `true`
- Explanation: The values `10` and `5` occur at different indices and `10 == 2 * 5`.

**Example 2**

- Input: `arr = [3, 1, 7, 11]`
- Output: `false`

**Example 3**

- Input: `arr = [0, 0]`
- Output: `true`
