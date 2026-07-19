# Longest Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 409 |
| Difficulty | Easy |
| Topics | Hash Table, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindrome/) |

## Problem Description
### Goal
Given a string containing lowercase and uppercase English letters, select any subset of its character occurrences and rearrange them to form a palindrome. Character comparison is case-sensitive, so `A` and `a` are different values.

Return the maximum possible palindrome length. Every paired character contributes two symmetric positions, and at most one leftover odd occurrence may occupy the center. Other unmatched occurrences can be discarded. The task asks only for the greatest length, not an actual palindrome. A one-character string yields `1`, and every nonempty input can contribute at least one center character.

### Function Contract
**Inputs**

- `s`: a string containing lowercase and uppercase English letters

**Return value**

- Return the maximum number of characters that can be rearranged into a palindrome.

### Examples
**Example 1**

- Input: `s = "abccccdd"`
- Output: `7`

**Example 2**

- Input: `s = "a"`
- Output: `1`

**Example 3**

- Input: `s = "bb"`
- Output: `2`
