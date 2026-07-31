# Minimum Cost to Make All Characters Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2712 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/) |

## Problem Description

### Goal

A 0-indexed binary string `s` of length $n$ may be changed with either of two operations. Choose an index $i$ and invert every character from index $0$ through $i$, inclusive, at cost $i+1$. Alternatively, invert every character from index $i$ through $n-1$, inclusive, at cost $n-i$.

Inverting changes every `'0'` in the selected range to `'1'` and every `'1'` to `'0'`. Operations may be applied as often as needed and may overlap. Determine the minimum total cost that makes every character in the final string equal; the common final character may be either zero or one.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$, where $1 \le n \le 10^5$.

**Return value**

Return the minimum total cost of prefix and suffix inversions needed to make all characters equal.

### Examples

**Example 1**

- Input: `s = "0011"`
- Output: `2`
- Explanation: Inverting the suffix beginning at index $2$ changes the string to `"0000"` and costs $4-2=2$.

**Example 2**

- Input: `s = "010101"`
- Output: `9`
- Explanation: Resolving the five alternating boundaries with the cheaper side of each boundary costs $1+2+3+2+1=9$.
