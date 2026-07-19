# Number of Squareful Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 996 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-squareful-arrays/) |

## Problem Description

### Goal

An array is squareful when the sum of every pair of adjacent elements is a perfect square. Given an integer array `nums`, count how many distinct permutations of all its elements are squareful.

Two permutations are different only when their values differ at some index. Consequently, exchanging two equal input occurrences does not create another permutation, while placing different values in a different order may do so. Return the number of value sequences that satisfy the adjacency condition throughout.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le12$ and $0\le\texttt{nums[i]}\le10^9$.

Let $U$ be the number of distinct values in `nums`.

**Return value**

- The number of distinct permutations in which every adjacent pair has a perfect-square sum.

### Examples

**Example 1**

- Input: `nums = [1, 17, 8]`
- Output: `2`
- Explanation: `[1, 8, 17]` and `[17, 8, 1]` are the valid permutations.

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `1`
- Explanation: The only distinct permutation is squareful because every adjacent sum is $4$.

**Example 3**

- Input: `nums = [1, 1, 8]`
- Output: `1`
- Explanation: Only `[1, 8, 1]` avoids the nonsquare adjacent sum $1+1$.
