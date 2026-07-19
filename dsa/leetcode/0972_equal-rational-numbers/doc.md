# Equal Rational Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 972 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [equal-rational-numbers](https://leetcode.com/problems/equal-rational-numbers/) |

## Problem Description

### Goal

Two strings `s` and `t` each represent a non-negative rational number. A representation has an integer part, may have a decimal point followed by a finite non-repeating part, and may finish with a nonempty repeating part enclosed in parentheses. An empty non-repeating part after the decimal point is allowed, as in `"1."` or `"1.(9)"`.

Parentheses mean that their digits repeat forever. Different strings can therefore denote the same value: a repeating block may be shifted or repeated, and an infinite tail of nines can carry into the preceding digits. Return `true` exactly when `s` and `t` denote the same rational number.

### Function Contract

**Inputs**

- `s` and `t`: valid non-negative rational-number representations.
- Each integer part has from $1$ through $4$ digits and no leading zero except the integer `0`.
- Each non-repeating fractional part has from $0$ through $4$ digits.
- When present, each repeating part has from $1$ through $4$ digits.
- Let $L=\lvert s\rvert+\lvert t\rvert$ be the total representation length.

**Return value**

Return `true` if both strings have exactly the same rational value; otherwise return `false`.

### Examples

**Example 1**

- Input: `s = "0.(52)", t = "0.5(25)"`
- Output: `true`

**Example 2**

- Input: `s = "0.1666(6)", t = "0.166(66)"`
- Output: `true`

**Example 3**

- Input: `s = "0.9(9)", t = "1."`
- Output: `true`
