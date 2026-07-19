# Sum of Beauty of All Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1781 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/) |

## Problem Description

### Goal

The beauty of a nonempty string is the frequency of its most frequent character minus the frequency of its least frequent character. Only characters that occur in the string participate in these two frequencies; absent letters are not counted as having frequency zero.

Given a string `s` containing lowercase English letters, consider every contiguous, nonempty substring. Return the sum of their beauty values. Substrings with all present characters occurring equally often contribute zero.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$.
- The constraints guarantee $1 \le n \le 500$.

**Return value**

For substring $s[i\mathbin{:}j]$, let $f_c(i,j)$ be the frequency of a present character $c$. Return

$$
\sum_{0\le i<j\le n}
\left(
\max_c f_c(i,j)-\min_{c:f_c(i,j)>0}f_c(i,j)
\right).
$$

### Examples

**Example 1**

- Input: `s = "aabcb"`
- Output: `5`
- Explanation: Five substrings have beauty one, and every other substring has beauty zero.

**Example 2**

- Input: `s = "aabcbaa"`
- Output: `17`

**Example 3**

- Input: `s = "aaaa"`
- Output: `0`
- Explanation: Every substring contains only `a`, so its maximum and minimum present frequencies are equal.
