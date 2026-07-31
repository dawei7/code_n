# Reverse Degree of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3498 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-degree-of-a-string/) |

## Problem Description

### Goal

You are given a non-empty string `s` containing only lowercase English letters. Each letter receives a value from the alphabet written in reverse order: `'a'` has value $26$, `'b'` has value $25$, and the values continue downward until `'z'` has value $1$.

For every character, multiply this reversed-alphabet value by the character's 1-indexed position in `s`. The reverse degree of the string is the sum of all those products. Return that total. Repeated letters are evaluated independently because their string positions may differ.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with $1 \le \lvert\texttt{s}\rvert \le 1000$.

**Return value**

Return an integer equal to the sum of each character's reversed-alphabet value times its 1-indexed string position.

### Examples

**Example 1**

- Input: `s = "abc"`
- Output: `148`
- Explanation: The three products are $26 \cdot 1$, $25 \cdot 2$, and $24 \cdot 3$.

**Example 2**

- Input: `s = "zaza"`
- Output: `160`
- Explanation: The products are $1 \cdot 1$, $26 \cdot 2$, $1 \cdot 3$, and $26 \cdot 4$.
