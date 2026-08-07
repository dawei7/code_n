## Description

A positive integer is *magical* if it is divisible by either `a` or `b`.

Given the three integers `n`, `a`, and `b`, return the $$n^{\text{th}}$$magical number. Since the answer may be very large, **return it modulo **$10^{9} + 7$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $n = 1, a = 2, b = 3$
- **Output:** `2`
#### Example 2

- **Input:** $n = 4, a = 2, b = 3$
- **Output:** `6`
### Constraints

- $1 \le n \le 10^{9}$

- $2 \le a, b \le 4 * 10^{4}$