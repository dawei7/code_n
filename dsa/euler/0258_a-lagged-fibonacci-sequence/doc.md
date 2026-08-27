## Description

A sequence is defined as:

$g_k = 1$, for $0 \le k \le 1999$
$g_k = g_{k-2000} + g_{k - 1999}$, for $k \ge 2000$.
Find $g_k \bmod 20092010$ for $k = 10^{18}$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

