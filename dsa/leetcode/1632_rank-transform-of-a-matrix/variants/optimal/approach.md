## General
**Process values from low to high.** Maintain the greatest rank already assigned in every row and every column. When handling value $x$, all strictly smaller values have finalized ranks, while no larger value has influenced the trackers. A cell `(r,c)` with value $x$ must therefore receive at least `1 + max(row_rank[r], column_rank[c])`.

**Unify equal cells before assigning ranks.** Equal cells sharing a row or column must have the same rank. For the current value, represent each involved row and column as a union-find node and union the row node with the column node for every cell. Connected components are exactly the transitive groups of equal cells constrained to share a rank.

**Assign a whole value batch atomically.** For each component, take one plus the maximum existing row or column rank over all its cells. Record every component rank before updating any tracker. This atomic step prevents one equal component from incorrectly influencing another disconnected component of the same value. Then write the answers and raise the affected row and column trackers.

Every assigned component rank exceeds all smaller values in each participating row and column, so all strict comparisons are respected. Equal connected cells are unified and receive one rank. Conversely, any valid assignment must exceed the same previously finalized tracker maximum, so the chosen rank is the smallest possible for that component. Induction over sorted values proves the complete matrix is the unique minimum assignment.

## Complexity detail
Grouping and sorting the $V$ cells by value takes $O(V\log V)$ time. Across all value batches, union-find, grouping, assignment, and tracker updates process $O(V)$ cells with near-constant amortized union-find cost. Total time is $O(V\log V)$. The value groups, temporary components, trackers, and answer use $O(V)$ space.

## Alternatives and edge cases
- **Component DAG:** Build equality components, add directed constraints from smaller to larger components within rows and columns, then compute longest-path ranks. This is correct but materializing and deduplicating the graph is more involved.
- **Repeatedly scan for the next value:** Avoiding the initial sort by linearly searching all unprocessed cells for each distinct value can take $O(V^2)$ time.
- **Rank equal cells independently:** This violates the equality rule when equal cells share a row or column, including through a transitive chain.
- Equal values in different rows and columns are not necessarily connected and can receive different ranks.
- All-equal matrices receive rank 1 everywhere.
- A value batch must be assigned before its row and column trackers are updated.
- Negative values and large magnitude do not affect the relative-order reasoning.
