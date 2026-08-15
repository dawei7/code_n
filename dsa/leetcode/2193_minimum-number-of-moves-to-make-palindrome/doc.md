# Minimum Number of Moves to Make Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2193 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/) |

## Problem Description

### Goal

Given a string `s` containing only lowercase English letters, one move may
swap any two adjacent characters. Such swaps preserve the multiset of
characters but can rearrange their positions.

Find the minimum number of moves required to arrange the entire string as a
palindrome. The input guarantees that some palindromic arrangement is
possible, so at most one character has an odd frequency.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1\le n\le2000$, whose
  character counts permit a palindrome.

**Return value**

Return the minimum number of adjacent swaps needed to make `s` a palindrome.

### Examples

#### Example 1

- **Input:** `s = "aabb"`
- **Output:** `2`

#### Example 2

- **Input:** `s = "letelt"`
- **Output:** `2`

#### Example 3

- **Input:** `s = "ntiin"`
- **Output:** `1`
