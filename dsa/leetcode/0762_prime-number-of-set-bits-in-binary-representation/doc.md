# Prime Number of Set Bits in Binary Representation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 762 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) |

## Problem Description

### Goal

Given integers `left` and `right`, consider every integer in the inclusive range `[left, right]`. For each value, count the set bits—the `1` digits—in its binary representation.

Return how many range values have a prime number of set bits. Primality applies to the bit count rather than to the integer itself; counts such as `2`, `3`, and `5` qualify, while `0` and `1` are not prime. Both interval endpoints are included.

### Function Contract

**Inputs**

- `left`: the positive lower endpoint of the range.
- `right`: the upper endpoint, with `left <= right`.

**Return value**

- The number of values in `[left, right]` whose set-bit count is prime.

### Examples

**Example 1**

- Input: `left = 6`, `right = 10`
- Output: `4`
- Explanation: `6`, `7`, `9`, and `10` have respectively `2`, `3`, `2`, and `2` set bits.

**Example 2**

- Input: `left = 10`, `right = 15`
- Output: `5`
- Explanation: Every value except `15`, which has four set bits, qualifies.

**Example 3**

- Input: `left = 1`, `right = 1`
- Output: `0`
- Explanation: One set bit is not a prime count.
