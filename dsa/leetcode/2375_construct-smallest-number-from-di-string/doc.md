# Construct Smallest Number From DI String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2375 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-smallest-number-from-di-string/) |

## Problem Description

### Goal

Given a 0-indexed string `pattern` containing only `'I'` and `'D'`, construct a digit string `num` with one more character than the pattern. Each digit must come from `'1'` through `'9'`, and no digit may be used more than once.

For every pattern position `i`, `'I'` requires `num[i] < num[i + 1]`, while `'D'` requires `num[i] > num[i + 1]`. Among all strings satisfying every comparison and the distinct-digit rule, return the lexicographically smallest possible `num`.

### Function Contract

**Inputs**

- `pattern`: A string of length $n$, where $1 \le n \le 8$ and every character is either `'I'` or `'D'`.

**Return value**

- Return the lexicographically smallest length-$(n+1)$ string of distinct digits from `'1'` through `'9'` that realizes all comparisons in `pattern`.

**Comparison semantics**

- `'I'` means the digit immediately before it in `num` is smaller than the digit immediately after it.
- `'D'` means the preceding digit is larger than the following digit.
- Digits are compared by value; all digits are distinct.

### Examples

**Example 1**

- Input: `pattern = "IIIDIDDD"`
- Output: `"123549876"`
- Explanation: Every adjacent comparison matches the pattern, all nine digits are distinct, and no valid string is lexicographically smaller.

**Example 2**

- Input: `pattern = "DDD"`
- Output: `"4321"`
- Explanation: Four distinct digits must decrease throughout; using the smallest four digits in reverse order gives the smallest valid string.
