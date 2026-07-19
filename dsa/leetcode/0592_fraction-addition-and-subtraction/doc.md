# Fraction Addition and Subtraction

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 592 |
| Difficulty | Medium |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/fraction-addition-and-subtraction/) |

## Problem Description
### Goal
Given a string `expression` representing fraction addition and subtraction, evaluate all of its terms exactly. Each term is a signed or unsigned fraction, and the operators between consecutive terms are `+` or `-`; calculations must preserve rational values rather than use an inexact decimal approximation.

Return the calculation result as a string containing one irreducible fraction. Keep the denominator positive and reduce the numerator and denominator by their greatest common divisor. If the result is an integer, it must still use fraction format with denominator `1`, such as `2/1`; a positive result does not include a leading plus sign.

### Function Contract
**Inputs**

- `expression: str`: consecutive fraction terms of the form `numerator / denominator`, separated by `+` or `-`

**Return value**

- A string `"numerator/denominator"` representing the exact reduced result
- The denominator must be positive
- An integer result still uses denominator `1`

### Examples
**Example 1**

- Input: `expression = "-1/2+1/2"`
- Output: `"0/1"`

**Example 2**

- Input: `expression = "-1/2+1/2+1/3"`
- Output: `"1/3"`

**Example 3**

- Input: `expression = "1/3-1/2"`
- Output: `"-1/6"`
