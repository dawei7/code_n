# Lexicographically Smallest String After a Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3216 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/) |

## Problem Description

### Goal

You are given a string `s` containing only decimal digits. You may perform at most one operation: choose two adjacent digits that have the same parity and swap them. Two digits have the same parity when they are both even or both odd.

Return the lexicographically smallest string obtainable under this rule. Making no swap is allowed, so an operation that would make the string larger is never required. Lexicographic comparison is decided by the first position at which two candidate strings differ.

### Function Contract

**Inputs**

- `s`: A string of decimal digits, with $2 \leq \lvert\texttt{s}\rvert \leq 100$.

**Return value**

Return the lexicographically smallest string obtainable by making zero or one legal adjacent swap.

### Examples

**Example 1**

- Input: `s = "45320"`
- Output: `"43520"`
- Explanation: The adjacent digits `5` and `3` are both odd. Swapping them produces the smallest legal result.

**Example 2**

- Input: `s = "001"`
- Output: `"001"`
- Explanation: The only same-parity adjacent pair contains equal digits, so no swap can improve the string.

**Example 3**

- Input: `s = "42"`
- Output: `"24"`
- Explanation: Both digits are even, and moving `2` to the first position makes the string smaller.
