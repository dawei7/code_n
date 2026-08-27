## Description

Let $p(n)$ be the number of ways to write $n$ as the sum of powers of two, ignoring order.

For example, $p(7) = 6$, the partitions being

$$
\begin{aligned}
7 &= 1+1+1+1+1+1+1 \\
&=1+1+1+1+1+2 \\
&=1+1+1+2+2 \\
&=1+1+1+4 \\
&=1+2+2+2 \\
&=1+2+4
\end{aligned}
$$

You are also given $p(7^7) \equiv 144548435 \pmod {10^9+7}$.

Find $p(7^{777})$. Give your answer modulo $10^9 + 7$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

