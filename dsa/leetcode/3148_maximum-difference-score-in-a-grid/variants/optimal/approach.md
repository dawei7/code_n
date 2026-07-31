## General

Suppose a route starts at value `start`, visits intermediate values, and ends at value `end`. Consecutive score differences cancel:

$$
(v_1-\texttt{start})+(v_2-v_1)+\cdots+(\texttt{end}-v_t)
=\texttt{end}-\texttt{start}.
$$

The cells that can precede `(row, column)` are exactly the upper-left prefix rectangle ending there, except for the destination itself. Any cell in that rectangle can reach the destination using at most one downward and one rightward move. Consequently, the best route ending at the current cell subtracts the smallest value in that preceding region.

**Compress prefix minima to one row**

Scan rows from top to bottom and columns from left to right. Before processing a cell, `prefix_minimum[column]` is the minimum over all earlier rows and columns through `column`. `left_minimum` is the minimum in the current row's processed prefix, together with all cells above that prefix.

Their minimum is therefore the smallest valid predecessor of the current cell. Subtract it from the current value to update the answer. Then include the current value in the prefix minimum stored for this column and carry that result as `left_minimum` for the next column.

The first cell has no predecessor and cannot define a route, but both dimensions are at least two, so later cells always provide valid moves. For every destination, the scan considers its minimum reachable start, which maximizes the telescoped difference. Taking the maximum over all destinations proves the result is optimal.

## Complexity detail

Every one of the $mn$ cells is processed once with constant work, so the running time is $O(mn)$.

The prefix-minimum array has one entry per column and the remaining state is scalar, giving $O(n)$ auxiliary space. Iterating along the smaller dimension could reduce this to $O(\min(m,n))$, but the required bound remains linear in one matrix dimension.

## Alternatives and edge cases

- **Full prefix-minimum matrix:** Storing the minimum for every upper-left rectangle gives the same $O(mn)$ time but uses $O(mn)$ space.
- **Enumerate every predecessor:** For each destination, scanning its whole upper-left rectangle is correct but can require $O(m^2n^2)$ time; it is the principal slower benchmark comparison.
- **Four-direction extrema:** Treating arbitrary pairs as reachable is invalid because routes can never move upward or leftward.
- The best pair may occupy the same row or the same column; requiring both coordinates to change rejects valid moves.
- At least one move is required, so the current cell must not be inserted into its prefix minimum before its score is evaluated.
- If all reachable differences are negative, the least negative one is the answer; initializing the result to zero would incorrectly allow an empty route.
- Equal-valued reachable cells can produce the optimal score zero.
