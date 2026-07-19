# Decode Ways

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 91 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-ways/) |

## Problem Description
### Goal
Letters are encoded by the integers `1` through `26`, mapping in order from `A` through `Z`. Given a nonempty decimal digit string, split it into one- or two-digit codes and decode every part using that mapping.

Return the number of complete valid decodings. Different split boundaries count as different ways even when prefixes overlap. A zero has no standalone letter and is valid only inside `10` or `20`; leading zeroes and pairs above `26` invalidate the affected split. Return zero when no full decoding exists.

### Function Contract
**Inputs**

- `s`: a nonempty string of decimal digits

**Return value**

The number of valid complete decodings.

### Examples
**Example 1**

- Input: `s = "12"`
- Output: `2`

**Example 2**

- Input: `s = "226"`
- Output: `3`

**Example 3**

- Input: `s = "06"`
- Output: `0`
