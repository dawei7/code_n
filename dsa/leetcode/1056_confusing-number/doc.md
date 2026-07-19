# Confusing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1056 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/confusing-number/) |

## Problem Description

### Goal

A **confusing number** becomes a different valid number after being rotated $180$ degrees. Under this rotation, digits `0`, `1`, `6`, `8`, and `9` become `0`, `1`, `9`, `8`, and `6`, respectively. Digits `2`, `3`, `4`, `5`, and `7` become invalid.

Rotate every digit of the non-negative integer `n`, reverse their positional order as the display turns, and ignore any leading zeros in the rotated result. Return `true` only when all digits remain valid and the rotated numeric value differs from `n`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^9$; let $D$ be its number of decimal digits, with zero having one digit.

**Return value**

- `true` if rotating `n` produces a valid different number; otherwise, `false`.

### Examples

**Example 1**

- Input: `n = 6`
- Output: `true`
- Explanation: Rotation produces `9`.

**Example 2**

- Input: `n = 89`
- Output: `true`
- Explanation: Rotation reverses the positions and maps the digits, producing `68`.

**Example 3**

- Input: `n = 11`
- Output: `false`
- Explanation: The rotated value is still `11`.
