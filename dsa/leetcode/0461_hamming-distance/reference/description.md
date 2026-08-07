### 1. Description

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, return *the **Hamming distance** between them*.

### 2. Function Contract

**Inputs**

- `x`: A nonnegative integer.
- `y`: A nonnegative integer.

**Return value**

- Return the number of corresponding binary positions where `x` and `y` have different bits.

### 3. Examples

#### Example 1

- **Input:** $x = 1, y = 4$
- **Output:** `2`
- **Explanation:**
1   (0 0 0 1)
4   (0 1 0 0)
↑   ↑
The above arrows point to positions where the corresponding bits are different.
#### Example 2

- **Input:** $x = 3, y = 1$
- **Output:** `1`

### 4. Constraints

- $0 \le x, y \le 2^{31} - 1$

### 5. Note

This question is the same as <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/" target="_blank"> 2220: Minimum Bit Flips to Convert Number.</a>