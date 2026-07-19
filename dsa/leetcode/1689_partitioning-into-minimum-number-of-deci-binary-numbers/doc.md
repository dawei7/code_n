# Partitioning Into Minimum Number Of Deci-Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1689 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/) |

## Problem Description
### Goal

A positive decimal integer is deci-binary when every digit in its ordinary base-10 representation is either `0` or `1`. For example, `10` and `101` are deci-binary, whereas a number containing any digit from `2` through `9` is not.

The positive integer to decompose is supplied as a decimal string `n`, which may be much longer than a built-in numeric type can hold. Express its value as a sum of positive deci-binary integers and return the minimum possible number of addends. Only the count is required, not the addends themselves.

### Function Contract
**Inputs**

- `n`: the digit string of a positive decimal integer with no leading zero, of length $L$

**Return value**

The minimum number of positive deci-binary integers whose arithmetic sum equals the value represented by `n`.

### Examples
**Example 1**

- Input: `n = "32"`
- Output: `3`

One decomposition is `11 + 11 + 10`.

**Example 2**

- Input: `n = "82734"`
- Output: `8`

The leading digit 8 already requires eight addends.

**Example 3**

- Input: `n = "27346209830709182346"`
- Output: `9`

The string contains a digit 9, which determines the answer.
