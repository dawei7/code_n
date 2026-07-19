# Super Pow

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 372 |
| Difficulty | Medium |
| Topics | Math, Divide and Conquer |
| Official Link | [LeetCode](https://leetcode.com/problems/super-pow/) |

## Problem Description
### Goal
Given a positive integer base `a` and a nonempty list of decimal digits `b`, let `B` be the positive exponent represented by those digits from most significant to least significant. The representation contains no leading zeroes, and `B` may be far too large for an ordinary integer type.

Return $a ^{B} \bmod 1337$. Process the exponent representation without constructing its full numerical value, reducing intermediate powers modulo `1337` to control size. Preserve ordinary modular behavior for bases larger than or divisible by the modulus, and return only the modular value rather than the enormous full power.

### Function Contract
**Inputs**

- `a`: an integer base
- `b`: a non-empty list of decimal digits representing the exponent from most significant to least significant

**Return value**

- $a ^{B} \bmod 1337$, where `B` is the integer represented by `b`.

### Examples
**Example 1**

- Input: `a = 2, b = [3]`
- Output: `8`

**Example 2**

- Input: `a = 2, b = [1,0]`
- Output: `1024`

**Example 3**

- Input: `a = 1, b = [4,3,3,8,5,2]`
- Output: `1`
