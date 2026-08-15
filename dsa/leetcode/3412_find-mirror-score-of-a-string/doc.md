# Find Mirror Score of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3412 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-mirror-score-of-a-string/) |

## Problem Description

### Goal

You are given a lowercase English string `s`. A letter's mirror is the letter in the same position when the alphabet is reversed: `a` mirrors `z`, `b` mirrors `y`, and so on.

Initially every index is unmarked and the score is zero. Process the indices from left to right. At index `i`, find the closest unmarked index `j` to its left whose character is the mirror of `s[i]`. If one exists, mark both `i` and `j` and add `i - j` to the score. If none exists, leave `i` unmarked and continue. Return the score after the complete scan.

### Function Contract

**Inputs**

- `s`: The lowercase English string to process.

The constraint is $1\le\lvert\texttt{s}\rvert\le10^5$.

**Return value**

- The total score produced by the prescribed left-to-right matching process.

### Examples

#### Example 1

- **Input:** `s = "aczzx"`
- **Output:** `5`

The `z` at index 2 pairs with the `a` at index 0 for 2 points. The `x` at index 4 then pairs with the `c` at index 1 for 3 more points.

#### Example 2

- **Input:** `s = "abcdef"`
- **Output:** `0`

No character has an earlier unmarked mirror.
