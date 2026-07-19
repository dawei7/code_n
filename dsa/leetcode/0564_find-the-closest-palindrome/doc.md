# Find the Closest Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 564 |
| Difficulty | Hard |
| Topics | Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-closest-palindrome/) |

## Problem Description
### Goal
Given a string `n` representing a positive integer, find the nearest integer whose decimal representation is a palindrome. The returned value must be different from `n` itself, even when `n` is already palindromic, and it must be returned as a decimal string without leading zeroes.

Choose the palindrome having the smallest absolute numerical difference from `n`. If two different palindromes are equally near, return the smaller one. Distance is based on integer value rather than on the number of changed digits or characters.

### Function Contract
**Inputs**

- `n`: the decimal representation of a positive integer

**Return value**

- The decimal string of the nearest different palindrome

### Examples
**Example 1**

- Input: `n = "123"`
- Output: `"121"`

**Example 2**

- Input: `n = "1"`
- Output: `"0"`

**Example 3**

- Input: `n = "99"`
- Output: `"101"`
