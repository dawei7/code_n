# Encode Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1256 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-number/) |

## Problem Description

### Goal

Nonnegative integers are encoded in groups of binary strings ordered first by length and then by binary value. The number `0` is encoded as the empty string; `1` and `2` are encoded as `"0"` and `"1"`; `3` through `6` are encoded as `"00"`, `"01"`, `"10"`, and `"11"`; subsequent groups continue in the same pattern.

Given a nonnegative integer `num`, return its encoding under this scheme. The result contains only the characters `"0"` and `"1"`, except that the encoding of zero contains no characters.

### Function Contract

**Inputs**

- `num`: an integer satisfying $0 \le \texttt{num} \le 10^9$.
- Let $q=\texttt{num}+1$.

**Return value**

- Return the binary encoding assigned to `num` by the stated length-grouped sequence.

### Examples

**Example 1**

- Input: `num = 23`
- Output: `"1000"`
- Explanation: `num + 1` is `24`, whose binary form is `"11000"`; removing its leading `"1"` leaves `"1000"`.

**Example 2**

- Input: `num = 107`
- Output: `"101100"`

**Example 3**

- Input: `num = 0`
- Output: `""`
