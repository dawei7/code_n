## Description

$2^7=128$ is the first power of two whose leading digits are "12".

The next power of two whose leading digits are "12" is $2^{80}$.

Define $p(L, n)$ to be the $n$th-smallest value of $j$ such that the base 10 representation of $2^j$ begins with the digits of $L$.

So $p(12, 1) = 7$ and $p(12, 2) = 80$.

You are also given that $p(123, 45) = 12710$.

Find $p(123, 678910)$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

