# Decrypt String from Alphabet to Integer Mapping

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1309 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/) |

## Problem Description
### Goal
A valid encoded string `s` represents lowercase English letters with digits and `#` markers. The letters `a` through `i` use the one-character codes `1` through `9`, respectively. The letters `j` through `z` use `10#` through `26#`, respectively.

Decode every token in order and return the resulting lowercase string. The input is guaranteed to follow this encoding and to have a unique valid interpretation, so malformed codes do not need a fallback result.

### Function Contract
**Inputs**

- `s`: a valid encoded string containing digits and possibly `#`.
- Its length $n$ satisfies $1\le n\le1000$.
- Every token is either one digit from `1` to `9` or a two-digit value from `10` to `26` followed by `#`.

**Return value**

The lowercase English string obtained by replacing each encoded integer $v$ with the $v$th letter of the alphabet.

### Examples
**Example 1**

- Input: `s = "10#11#12"`
- Output: `"jkab"`
- Explanation: `10#` and `11#` decode to `j` and `k`; the final `1` and `2` decode separately.

**Example 2**

- Input: `s = "1326#"`
- Output: `"acz"`

**Example 3**

- Input: `s = "123456789"`
- Output: `"abcdefghi"`
