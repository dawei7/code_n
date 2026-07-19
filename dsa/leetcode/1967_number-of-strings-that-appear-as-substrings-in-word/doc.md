# Number of Strings That Appear as Substrings in Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1967 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) |

## Problem Description
### Goal
Given an array of strings `patterns` and a string `word`, count how many array
entries occur as substrings of `word`. A substring is a contiguous sequence of
characters.

Each position in `patterns` is counted independently. Thus, if the same pattern
appears several times in the array and occurs in `word`, every copy
contributes one to the answer. A pattern contributes at most once regardless
of how many different occurrences it has inside `word`.

### Function Contract
**Inputs**

- `patterns`: a list of $P$ nonempty lowercase strings, where
  $1\le P\le100$ and each length is at most $100$.
- `word`: a nonempty lowercase string of length $M$, where $1\le M\le100$.
- Let $T$ be the sum of all pattern lengths and $L$ the maximum pattern
  length.

**Return value**

- The number of entries in `patterns` that occur contiguously in `word`.

### Examples
**Example 1**

- Input: `patterns = ["a", "abc", "bc", "d"], word = "abc"`
- Output: `3`

**Example 2**

- Input: `patterns = ["a", "b", "c"], word = "aaaaabbbbb"`
- Output: `2`

**Example 3**

- Input: `patterns = ["a", "a", "a"], word = "ab"`
- Output: `3`
