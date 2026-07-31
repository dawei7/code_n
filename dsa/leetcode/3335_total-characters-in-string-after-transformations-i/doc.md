# Total Characters in String After Transformations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3335 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Dynamic Programming, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/) |

## Problem Description

### Goal

You are given a lowercase string `s` and must transform every character simultaneously, repeating the operation exactly `t` times. In one operation, each character other than `z` advances to the next letter of the alphabet: `a` becomes `b`, `b` becomes `c`, and so forth.

The special character `z` is replaced by the two-character string `"ab"`, so the string may grow. Determine the length of the complete string after all `t` transformations. Return the length modulo $10^9+7$ because repeated splits can make it very large.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string with length $n$, where $1 \le n \le 10^5$.
- `t`: The exact number of simultaneous transformations, where $1 \le t \le 10^5$.

**Return value**

- The transformed string's length after exactly $t$ operations, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `s = "abcyy", t = 2`
- Output: `7`
- Explanation: The successive strings are `"bcdzz"` and `"cdeabab"`.

**Example 2**

- Input: `s = "azbk", t = 1`
- Output: `5`
- Explanation: The transformed string is `"babcl"`; the original `z` contributes `"ab"`.
