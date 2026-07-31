# Minimum Operations to Make a Special Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2844 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/) |

## Problem Description

### Goal

You are given a 0-indexed string `num` representing a non-negative integer. In one operation, you may delete any one digit while preserving the relative order of all digits that remain. If every digit is deleted, the resulting value is defined to be `0`.

An integer is special when it is divisible by $25$. Return the minimum number of digit deletions needed to make the represented number special.

### Function Contract

**Inputs**

- `num`: A decimal string without leading zeros.

The constraints are $1\le\lvert\texttt{num}\rvert\le100$, and every character is a digit from `0` through `9`. Let $n=\lvert\texttt{num}\rvert$.

**Return value**

- The minimum number of digits that must be deleted so the remaining value is divisible by $25$.

### Examples

**Example 1**

- Input: `num = "2245047"`
- Output: `2`
- Explanation: Deleting the final two digits leaves `22450`, which is divisible by $25$.

**Example 2**

- Input: `num = "2908305"`
- Output: `3`
- Explanation: Deleting the digits at original indices `3`, `4`, and `6` leaves `2900`.

**Example 3**

- Input: `num = "10"`
- Output: `1`
- Explanation: Deleting the leading `1` leaves `0`, a multiple of $25$.
