## General

Exactly $n-1$ moves take the first child from row 0 and column 0 to row $n-1$ and column $n-1$. Both coordinates must increase on every move, so this child has no choice: it visits every $(i,i)$ room on the main diagonal.

The top-right child must increase its row on every move. Before the destination, any useful room lies strictly above the diagonal. If it reaches $(i,i)$ early, every remaining move must be down-right, following rooms already collected by the first child. Because fruit counts are nonnegative, an optimal contribution can instead be represented by a path through columns greater than the current row until its final move. The bottom-left child is symmetric and stays strictly below the diagonal.

These two strict triangles are disjoint from each other and from the forced diagonal. Their best contributions can therefore be optimized independently without a joint three-child state.

For the upper triangle, let the rolling value at column $j$ be the greatest fruit total for a top-right path reaching the previous row at that column. A state $(i,j)$ receives transitions only from columns $j-1$, $j$, and $j+1$. Restrict states to $j>i$, add the current room's fruit, and keep only the previous and current rows. After processing row $n-2$, the only strict-triangle state that can enter the destination is column $n-1$.

Apply the transposed recurrence to the lower triangle: sweep columns, index the rolling array by row, and use predecessor rows $i-1$, $i$, and $i+1$. Add both dynamic-program totals to the diagonal sum. The destination itself appears only in the diagonal sum, so shared-room fruit is never double-counted.

## Complexity detail

Each strict triangle contains $\Theta(n^2)$ states, and every state examines at most three predecessors. Together with the diagonal scan, total time is $O(n^2)$.

Only two length-$n$ layers are needed for either triangular dynamic program. Reusing them sequentially gives $O(n)$ auxiliary space.

The benchmark defines `size` as the grid dimension $n$ and fills both triangles with nonzero, varying values. The reference performs constant work per state. A correct but slower dynamic program that scans all $n$ positions in the preceding layer before filtering for the three legal predecessors performs $\Theta(n^3)$ work.

## Alternatives and edge cases

- **Enumerate complete paths:** Each side child has up to three choices per move, causing exponential growth even though many paths reach the same state.
- **Scan an entire predecessor layer:** This preserves the recurrence but wastes $O(n)$ work per state and raises the total to $O(n^3)$.
- **Joint three-child dynamic programming:** It models collisions directly but is unnecessary once the forced diagonal and disjoint strict triangles are established.
- **Count the destination three times:** All children finish there, but its fruit must be included only once through the diagonal sum.
- **Touch the diagonal early:** A side child then has no way to create a new contribution beyond the diagonal; strict-triangle states capture an equally good or better nonnegative-fruit path.
- **Two-by-two grid:** Neither side dynamic program has an interior layer; the result is exactly the four corner rooms.
- **Zero-valued rooms:** They remain legal transitions and may be necessary to reach a later high-value room.
- **Direction changes:** A side path may move toward the diagonal and then away again, so a single greedy direction is not sufficient.
