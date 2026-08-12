# Lattice Paths - Optimal Approach

## Algorithm Explanation

In an $N \times N$ grid, any valid path from top-left to bottom-right moving only right ($R$) and down ($D$) consists of exactly $N$ right moves and $N$ down moves, for a total of $2N$ moves.

The problem reduces to choosing which $N$ of the $2N$ steps are right moves ($R$):
$$\binom{2N}{N} = \frac{(2N)!}{N! N!}$$

For $N = 20$:
$$\binom{40}{20} = \frac{40!}{20! 20!}$$

Using Python's `math.comb(40, 20)`, the result is computed instantaneously.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ - Computing combinatorial product.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
