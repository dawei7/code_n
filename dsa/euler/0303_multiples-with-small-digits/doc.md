## Description

For a positive integer $n$, define $f(n)$ as the least positive multiple of $n$ that, written in base $10$, uses only digits $\le 2$.

Thus $f(2)=2$, $f(3)=12$, $f(7)=21$, $f(42)=210$, $f(89)=1121222$.

Also, $\sum \limits_{n = 1}^{100} {\dfrac{f(n)}{n}} = 11363107$.

Find $\sum \limits_{n=1}^{10000} {\dfrac{f(n)}{n}}$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

