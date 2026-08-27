## Description

Given is the function $f(x) = \lfloor 2^{30.403243784 - x^2}\rfloor \times 10^{-9}$ ($\lfloor \, \rfloor$ is the floor-function),

the sequence $u_n$ is defined by $u_0 = -1$ and $u_{n + 1} = f(u_n)$.

Find $u_n + u_{n + 1}$ for $n = 10^{12}$.

Give your answer with $9$ digits after the decimal point.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

