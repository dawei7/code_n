# Count Sorted Vowel Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1641 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-sorted-vowel-strings/) |

## Problem Description
### Goal
Given an integer `n`, count the length-$n$ strings made only from the vowels `a`, `e`, `i`, `o`, and `u` whose characters are in lexicographically sorted order.

A string is lexicographically sorted when every character is the same as or alphabetically before the character immediately following it. Thus repeated vowels are allowed, while a later vowel can never be followed by an earlier one.

### Function Contract
**Inputs**

- `n`: the required string length, where $1 \le n \le 50$.

**Return value**

Return the number of non-decreasing length-$n$ strings over the five vowels.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `5`

Each individual vowel forms one sorted string.

**Example 2**

- Input: `n = 2`
- Output: `15`

The valid pairs include `"aa"`, `"ae"`, and `"uu"`; a pair such as `"ea"` is excluded because it decreases.

**Example 3**

- Input: `n = 33`
- Output: `66045`
