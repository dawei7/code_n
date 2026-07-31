# Maximum Difference Between Even and Odd Frequency I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3442 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/) |

## Problem Description

### Goal

For each distinct lowercase letter in a string, consider how often it occurs. Choose one present character whose frequency is odd and another present character whose frequency is even.

Maximize the odd-frequency character's count minus the even-frequency character's count, and return that difference. The input guarantees that both kinds of frequency exist, so a valid pair can always be selected.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length from $3$ through $100$.

At least one present character has odd frequency and at least one has even frequency.

**Return value**

Return the maximum value of $\operatorname{freq}(a_1)-\operatorname{freq}(a_2)$ where $a_1$ has odd frequency and $a_2$ has even frequency.

### Examples

**Example 1**

- Input: `s = "aaaaabbc"`
- Output: `3`

The largest odd frequency is $5$ for `a`, while `b` has the smallest even frequency $2$.

**Example 2**

- Input: `s = "abcabcab"`
- Output: `1`

The odd frequency $3$ of `a` minus the even frequency $2$ of `c` gives $1$.
