# Find the Shortest Superstring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 943 |
| Difficulty | Hard |
| Topics | Array, String, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-shortest-superstring/) |

## Problem Description

### Goal

Given an array `words` of unique lowercase English strings, construct the shortest string that contains every member of `words` as a substring. A word may begin at any position in the result, and overlapping suffixes and prefixes may share the same characters rather than being repeated.

No input word is a substring of another input word. If several strings have the minimum possible length while containing all the words, any one of those shortest superstrings may be returned.

### Function Contract

Let $m$ be the number of strings and let $\ell$ be the maximum string length. Define

$$
T = m^2 2^m + m^2 \ell^2,
\qquad
S = m2^m + m^2.
$$

**Inputs**

- `words`: a list of $m$ unique lowercase English strings, where $1 \le m \le 12$ and each string has length from $1$ through $20$.
- No string in `words` is a substring of another string in `words`.

**Return value**

Return any minimum-length string that contains every string in `words` as a substring.

### Examples

**Example 1**

- Input: `words = ["alex", "loves", "leetcode"]`
- Output: `"alexlovesleetcode"`

There are no useful overlaps here, so concatenating the three words in any order has minimum length and is acceptable.

**Example 2**

- Input: `words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]`
- Output: `"gctaagttcatgcatc"`
