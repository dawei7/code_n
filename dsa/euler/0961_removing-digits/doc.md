## Description

This game starts with a positive integer. Two players take turns to remove a single digit from that integer. After the digit is removed any resulting leading zeros are removed.

For example, removing a digit from $105$ results in either $5$, $10$ or $15$.

The winner is the person who removes the last nonzero digit.

Define $W(N)$ to be how many positive integers less than $N$ for which the first player can guarantee a win given optimal play. You are given $W(100) = 18$ and $W(10^4) = 1656$.

Find $W(10^{18})$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

