# Minimum Insertion Steps to Make a String Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1312 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) |

## Problem Description
### Goal
Given a lowercase string `s`, one step may insert any character at any position. Existing characters cannot be removed, replaced, or reordered.

Find the minimum number of insertion steps needed to make the resulting string a palindrome—a string that reads identically from left to right and from right to left. Return only the minimum count; the constructed palindrome itself is not required.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $n$, where $1\le n\le500$.

**Return value**

The smallest number of arbitrary character insertions that can transform `s` into a palindrome while preserving every original character in order.

### Examples
**Example 1**

- Input: `s = "zzazz"`
- Output: `0`
- Explanation: The input is already a palindrome.

**Example 2**

- Input: `s = "mbadm"`
- Output: `2`
- Explanation: Two insertions can form `"mbdadbm"` or another palindrome; one insertion cannot suffice.

**Example 3**

- Input: `s = "leetcode"`
- Output: `5`
