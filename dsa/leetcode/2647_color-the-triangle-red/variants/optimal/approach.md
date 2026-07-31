## General

Let $R$ be the currently red triangles, and let $e(R)$ count neighboring pairs whose two endpoints are red. Consider

$$
\Phi(R)=2\lvert R\rvert-e(R).
$$

When a white triangle with $d \ge 2$ red neighbors becomes red, $\Phi$ changes by $2-d \le 0$. The completed triangle has $n^2$ vertices. Its horizontal neighbor edges total $n(n-1)$, and its edges between consecutive rows total $n(n-1)/2$. Therefore

$$
\Phi(\text{all red})=2n^2-\frac{3n(n-1)}{2}=\frac{n(n+3)}{2}.
$$

An initial set of $k$ triangles has $\Phi \le 2k$. Since propagation cannot increase the potential, every successful set must satisfy

$$
k \ge \left\lceil\frac{n(n+3)}{4}\right\rceil.
$$

**Attaining the lower bound**

Build the answer from the bottom upward in repeating four-row bands. Within a band whose bottom row is $i$, select every odd column of row $i$, only column $2$ of row $i-1$, odd columns beginning at $3$ of row $i-2$, and only column $1$ of row $i-3$. At the top, the incomplete band is handled by the same modular pattern, with `(1, 1)` always selected.

The pattern alternates a dense row with a one-triangle row. Every gap in a dense row is surrounded by two selected or subsequently red side-neighbors; after those gaps fill, the adjacent sparse row can fill from its selected anchor, and this exposes the next row. Repeating that argument across each four-row band colors the whole triangle. Counting the selected coordinates gives exactly the lower bound above, so the construction is minimum.

The implementation expresses the band pattern through `offset = (n - row) % 4`. Offsets $0$ and $2$ emit alternating positions across the row, while offsets $1$ and $3$ emit one anchor.

## Complexity detail

The minimum output itself contains $\lceil n(n+3)/4\rceil=\Theta(n^2)$ coordinate pairs. Emitting each pair once takes $O(n^2)$ time and the returned list uses $O(n^2)$ space. Apart from the required output, only constant auxiliary state is used.

## Alternatives and edge cases

- **Explicit four-row loop:** Processing complete bands and then branching on `n % 4` is equivalent, but the modular row formula avoids a separate remainder table.
- **Search or propagation simulation:** Testing candidate seed sets or repeatedly simulating the coloring process is far more expensive and is unnecessary once the optimal pattern and potential bound are known.
- **Returning every boundary triangle:** This may propagate successfully, but it does not generally have minimum cardinality.
- The tip `(1, 1)` must be selected because it has only one neighbor and can never acquire two red neighbors later.
- Coordinate columns are 1-indexed and range through $2i-1$ in row $i$; parity determines triangle orientation and vertical adjacency.
- Multiple minimum coordinate sets can be valid, so judging must verify legality, cardinality, and propagation rather than require one exact ordering.
