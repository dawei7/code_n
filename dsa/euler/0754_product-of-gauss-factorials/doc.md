## Description

The Gauss Factorial of a number $n$ is defined as the product of all positive numbers $\leq n$ that are relatively prime to $n$. For example $g(10)=1\times 3\times 7\times 9 = 189$. 

Also we define

$$
\displaystyle G(n) = \prod_{i=1}^{n}g(i)
$$

You are given $G(10) = 23044331520000$.

Find $G(10^8)$. Give your answer modulo $1\,000\,000\,007$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

