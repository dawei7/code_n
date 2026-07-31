# Maximum Strength of a Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2708 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Greedy, Bit Manipulation, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-strength-of-a-group/) |

## Problem Description

### Goal

The integer array `nums` contains exam scores, one for each student. Form a non-empty group by choosing any subset of student indices. The group's strength is the product of the scores at all chosen indices.

Return the largest strength obtainable from any non-empty group. Each array occurrence may be chosen at most once, while its position relative to other chosen students does not affect the product. Negative values can improve the result when combined appropriately, zero may be preferable to every available negative product, and the non-empty rule prevents using the multiplicative identity from an empty selection.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 13$ and $-9 \le \texttt{nums[i]} \le 9$.

**Return value**

Return the maximum product among all non-empty subsets of indices in `nums`.

### Examples

**Example 1**

- Input: `nums = [3,-1,-5,2,5,-9]`
- Output: `1350`
- Explanation: Choosing values $3,-5,2,5,-9$ gives $1350$.

**Example 2**

- Input: `nums = [-4,-5,-4]`
- Output: `20`
- Explanation: The pair $-5$ and $-4$ has the greatest product.

**Example 3**

- Input: `nums = [-5,0]`
- Output: `0`
- Explanation: The one-element group containing zero is stronger than the group containing only $-5$.
