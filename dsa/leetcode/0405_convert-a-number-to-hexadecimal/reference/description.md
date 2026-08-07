## Description

Given a 32-bit integer `num`, return *a string representing its hexadecimal representation*. For negative integers, <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">two’s complement</a> method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

**Note: **You are not allowed to use any built-in library method to directly solve this problem.
### Function Contract

**Inputs**

- `num`: A signed 32-bit integer.

**Return value**

Return the lowercase hexadecimal representation without unnecessary leading zeroes; negative inputs use their full 32-bit two's-complement bit pattern.

### Examples
#### Example 1

- **Input:** $num = 26$
- **Output:** `"1a"`
#### Example 2

- **Input:** $num = -1$
- **Output:** `"ffffffff"`
### Constraints

- $-2^{31} \le num \le 2^{31} - 1$