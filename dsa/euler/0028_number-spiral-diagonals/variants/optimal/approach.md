# Number Spiral Diagonals - Optimal Approach

## Algorithm Explanation

Consider an $N \times N$ clockwise number spiral ($N$ is odd):

Center element at $k = 1$ is $1$.

For each outer ring of odd side length $k = 3, 5, 7, \dots, N$:
- Top-Right corner: $k^2$
- Top-Left corner: $k^2 - (k - 1)$
- Bottom-Left corner: $k^2 - 2(k - 1)$
- Bottom-Right corner: $k^2 - 3(k - 1)$

Sum of all 4 corners for ring $k$:
$$\text{Corner Sum}(k) = 4k^2 - 6(k - 1)$$

Summing $\text{Corner Sum}(k)$ for $k \in \{3, 5, \dots, 1001\}$ plus $1$ for the center yields the exact answer in $\mathcal{O}(N)$ time.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1001$ ($500$ loop iterations).
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
