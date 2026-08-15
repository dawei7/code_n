### 1. Description

You are given a **positive** integer `n`.

Let `s` be the **binary representation** of `n` without leading zeros.

The **reverse** of a binary string `s` is obtained by writing the characters of `s` in the opposite order.

You may flip any bit in `s` (change `0 → 1` or `1 → 0`). Each flip affects **exactly** one bit.

Return the **minimum** number of flips required to make `s` equal to the reverse of its original form.

### 2. Function Contract

**Inputs**

- `n`: The positive integer whose binary representation supplies both the starting string and the reversed target.

Let $B$ be the number of bits in the representation of `n`. The representation has no leading zeros, and flipping a bit does not insert, delete, or move any position.

**Return value**

Return the fewest single-position flips that make the original $B$-character binary string equal to its $B$-character reversal.

### 3. Examples

#### Example 1

- **Input:** n = 7

- **Output:** 0

- **Explanation:** The binary representation of 7 is `"111"`. Its reverse is also `"111"`, which is the same. Hence, no flips are needed.

#### Example 2

- **Input:** n = 10

- **Output:** 4

- **Explanation:** The binary representation of 10 is `"1010"`. Its reverse is `"0101"`. All four bits must be flipped to make them equal. Thus, the minimum number of flips required is 4.

### 4. Constraints

- $1 \le n \le 10^{9}$
