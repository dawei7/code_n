## General

**Convert the radius to a span.** Along either coordinate, a sensor reaches `k` cells before its position, its own coordinate, and `k` cells after it. Its maximum one-dimensional span is therefore $s=2k+1$. Partition the $n$ rows into $\lceil n/s\rceil$ consecutive bands and the $m$ columns into $\lceil m/s\rceil$ bands. Placing one sensor near the center of every row-band and column-band intersection covers that entire rectangular block, establishing an achievable product.

**Match the construction with a lower bound.** Select $\lceil n/s\rceil$ row coordinates separated by more than $2k$, and independently select $\lceil m/s\rceil$ such column coordinates. Their Cartesian product contains one witness cell per band intersection. A single sensor cannot cover two selected rows or two selected columns, so it covers at most one witness cell. Consequently, at least the product of the two ceiling counts is necessary. The construction meets that bound exactly.

Compute each ceiling with integer arithmetic and multiply the results.

## Complexity detail

The algorithm performs a fixed number of arithmetic operations, taking $O(1)$ time and $O(1)$ auxiliary space.

The benchmark sets `n = m = N`, fixes `k = 2`, and uses sizes 32, 128, and 512 for a 16x span. The accepted formula remains constant time. A correct constructive method that allocates a grid and explicitly marks every covered cell takes $O(N^2)$ time and space, so it must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Explicit coverage grid:** Placing the same optimal sensor pattern and marking its cells is correct, but wastes $O(nm)$ time and space.
- **Greedy uncovered-cell scan:** It can reproduce the band construction, but still visits the grid rather than using the closed form.
- **Zero radius:** The span is one, so every cell requires its own sensor and the answer is $nm$.
- **Radius larger than both dimensions:** Both ceiling counts are one, giving a single sensor.
- **Partial final band:** Ceiling division accounts for a boundary band shorter than $2k+1$.
- **Rectangular grid:** Row and column counts are independent; neither dimension should be replaced by the other.
