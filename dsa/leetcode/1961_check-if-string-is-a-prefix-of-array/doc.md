# Check If String Is a Prefix of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1961 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/) |

## Problem Description
### Goal
Given a string `s` and an ordered array of strings `words`, determine whether
`s` is a prefix string of the array.

Specifically, `s` qualifies when there is a positive integer `k`, no larger
than the number of words, such that concatenating exactly the first `k` entries
of `words` produces `s`. The match must therefore end at a word boundary;
ending partway through the next word is not sufficient. Return whether such a
prefix exists.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $L$, where $1\le L\le1000$.
- `words`: between $1$ and $100$ nonempty lowercase English strings, each
  having length at most $20$.

**Return value**

- `True` if `s` equals the concatenation of the first `k` words for some
  positive valid `k`; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "iloveleetcode", words = ["i", "love", "leetcode", "apples"]`
- Output: `True`

**Example 2**

- Input: `s = "iloveleetcode", words = ["apples", "i", "love", "leetcode"]`
- Output: `False`

**Example 3**

- Input: `s = "abc", words = ["ab", "cd"]`
- Output: `False`
