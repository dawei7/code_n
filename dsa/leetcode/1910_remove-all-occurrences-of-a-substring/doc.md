# Remove All Occurrences of a Substring

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/) |
| Frontend ID | 1910 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given lowercase strings `s` and `part`. While `part` occurs as a contiguous substring of the current `s`, locate its leftmost occurrence and remove exactly those characters.

Continue on the newly joined string until no occurrence remains, then return that final string. A deletion can bring characters from opposite sides of the removed interval together, so it may create a new occurrence that was not contiguous before the deletion.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $N$.
- `part`: a non-empty lowercase English pattern of length $M$.
- $1 \le N, M \le 1000$.

**Return value**

- Return the string remaining after repeatedly deleting the leftmost occurrence of `part`.

### Examples

**Example 1**

- Input: `s = "daabcbaabcbc", part = "abc"`
- Output: `"dab"`

The successive strings are `"dabaabcbc"`, `"dababc"`, and `"dab"`.

**Example 2**

- Input: `s = "axxxxyyyyb", part = "xy"`
- Output: `"ab"`

Each deletion joins another `x` to another `y`, exposing the next `"xy"`.

**Example 3**

- Input: `s = "aaaaa", part = "aa"`
- Output: `"a"`

Two leftmost pairs are removed, leaving one unmatched character.
