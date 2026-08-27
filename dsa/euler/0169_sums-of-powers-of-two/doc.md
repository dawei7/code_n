## Description

Define $f(0)=1$ and $f(n)$ to be the number of different ways $n$ can be expressed as a sum of integer powers of $2$ using each power no more than twice.

For example, $f(10)=5$ since there are five different ways to express $10$:

$$
\begin{aligned}
& 1 + 1 + 8\\
& 1 + 1 + 4 + 4\\
& 1 + 1 + 2 + 2 + 4\\
& 2 + 4 + 4\\
& 2 + 8
\end{aligned}
$$

What is $f(10^{25})$?


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

