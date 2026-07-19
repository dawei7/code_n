## General
**Canonicalize every board by collapsing it**

After each insertion, repeatedly remove all runs of length at least three until no further group disappears. Equivalent chain reactions therefore produce the same stable board state.

**Search by number of inserted balls**

Breadth-first states contain the stable board and the five remaining color counts. Each edge inserts one available ball and collapses the result. The first empty board is optimal because all states using `k` balls are processed before states using $k + 1$.

**Generate every useful insertion once**

An insertion is useful when it joins the same color or inserts a different color between an equal pair. The second form is an essential setup move for later cascades. An insertion with neither property creates an isolated ball and can be postponed until it becomes useful. Equivalent positions inside one same-color run are skipped.

**Deduplicate converging histories**

Different insertion orders can reach the same stable board with identical hand counts. A visited set retains only the shallowest occurrence. If the queue empties, no legal sequence can clear the row.

## Complexity detail
With initial board length $n$ and hand length $h$, there are at most $O((n + h)^h)$ conservatively bounded states. Generating and collapsing successors costs another $O(n + h)$ factor, yielding $O((n + h)^{h + 1})$ time and $O((n + h)^h)$ space.

## Alternatives and edge cases
- **Memoized depth-first search:** can return the minimum remaining cost from each complete state.
- **Search without a visited set:** is correct but repeats states reached by different insertion orders.
- **Complete existing runs only:** is incomplete because setup insertions between equal balls may be necessary.
- **Try every position and color:** is complete but creates many isolated and duplicate moves.
- **Immediate cascade:** always stabilize before choosing another insertion.
- **Insufficient hand:** exhausted states remain failures.
- **Empty board:** requires zero additional balls.
- **Duplicate hand colors:** counts make their order irrelevant.
