# Largest Multiple of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1363 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/largest-multiple-of-three/) |

## Problem Description

### Goal

Given an array of decimal digits, select any nonempty subset of their occurrences and arrange the selected digits in any order. Each input occurrence may be used at most once.

Return the numerically largest arrangement that is divisible by $3$, represented as a string. The representation must not contain leading zeroes unless its value is exactly zero; if no nonempty selection can form a multiple of three, return the empty string. When the selected digits are all zero, return `"0"` rather than several zeroes.

### Function Contract

**Inputs**

- `digits`: an array of $n$ integers, each from $0$ through $9$.

**Return value**

- The largest decimal string obtainable from some input occurrences whose integer value is divisible by $3$, or `""` when no such nonempty selection exists.

### Examples

**Example 1**

- Input: `digits = [8,1,9]`
- Output: `"981"`

**Example 2**

- Input: `digits = [8,6,7,1,0]`
- Output: `"8760"`

**Example 3**

- Input: `digits = [1]`
- Output: `""`
