## Description

Let $n$ be a positive integer. Consider nim positions where:

There are $n$ non-empty piles.
Each pile has size less than $2^n$.
No two piles have the same size.
Let $W(n)$ be the number of winning nim positions satisfying the above conditions (a position is winning if the first player has a winning strategy). For example, $W(1) = 1$, $W(2) = 6$, $W(3) = 168$, $W(5) = 19764360$ and $W(100) \bmod 1\,000\,000\,007 = 384777056$.

Find $W(10\,000\,000) \bmod 1\,000\,000\,007$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

