## Description

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

$$
\begin{aligned}
&44 \to 32 \to 13 \to 10 \to \mathbf 1 \to \mathbf 1\\
&85 \to \mathbf{89} \to 145 \to 42 \to 20 \to 4 \to 16 \to 37 \to 58 \to \mathbf{89}
\end{aligned}
$$

Therefore any chain that arrives at $1$ or $89$ will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at $1$ or $89$.

How many starting numbers below ten million will arrive at $89$?


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

