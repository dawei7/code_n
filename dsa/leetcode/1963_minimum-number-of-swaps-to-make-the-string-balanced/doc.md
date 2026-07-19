# Minimum Number of Swaps to Make the String Balanced

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1963 |
| Difficulty | Medium |
| Topics | Two Pointers, String, Stack, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) |

## Problem Description
### Goal
The even-length string `s` contains equal numbers of opening brackets `"["`
and closing brackets `"]"`. A string is balanced when it is empty, is a
concatenation of balanced strings, or has the form `[C]` for a balanced string
`C`.

In one operation, swap the brackets at any two indices; the positions do not
need to be adjacent. Perform as few swaps as possible to make `s` balanced,
and return that minimum number.

### Function Contract
**Inputs**

- `s`: an even-length bracket string of length $N$, where
  $2\le N\le10^6$, containing exactly $N/2$ copies of each bracket.

**Return value**

- The minimum number of arbitrary index swaps needed to make `s` balanced.

### Examples
**Example 1**

- Input: `s = "][]["`
- Output: `1`

**Example 2**

- Input: `s = "]]][[["`
- Output: `2`

**Example 3**

- Input: `s = "[]"`
- Output: `0`
