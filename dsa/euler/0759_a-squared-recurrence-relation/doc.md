## Description

The function $f$ is defined for all positive integers as follows:

$$
\begin{aligned}
f(1) &=  1\\
f(2n) &= 2f(n)\\
f(2n+1) &= 2n+1 + 2f(n)+\tfrac 1n f(n)
\end{aligned}
$$

It can be proven that $f(n)$ is integer for all values of $n$.

The function $S(n)$ is defined as $S(n) = \displaystyle \sum_{i=1}^n f(i) ^2$.

For example, $S(10)=1530$ and $S(10^2)=4798445$.

Find $S(10^{16})$. Give your answer modulo $1\,000\,000\,007$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

