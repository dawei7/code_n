# Find Kth Bit in Nth Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1545 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Recursion, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/) |

## Problem Description
### Goal
A sequence of binary strings is defined recursively. The first string is `S1 = "0"`. For every $i > 1$, form `Si` by concatenating `S(i - 1)`, one `"1"`, and the reverse of the bitwise inversion of `S(i - 1)`. Inversion changes every `"0"` to `"1"` and every `"1"` to `"0"`.

Given `n` and a one-indexed position `k`, return the `k`-th bit of `Sn`. The full string has length $2^n - 1$, but only the requested character is needed.

### Function Contract
**Inputs**

- `n`: the sequence level, where $1 \le n \le 20$.
- `k`: a one-indexed position satisfying $1 \le k \le 2^n - 1$.

**Return value**

The character `"0"` or `"1"` at position `k` in `Sn`.

### Examples
**Example 1**

- Input: `n = 3, k = 1`
- Output: `"0"`
- Explanation: `S3 = "0111001"`, whose first character is `"0"`.

**Example 2**

- Input: `n = 4, k = 11`
- Output: `"1"`
- Explanation: The eleventh character of `S4 = "011100110110001"` is `"1"`.

**Example 3**

- Input: `n = 1, k = 1`
- Output: `"0"`
- Explanation: The base string contains only that bit.
