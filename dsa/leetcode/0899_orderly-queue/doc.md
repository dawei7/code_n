# Orderly Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 899 |
| Difficulty | Hard |
| Topics | Math, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/orderly-queue/) |

## Problem Description
### Goal
You are given a lowercase English string `s` and an integer `k`. In one move, choose any one of the first `k` characters currently in the string, remove that character from its position, and append it to the end.

The move may be applied any number of times, including zero. Each choice changes which characters occupy the first `k` positions and can therefore enable later choices.

Return the lexicographically smallest string reachable through this process.

### Function Contract
Let $n$ be the length of `s`.

**Inputs**

- `s`: a string of lowercase English letters with $1 \leq n \leq 1000$.
- `k`: the size of the selectable prefix, where $1 \leq k \leq n$.

**Return value**

Return the lexicographically smallest string obtainable after any number of valid moves.

### Examples
**Example 1**

- Input: `s = "cba", k = 1`
- Output: `"acb"`

Only the first character can move, so the reachable strings are rotations; moving `"c"` and then `"b"` produces the smallest rotation.

**Example 2**

- Input: `s = "baaca", k = 3`
- Output: `"aaabc"`

**Example 3**

- Input: `s = "abc", k = 1`
- Output: `"abc"`
