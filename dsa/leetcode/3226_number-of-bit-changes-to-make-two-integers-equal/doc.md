# Number of Bit Changes to Make Two Integers Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3226 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/) |

## Problem Description

### Goal

You are given positive integers `n` and `k`. One change may select a bit that is currently `1` in the binary representation of `n` and turn that bit into `0`.

Return the number of changes required to make `n` equal to `k`. Bits cannot be changed from `0` to `1`, so return `-1` when the transformation is impossible. Each changed bit counts as one operation, and leading zeroes have no effect on either integer.

### Function Contract

**Inputs**

- `n`: The starting integer, with $1 \leq n \leq 10^6$.
- `k`: The required integer, with $1 \leq k \leq 10^6$.

**Return value**

Return the minimum number of `1` bits that must be cleared, or `-1` if `k` contains a `1` bit absent from `n`.

### Examples

#### Example 1

- **Input:** `n = 13, k = 4`
- **Output:** `2`
- **Explanation:** Clearing the `8` and `1` bits changes binary `1101` to `0100`.

#### Example 2

- **Input:** `n = 21, k = 21`
- **Output:** `0`
- **Explanation:** The integers already match.

#### Example 3

- **Input:** `n = 14, k = 13`
- **Output:** `-1`
- **Explanation:** `k` needs a low `1` bit that is `0` in `n`.
