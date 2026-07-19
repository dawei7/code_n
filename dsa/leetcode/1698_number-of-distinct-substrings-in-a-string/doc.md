# Number of Distinct Substrings in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1698 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Trie, Rolling Hash, Suffix Array, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/) |

## Problem Description
### Goal

Given a lowercase English string `s`, count the different nonempty strings that occur as contiguous substrings of `s`. A substring is formed by removing zero or more characters from the front and zero or more characters from the back, so the remaining characters must stay adjacent and in order.

Equal substring contents count once even when they occur at several positions. Substrings of different lengths are different, and the empty string is not included. Return the number of distinct substring contents represented anywhere in `s`.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 500$

**Return value**

The number of distinct nonempty contiguous substrings of `s`.

### Examples
**Example 1**

- Input: `s = "aabbaba"`
- Output: `21`

Repeated occurrences such as `"a"`, `"b"`, and `"ba"` contribute only once apiece.

**Example 2**

- Input: `s = "abcdefg"`
- Output: `28`

Every substring is distinct, so the count is $7 \cdot 8 / 2 = 28$.

**Example 3**

- Input: `s = "aaaa"`
- Output: `4`

The only distinct contents are `"a"`, `"aa"`, `"aaa"`, and `"aaaa"`.
