# Number of Steps to Reduce a Number in Binary Representation to One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1404 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Bit Manipulation, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/) |

## Problem Description

### Goal

A positive integer is provided as a binary string `s` with no leading zeroes. Repeatedly change the represented number until it becomes one.

When the current number is even, divide it by two. When it is odd and greater than one, add one. Each division or addition counts as one step. Return the number of steps required to reach one. The binary input may be much longer than a machine integer.

### Function Contract

**Inputs**

- `s`: a binary representation of length $n$, where $1 \le n \le 500$, `s[0] == "1"`, and no leading zeroes occur.

**Return value**

- The number of prescribed even divisions and odd increments needed to reduce the represented value to one.

### Examples

**Example 1**

- Input: `s = "1101"`
- Output: `6`

**Example 2**

- Input: `s = "10"`
- Output: `1`

**Example 3**

- Input: `s = "1"`
- Output: `0`
