### 1. Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

- For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `num`, return *its complement*.

### 2. Function Contract

**Inputs**

- `num`: the positive integer to complement

**Return value**

- Return the integer represented by flipping every bit in the no-leading-zero binary representation of `num`.

Do not complement implicit leading zeroes or apply a fixed signed-integer width.

### 3. Examples

#### Example 1

- **Input:** $num = 5$
- **Output:** `2`
- **Explanation:** The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
#### Example 2

- **Input:** $num = 1$
- **Output:** `0`
- **Explanation:** The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

### 4. Constraints

- $1 \le num < 2^{31}$

### 5. Note

This question is the same as 1009: <a href="https://leetcode.com/problems/complement-of-base-10-integer/" target="_blank">https://leetcode.com/problems/complement-of-base-10-integer/</a>