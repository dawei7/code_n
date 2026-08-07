## Description

Given two integers `n` and `k`, return *the* $$k^{\text{th}}$$ *lexicographically smallest integer in the range* `[1, n]`.
### Function Contract

**Inputs**

- `n`: The inclusive upper bound of the positive integer range.
- `k`: The valid one-based lexicographic rank to select.

**Return value**

Return the integer occupying position `k` when the decimal representations of $1$ through `n` are ordered
lexicographically.

### Examples
#### Example 1

- **Input:** $n = 13, k = 2$
- **Output:** `10`
- **Explanation:** The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
#### Example 2

- **Input:** $n = 1, k = 1$
- **Output:** `1`
### Constraints

- $1 \le k \le n \le 10^{9}$