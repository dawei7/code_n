## Description

Given an integer `n`, return the $$n^{\text{th}}$$ digit of the infinite integer sequence `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]`.
### Function Contract

**Inputs**

- `n`: A positive one-based position in the concatenated decimal sequence.

**Return value**

Return the decimal digit occupying position `n` as an integer from `0` through `9`.

### Examples

#### Example 1

- **Input:** $n = 3$
- **Output:** `3`
#### Example 2

- **Input:** $n = 11$
- **Output:** `0`
- **Explanation:** The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
### Constraints

- $1 \le n \le 2^{31} - 1$