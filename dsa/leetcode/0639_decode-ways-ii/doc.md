# Decode Ways II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 639 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-ways-ii/) |

## Problem Description
### Goal
A message maps letters `A` through `Z` to the numbers `1` through `26`. Given an encoded string `s`, count the ways to split all of its characters into valid one- or two-digit codes and map them back to letters. A code with a leading zero, such as `06`, is invalid.

The string may also contain `*`, and each occurrence independently represents any digit from `1` through `9`, never `0`. Count all valid choices of wildcard digits and groupings, then return the total modulo `1,000,000,007`. A literal `0` can participate only as the second digit of `10` or `20`, including wildcard combinations that realize those codes.

### Function Contract
**Inputs**

- `s`: a nonempty string containing decimal digits and `*` wildcards

**Return value**

- The number of complete valid decodings modulo `1,000,000,007`
- A zero cannot decode alone and is valid only inside `10` or `20`, including wildcard forms that realize those pairs

### Examples
**Example 1**

- Input: `s = "*"`
- Output: `9`

**Example 2**

- Input: `s = "1*"`
- Output: `18`

**Example 3**

- Input: `s = "2*"`
- Output: `15`
