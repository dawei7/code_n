# Add Binary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 67 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Bit Manipulation, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/add-binary/) |

## Problem Description
### Goal
You are given two nonempty strings `a` and `b` representing nonnegative binary integers. Each contains only `0` and `1` and has no leading zero unless it is exactly `"0"`; either value may exceed fixed-width integer capacity.

Add the two represented values and return their sum as a canonical binary string. Process binary carries without depending on whole-string numeric conversion. The result uses no leading zeroes, and adding two zero strings returns the single character `"0"`.

### Function Contract
**Inputs**

- `a`: the first binary string
- `b`: the second binary string

**Return value**

The binary representation of their sum.

### Examples
**Example 1**

- Input: `a = "11", b = "1"`
- Output: `"100"`

**Example 2**

- Input: `a = "1010", b = "1011"`
- Output: `"10101"`

**Example 3**

- Input: `a = "0", b = "0"`
- Output: `"0"`
