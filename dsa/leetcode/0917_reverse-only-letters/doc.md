# Reverse Only Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 917 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-only-letters/) |

## Problem Description
### Goal

Given a string `s`, reverse the order of its English letters while preserving every other character at its original index. Both lowercase and uppercase English letters participate in the reversal, and their case travels with the character.

Characters that are not English letters must not move. Return the resulting string after the letters have been placed in reverse order around those fixed positions.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 100$.
- Every character has an ASCII value from $33$ through $122$. The string contains neither a double quote nor a backslash.

**Return value**

A string of the same length in which the subsequence of English letters is reversed and every non-letter remains at its original index.

### Examples
**Example 1**

- Input: `s = "ab-cd"`
- Output: `"dc-ba"`

**Example 2**

- Input: `s = "a-bC-dEf-ghIj"`
- Output: `"j-Ih-gfE-dCba"`

**Example 3**

- Input: `s = "Test1ng-Leet=code-Q!"`
- Output: `"Qedo1ct-eeLg=ntse-T!"`
