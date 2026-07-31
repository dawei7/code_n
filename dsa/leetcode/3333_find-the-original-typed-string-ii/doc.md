# Find the Original Typed String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3333 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-original-typed-string-ii/) |

## Problem Description

### Goal

Alice intended to type a lowercase string, but she may hold a key for too long and make one intended character appear several consecutive times. The string `word` is the final text displayed on the screen. Within any maximal run of equal displayed characters, the intended string may have contained any positive number of that character up to the displayed run length.

Given a positive integer `k`, count the distinct intended strings that could produce `word` and whose length is at least $k$. Different choices of intended length within any run can combine independently. Because the number of possibilities may be large, return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `word`: A nonempty lowercase English string with length $n$, where $1 \le n \le 5 \cdot 10^5$.
- `k`: The minimum permitted length of the intended string, where $1 \le k \le 2000$.

**Return value**

- The number of possible original strings of length at least $k$, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `word = "aabbccdd", k = 7`
- Output: `5`
- Explanation: The displayed word itself and the four strings formed by shortening exactly one run to one character have sufficient length.

**Example 2**

- Input: `word = "aabbccdd", k = 8`
- Output: `1`
- Explanation: Only the full displayed word reaches length $8$.

**Example 3**

- Input: `word = "aaabbb", k = 3`
- Output: `8`
