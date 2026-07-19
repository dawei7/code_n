# Lexicographical Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 386 |
| Difficulty | Medium |
| Topics | Depth-First Search, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographical-numbers/) |

## Problem Description
### Goal
Given a positive integer `n`, return every integer in the range `[1, n]` sorted in lexicographical order of its decimal representation. This is dictionary-style text order, so a number precedes its longer extensions and `10` appears before `2`.

Return the ordered integers as numbers rather than strings. Generate the sequence in $O(n)$ time using constant auxiliary traversal space beyond the required output, without converting and sorting all values as text. Never include zero or values above `n`, and correctly backtrack across completed decimal-prefix branches such as the transition after a value ending in `9`.

### Function Contract
**Inputs**

- `n`: the inclusive positive upper bound

**Return value**

- Return a list containing each integer in `[1, n]` exactly once in lexicographical order.

### Examples
**Example 1**

- Input: `n = 13`
- Output: `[1,10,11,12,13,2,3,4,5,6,7,8,9]`

**Example 2**

- Input: `n = 2`
- Output: `[1,2]`

**Example 3**

- Input: `n = 20`
- Output: `[1,10,11,12,13,14,15,16,17,18,19,2,20,3,4,5,6,7,8,9]`
