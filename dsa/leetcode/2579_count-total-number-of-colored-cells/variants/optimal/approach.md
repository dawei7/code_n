## General

The blue region is determined only by Manhattan distance from the first cell. After minute $n$, a cell is colored exactly when its Manhattan distance from the center is at most $n-1$.

**Counting one new layer:** For every positive distance $k$, the boundary $lvert x \rvert + \lvert y \rvert = k$ contains $4k$ cells. There are $k+1$ points from `(0, k)` to `(k, 0)` in one quadrant boundary, but accounting for the four axes only once gives the standard diamond perimeter count $4k$.

The first minute contributes the center cell. Minutes $2$ through $n$ add the layers for distances $1$ through $n-1$, so the total is

$$
1 + \sum_{k=1}^{n-1} 4k
= 1 + 4\frac{(n-1)n}{2}
= 1 + 2n(n-1).
$$

Every layer is disjoint, and together these layers contain precisely all cells whose Manhattan distance is at most $n-1$. Evaluating the derived formula therefore returns the exact colored-cell count.

## Complexity detail

The closed form uses a constant number of arithmetic operations, so it takes $O(1)$ time and $O(1)$ space. The maximum answer exceeds a signed 32-bit integer, so fixed-width implementations must perform the multiplication in 64-bit arithmetic.

## Alternatives and edge cases

- **Minute-by-minute accumulation:** Adding `4 * layer` for every layer is correct and easy to derive, but it takes $O(n)$ time instead of evaluating the arithmetic series directly.
- **Grid simulation:** Storing colored coordinates and expanding the frontier reproduces the process but requires $\Theta(n^2)$ cells and unnecessary set operations.
- **First minute:** At `n = 1`, the summation is empty and the formula correctly returns only the center cell.
- **Maximum input:** At `n = 100000`, the result is `19999800001`, which requires 64-bit arithmetic in languages with fixed-width integers.
