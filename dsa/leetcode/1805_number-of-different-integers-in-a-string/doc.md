# Number of Different Integers in a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-different-integers-in-a-string/) |
| Frontend ID | 1805 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A string `word` contains lowercase English letters and decimal digits. Treat every maximal consecutive run of digits as one nonnegative integer; letters separate neighboring runs.

Two digit runs represent the same integer when they differ only by leading zeros. For example, `"1"`, `"01"`, and `"001"` are one value, and every run consisting only of zeros represents zero. Return how many distinct integers occur in the string.

### Function Contract

**Inputs**

- `word`: a string of length $n$, where $1 \le n \le 1000$ and every character is a lowercase English letter or a decimal digit.

**Return value**

- Return the number of distinct integer values represented by maximal digit runs in `word`.

### Examples

**Example 1**

- Input: `word = "a123bc34d8ef34"`
- Output: `3`

The digit runs represent `123`, `34`, `8`, and `34`.

**Example 2**

- Input: `word = "leet1234code234"`
- Output: `2`

The two represented values are `1234` and `234`.

**Example 3**

- Input: `word = "a1b01c001"`
- Output: `1`

All three runs normalize to the integer value one.
