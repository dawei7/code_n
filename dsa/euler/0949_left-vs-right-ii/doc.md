## Description

Left and Right play a game with a number of words, each consisting of L's and R's, alternating turns. On Left's turn, for each word, Left can remove any number of letters (possibly zero), but not all the letters, from the left side of the word. However, at least one letter must be removed from at least one word. Right does the same on Right's turn except that Right removes letters from the right side of each word. The game continues until each word is reduced to a single letter. If there are more L's than R's remaining then Left wins; otherwise if there are more R's than L's then Right wins. In this problem we only consider games with an odd number of words, thus making ties impossible.

Let $G(n, k)$ be the number of ways of choosing $k$ words of length $n$, for which Right has a winning strategy when Left plays first. Different orderings of the same set of words are to be counted separately.

It can be seen that $G(2, 3) = 14$ due to the following solutions (and their reorderings):

- $(\text{LL}, \text{RR}, \text{RR}) : 3 \text{ orderings}$
- $(\text{LR}, \text{LR}, \text{LR}) : 1 \text{ ordering}$
- $(\text{LR}, \text{LR}, \text{RR}) : 3 \text{ orderings}$
- $(\text{LR}, \text{RR}, \text{RR}) : 3 \text{ orderings}$
- $(\text{RL}, \text{RR}, \text{RR}) : 3 \text{ orderings}$
- $(\text{RR}, \text{RR}, \text{RR}) : 1 \text{ ordering}$

You are also given $G(4, 3) = 496$ and $G(8, 5) = 26359197010$.

Find $G(20, 7)$ giving your answer modulo $1001001011$.


## Function Contract

- `solve() -> int`


## Examples

- Illustrative small inputs that demonstrate problem rules without spoiling the final target solution.


## Constraints

- Execution time MUST be strictly under 1 minute.

