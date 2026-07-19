# String Without AAA or BBB

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 984 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/string-without-aaa-or-bbb/) |

## Problem Description

### Goal

Given two integers `a` and `b`, construct any string `s` containing exactly `a` copies of the letter `"a"` and exactly `b` copies of the letter `"b"`.

The resulting string must have length `a + b`. It must not contain `"aaa"` as a substring, and it must not contain `"bbb"` as a substring. Several different arrangements may satisfy these conditions; returning any one of them is valid. The input is guaranteed to admit at least one valid arrangement.

### Function Contract

**Inputs**

- `a`: the required number of `"a"` characters, where $0\le A=\texttt{a}\le100$.
- `b`: the required number of `"b"` characters, where $0\le B=\texttt{b}\le100$.

Let $L=A+B$ be the required output length.

**Return value**

- Any length-$L$ string with exactly $A$ letters `"a"`, exactly $B$ letters `"b"`, and no run of three equal letters.

### Examples

**Example 1**

- Input: `a = 1, b = 2`
- Output: `"abb"`
- Explanation: `"bab"` and `"bba"` are also valid.

**Example 2**

- Input: `a = 4, b = 1`
- Output: `"aabaa"`
