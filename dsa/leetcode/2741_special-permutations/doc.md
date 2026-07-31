# Special Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2741 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/special-permutations/) |

## Problem Description

### Goal

An array `nums` contains $n$ distinct positive integers. A permutation of all its values is special when every adjacent pair is compatible by divisibility: for each neighboring pair, either the left value is divisible by the right value or the right value is divisible by the left value.

Count all distinct special permutations of `nums`. Every input value must appear exactly once in each counted ordering. Because the number of valid orderings can be large, return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct positive integers, where $2 \le n \le 14$ and $1 \le \texttt{nums}[i] \le 10^9$.

**Return value**

Return the number of permutations in which every adjacent pair satisfies at least one of the two divisibility directions, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [2,3,6]`
- Output: `2`
- Explanation: `[3,6,2]` and `[2,6,3]` are the two compatible orderings.

**Example 2**

- Input: `nums = [1,4,3]`
- Output: `2`
- Explanation: The valid permutations are `[3,1,4]` and `[4,1,3]` because `1` connects the otherwise incompatible values.

**Example 3**

- Input: `nums = [2,4,8]`
- Output: `6`
- Explanation: Every pair is compatible, so all $3!$ permutations are special.
