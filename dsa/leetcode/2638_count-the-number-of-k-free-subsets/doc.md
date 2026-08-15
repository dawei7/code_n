# Count the Number of K-Free Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2638 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Sorting, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-k-free-subsets/) |

## Problem Description

### Goal

You are given an array `nums` containing distinct positive integers and a positive integer `k`. A subset is **k-Free** when it does not contain two different values whose absolute difference is exactly `k`.

Count every k-Free subset of `nums` and return that total. Subsets are determined by the selected elements, their order is irrelevant, and the empty subset is included in the answer.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct integers, where $1 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 1000$.
- `k`: A positive integer with $1 \le k \le 1000$.

**Return value**

Return the number of subsets of `nums` in which no pair of selected values has absolute difference exactly `k`. Include the empty subset.

### Examples

#### Example 1

- **Input:** `nums = [5,4,6]`, `k = 1`
- **Output:** `5`
- **Explanation:** The valid subsets are `[]`, `[4]`, `[5]`, `[6]`, and `[4,6]`.

#### Example 2

- **Input:** `nums = [2,3,5,8]`, `k = 5`
- **Output:** `12`
- **Explanation:** The only conflicting pair is `3` and `8`. Of the sixteen total subsets, four contain both values, leaving twelve valid subsets.

#### Example 3

- **Input:** `nums = [10,5,9,11]`, `k = 20`
- **Output:** `16`
- **Explanation:** No two values differ by twenty, so all $2^4$ subsets are k-Free.
