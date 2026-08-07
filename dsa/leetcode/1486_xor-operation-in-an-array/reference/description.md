## Description

You are given an integer `n` and an integer `start`.

Define an array `nums` where $\text{nums}[i] = start + 2 * i$ (**0-indexed**) and $n = \text{nums.length}$.

Return *the bitwise XOR of all elements of* `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $n = 5, start = 0$
- **Output:** `8`
- **Explanation:** Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
#### Example 2

- **Input:** $n = 4, start = 3$
- **Output:** `8`
- **Explanation:** Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
### Constraints

- $1 \le n \le 1000$

- $0 \le start \le 1000$

- $n = \text{nums.length}$