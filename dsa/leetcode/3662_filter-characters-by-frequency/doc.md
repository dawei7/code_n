# Filter Characters by Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3662 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/filter-characters-by-frequency/) |

## Problem Description
### Goal

Given a string `s` of lowercase English letters and an integer `k`, determine each character's frequency across the complete original string.

Construct a new string by retaining exactly the occurrences whose character appears strictly fewer than `k` times in `s`. If a character qualifies, keep every one of its occurrences; if its frequency is at least `k`, remove all of them.

Preserve the original left-to-right order of every retained occurrence. Return the constructed string, or the empty string when no character has a qualifying frequency.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase English string of length $n$, where $1\le n\le100$.
- `k`: an integer threshold satisfying $1\le k\le n$.

**Return value**

Return the stable-order subsequence containing all and only occurrences of characters whose total frequency in `s` is less than `k`.

### Examples

**Example 1**

- Input: `s = "aadbbcccca"`, `k = 3`
- Output: `"dbb"`
- The frequencies of `a`, `b`, `c`, and `d` are `3`, `2`, `4`, and `1`; only `b` and `d` qualify.

**Example 2**

- Input: `s = "xyz"`, `k = 2`
- Output: `"xyz"`
- Every character occurs once, which is strictly below `2`.

**Example 3**

- Input: `s = "aabcc"`, `k = 2`
- Output: `"b"`
- Frequencies equal to the threshold do not qualify.
