# Complex Number Multiplication

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 537 |
| Difficulty | Medium |
| Topics | Math, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/complex-number-multiplication/) |

## Problem Description
### Goal
Given two complex numbers encoded as strings `real+imaginaryi`, parse each signed integer real part and signed integer imaginary coefficient. The separator remains a literal plus sign even when the imaginary coefficient is negative, as in `1+-1i`.

Multiply the numbers using $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$. Return the product in the same `real+imaginaryi` string format with decimal integer components and a trailing `i`. Do not return a floating-point approximation, omit a zero component, or replace the required separator format.

### Function Contract
**Inputs**

- `num1`, `num2`: complex-number strings whose real and imaginary integer components are each between `-100` and `100`

**Return value**

- The exact complex product formatted as `real+imaginaryi`, including `+-` when the imaginary result is negative

### Examples
**Example 1**

- Input: `num1 = "1+1i", num2 = "1+1i"`
- Output: `"0+2i"`

**Example 2**

- Input: `num1 = "1+-1i", num2 = "1+-1i"`
- Output: `"0+-2i"`

**Example 3**

- Input: `num1 = "100+100i", num2 = "100+-100i"`
- Output: `"20000+0i"`
