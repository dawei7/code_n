## Description

Let $g(n)$ be a sequence defined as follows:

$g(4) = 13$,

$g(n) = g(n-1) + \gcd(n, g(n-1))$ for $n \gt 4$.

The first few values are:

    $n$4567891011121314151617181920...
    $g(n)$1314161718272829303132333451545560...
    

You are given that $g(1\,000) = 2524$ and $g(1\,000\,000) = 2624152$.

Find $g(10^{15})$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

