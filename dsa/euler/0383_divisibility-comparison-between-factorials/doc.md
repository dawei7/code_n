## Description

Let $f_5(n)$ be the largest integer $x$ for which $5^x$ divides $n$.

For example, $f_5(625000) = 7$.

Let $T_5(n)$ be the number of integers $i$ which satisfy $f_5((2 \cdot i - 1)!) \lt 2 \cdot f_5(i!)$ and $1 \le i \le n$.

It can be verified that $T_5(10^3) = 68$ and $T_5(10^9) = 2408210$.

Find $T_5(10^{18})$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

