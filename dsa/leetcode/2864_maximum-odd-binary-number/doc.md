# Maximum Odd Binary Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2864 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-odd-binary-number/) |

## Problem Description

### Goal

You are given a binary string `s` containing at least one `1`. Rearrange all of its bits to form the greatest possible odd binary number, then return that arrangement as a string.

Every input bit must be used exactly once in the rearranged string. An odd binary number must end in `1`, and the returned representation is allowed to begin with zeros.

### Function Contract

**Inputs**

- `s`: A string consisting only of `0` and `1` characters and containing at least one `1`.

Let $n$ be the length of `s`. The input satisfies $1 \le n \le 100$.

**Return value**

- Return the lexicographically greatest rearrangement of all bits that ends in `1` and therefore represents an odd binary number.

### Examples

**Example 1**

- Input: `s = "010"`
- Output: `"001"`
- Explanation: The only available `1` must occupy the final position. Leading zeros are permitted.

**Example 2**

- Input: `s = "0101"`
- Output: `"1001"`
- Explanation: Reserve one `1` for the last bit, then place the other `1` before both zeros.
