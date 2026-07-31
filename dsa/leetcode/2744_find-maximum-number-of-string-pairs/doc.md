# Find Maximum Number of String Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2744 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-maximum-number-of-string-pairs/) |

## Problem Description

### Goal

An array `words` contains distinct two-character lowercase strings. Two different indices $i<j$ form a pair when `words[i]` equals the reversal of `words[j]`.

Choose as many such pairs as possible while using each string in at most one pair. Return the maximum number formed. A two-character palindrome such as `"aa"` cannot pair with itself, and distinctness means there is no second identical copy available.

### Function Contract

Let $n$ be the number of strings.

**Inputs**

- `words`: An array of distinct lowercase strings, where $1 \le n \le 50$ and every string has length exactly $2$.

**Return value**

Return the maximum number of disjoint index pairs whose strings are reversals of one another.

### Examples

**Example 1**

- Input: `words = ["cd","ac","dc","ca","zz"]`
- Output: `2`
- Explanation: Pair `"cd"` with `"dc"` and `"ac"` with `"ca"`; `"zz"` has no separate partner.

**Example 2**

- Input: `words = ["ab","ba","cc"]`
- Output: `1`
- Explanation: Only `"ab"` and `"ba"` form a pair.

**Example 3**

- Input: `words = ["aa","ab"]`
- Output: `0`
- Explanation: `"aa"` cannot pair with itself, and `"ba"` is absent.
