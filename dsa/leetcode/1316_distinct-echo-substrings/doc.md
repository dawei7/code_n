# Distinct Echo Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1316 |
| Difficulty | Hard |
| Topics | String, Trie, Rolling Hash, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/distinct-echo-substrings/) |

## Problem Description
### Goal
An echo substring is a nonempty substring that can be written as `a + a` for some nonempty string `a`; its first half and second half are identical.

Given a lowercase string `text`, count how many distinct echo-substring values occur anywhere in it. Multiple occurrences of the same substring contribute only once, while equal-length echo substrings with different characters are distinct.

### Function Contract
**Inputs**

- `text`: a lowercase English string of length $n$, where $1\le n\le2000$.

**Return value**

The number of distinct nonempty substrings of `text` whose length is even and whose two halves are equal.

### Examples
**Example 1**

- Input: `text = "abcabcabc"`
- Output: `3`
- Explanation: The distinct echo substrings are `"abcabc"`, `"bcabca"`, and `"cabcab"`.

**Example 2**

- Input: `text = "leetcodeleetcode"`
- Output: `2`
- Explanation: The qualifying values are `"ee"` and `"leetcodeleetcode"`.

**Example 3**

- Input: `text = "aaaa"`
- Output: `2`
- Explanation: `"aa"` and `"aaaa"` are distinct echo substrings.
