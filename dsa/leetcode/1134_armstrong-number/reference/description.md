## Description

Given an integer `n`, return `true` *if and only if it is an **Armstrong number***.

The `k`-digit number `n` is an Armstrong number if and only if the $$k^{\text{th}}$$ power of each digit sums to `n`.
### Function Contract

**Inputs**

- `n`: a positive integer. Let $k$ be the number of digits in its ordinary decimal representation, and let those digits be $d_1, d_2, \ldots, d_k$.

The Armstrong sum is

$\sum_{i=1}^{k} d_i^k.$

**Return value**

- `true` exactly when the Armstrong sum equals `n`; otherwise, `false`.

Repeated digits contribute separately, and a zero digit contributes $0^k = 0$.

### Examples

#### Example 1

- **Input:** $n = 153$
- **Output:** `true`
- **Explanation:** 153 is a 3-digit number, and 153 = $1^{3}$ + $5^{3}$ + $3^{3}$.
#### Example 2

- **Input:** $n = 123$
- **Output:** `false`
- **Explanation:** 123 is a 3-digit number, and 123 != $1^{3}$ + $2^{3}$ + $3^{3}$ = 36.
### Constraints

- $1 \le n \le 10^{8}$