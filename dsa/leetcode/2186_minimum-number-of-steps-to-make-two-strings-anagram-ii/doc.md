# Minimum Number of Steps to Make Two Strings Anagram II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/) |

## Problem Description

### Goal

Two lowercase strings `s` and `t` may contain different numbers of each
letter. In one step, append any one lowercase character to either string.
Existing characters cannot be removed or changed.

Find the minimum number of append operations needed so the two resulting
strings are anagrams. Anagrams contain equal frequencies of every character;
their character order may differ or remain the same. Appends may be required
on both strings to balance different letters.

### Function Contract

**Inputs**

- `s`: a lowercase English string.
- `t`: another lowercase English string.

Each input length is in $[1,2\cdot10^5]$.

**Return value**

Return the minimum total number of single-character appends needed to make
`s` and `t` anagrams.

### Examples

#### Example 1

- **Input:** `s = "leetcode"`, `t = "coats"`
- **Output:** `7`

#### Example 2

- **Input:** `s = "night"`, `t = "thing"`
- **Output:** `0`

#### Example 3

- **Input:** `s = "a"`, `t = "b"`
- **Output:** `2`
