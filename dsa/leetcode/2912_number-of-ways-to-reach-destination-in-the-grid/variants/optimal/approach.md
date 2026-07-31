## General

**Only the destination's row and column matter.** Relative to `dest`, every
cell belongs to exactly one of four classes: the destination itself, another
cell in its row, another cell in its column, or a cell sharing neither
coordinate. Cells in the same class have identical transition counts, so the
grid never needs to be materialized even when $n$ and $m$ are enormous.

**Count transitions between the four classes.** Let the current aggregated
counts be `at_dest`, `same_row`, `same_col`, and `neither`. A route reaches the
destination next only from one of the latter two aligned classes. From the
destination there are $m-1$ choices into its row and $n-1$ into its column.
From a same-row cell, $m-2$ moves stay in that class and $n-1$ enter the
neither class; the same-column formula is symmetric. Finally, each neither
cell has one move into the destination row, one into its column, and
$n+m-4$ moves that remain neither. These counts give the simultaneous update

$$
\begin{aligned}
D' &= R+C,\\
R' &= (m-1)D+(m-2)R+X,\\
C' &= (n-1)D+(n-2)C+X,\\
X' &= (n-1)R+(m-1)C+(n+m-4)X.
\end{aligned}
$$

Initialize exactly one class according to `source`, apply the update $k$
times, and reduce every count modulo $10^9+7$. By induction, each state equals
the number of routes ending in its class after the processed number of moves:
the base state contains only the source, and every legal next cell is counted
once by the transition from its current class. Therefore `at_dest` after the
$k$th update is precisely the requested count.

## Complexity detail

Each of the $k$ updates performs a constant number of arithmetic operations,
so the running time is $O(k)$. Only four path counts are retained, giving
$O(1)$ auxiliary space. The bounds are independent of the potentially
billion-sized grid dimensions.

## Alternatives and edge cases

- **Dynamic programming over every cell:** Row and column totals can speed up each layer, but storing the full grid still costs $O(nm)$ space and $O(knm)$ time; destination-relative symmetry removes that factor entirely.
- **Four-by-four matrix exponentiation:** Exponentiating the fixed transition matrix can reduce the dependence on $k$ to $O(\log k)$, but the linear recurrence is simpler and comfortably fits the stated $k\le 10^5$ bound.
- **Source equals destination:** The initial destination count is one, but one move cannot stay there; exact-move semantics still require processing all $k$ transitions.
- **One aligned coordinate:** A source in the destination row or column has exactly one direct one-move route to it.
- **No aligned coordinate:** Reaching the destination requires at least two moves, through either the destination row or its column.
- **Smallest grid:** When $n=m=2$, coefficients such as $n-2$, $m-2$, and $n+m-4$ legitimately become zero.
- **Modulo arithmetic:** Reduce every new class count, since both the dimensions and the number of route sequences can be very large.
