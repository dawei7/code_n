# Minimum Moves to Convert String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2027 |
| Difficulty | Easy |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-convert-string/) |

## Problem Description

### Goal

A string `s` contains only `X` and `O`. In one move, choose any three
consecutive positions and convert all three characters to `O`; a position that
already contains `O` remains unchanged.

Find the minimum number of moves needed to eliminate every `X`. Moves may
overlap, and a move is allowed to include existing `O` characters when doing
so covers an `X`.

### Function Contract

Let $N$ be the length of `s`.

**Inputs**

- `s`: a string of $N$ characters, each either `X` or `O`, where
  $3 \le N \le 1000$.

**Return value**

- The minimum number of length-three conversion moves required to make every
  character `O`.

### Examples

**Example 1**

- Input: `s = "XXX"`
- Output: `1`

**Example 2**

- Input: `s = "XXOX"`
- Output: `2`
- Explanation: One move covers the first three positions, and a second covers
  the final `X`.

**Example 3**

- Input: `s = "OOOO"`
- Output: `0`
