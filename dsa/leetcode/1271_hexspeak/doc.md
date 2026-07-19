# Hexspeak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1271 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/hexspeak/) |

## Problem Description

### Goal

A positive decimal integer can be written in Hexspeak by first converting it to an uppercase hexadecimal string. In that string, hexadecimal digit `0` is pronounced as the letter `O`, and digit `1` is pronounced as the letter `I`. The ordinary hexadecimal letters `A` through `F` remain unchanged.

A representation is valid only when every converted character belongs to `A`, `B`, `C`, `D`, `E`, `F`, `I`, or `O`. Given the decimal integer as the string `num`, return its valid Hexspeak form. If its hexadecimal expansion contains any digit from `2` through `9`, return `"ERROR"` instead. The returned letters must be uppercase.

### Function Contract

**Inputs**

- `num`: a decimal string with no leading zeros representing an integer $n$ where $1 \le n \le 10^{12}$.
- Let $d=\lfloor\log_{16}n\rfloor+1$ be the number of hexadecimal digits. The source constraint guarantees $1 \le d \le 10$.

**Return value**

- Return the uppercase Hexspeak representation, or `"ERROR"` if any hexadecimal digit is between `2` and `9`.

### Examples

**Example 1**

- Input: `num = "257"`
- Output: `"IOI"`

**Example 2**

- Input: `num = "3"`
- Output: `"ERROR"`

**Example 3**

- Input: `num = "2827"`
- Output: `"BOB"`
