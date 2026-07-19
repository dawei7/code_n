# Next Greater Numerically Balanced Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2048 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Backtracking, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-numerically-balanced-number/) |

## Problem Description

### Goal

An integer is *numerically balanced* when each digit that appears in its decimal representation occurs exactly as many times as the digit's value. For example, `22` is balanced because digit `2` occurs twice, while `1022` is not: the presence of digit `0` would require it to occur zero times, which is impossible once it appears.

Given an integer `n`, find the smallest numerically balanced integer that is strictly greater than `n`. The answer must therefore satisfy both the digit-frequency rule and the minimality requirement; returning `n` itself is never allowed, even when `n` is already balanced.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^6$.

**Return value**

- Return the smallest integer greater than `n` for which every occurring digit $d$ appears exactly $d$ times.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `22`
- Explanation: Digit `2` occurs exactly twice, and no smaller balanced integer is greater than `1`.

**Example 2**

- Input: `n = 1000`
- Output: `1333`
- Explanation: Digit `1` occurs once and digit `3` occurs three times. A value such as `1022` is invalid because an occurring zero can never have zero occurrences.

**Example 3**

- Input: `n = 3000`
- Output: `3133`
- Explanation: `3133` has one `1` and three `3` digits and is the first balanced value after `3000`.
