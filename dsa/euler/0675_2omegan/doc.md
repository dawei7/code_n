## Description

Let $\omega(n)$ denote the number of distinct prime divisors of a positive integer $n$.

So  $\omega(1) = 0$ and  $\omega(360) = \omega(2^{3} \times 3^{2} \times 5) = 3$.

Let $S(n)$ be $ \sum_{d \mid n} 2^{\omega(d)}  $.

E.g. $S(6) = 2^{\omega(1)}+2^{\omega(2)}+2^{\omega(3)}+2^{\omega(6)} = 2^0+2^1+2^1+2^2 = 9$.

Let $F(n)=\sum_{i=2}^n S(i!)$.
$F(10)=4821.$

Find $F(10\,000\,000)$. Give your answer modulo  $1\,000\,000\,087$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

