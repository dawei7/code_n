## Description

Fermat's Last Theorem states that no three positive integers $a$, $b$, $c$ satisfy the equation 

$$
a^n+b^n=c^n
$$

for any integer value of $n$ greater than 2.

For this problem we are only considering the case $n=3$. For certain values of $p$, it is possible to solve the congruence equation:

$$
a^3+b^3 \equiv c^3 \pmod{p}
$$

For a prime $p$, we define $F(p)$ as the number of integer solutions to this equation for $1 \le a,b,c < p$.

You are given $F(5) = 12$ and $F(7) = 0$.

Find the sum of $F(p)$ over all primes $p$ less than $6\,000\,000$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

