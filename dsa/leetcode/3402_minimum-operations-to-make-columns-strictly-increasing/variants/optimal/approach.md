## General

**Columns are independent.** Incrementing one cell affects only its own column's ordering. The total minimum is the sum of independent minimum costs for each column.

`zip(*grid)` iterates the matrix by columns, producing a tuple of top-to-bottom values for each.

**Track the adjusted predecessor, not the original one.** `pre` is the value assigned to the previous row after all required increments. It begins at negative one. Because original values are nonnegative, the first cell always exceeds it and can remain unchanged.

**Keep a cell when it is already large enough.** If `pre < cur`, strict increase holds and the cheapest action is no action. Increasing `cur` would only add cost and make the next row's requirement harder. The source sets `pre=cur`.

**Otherwise raise it to the smallest legal value.** If `cur <= pre`, the current adjusted value must be at least `pre+1`. Since operations only increment, choosing exactly that value is feasible and cheapest.

The source performs `pre += 1` and adds `pre-cur` operations.

**Why local smallest choices are globally optimal.** Any valid solution must assign current cell a value greater than adjusted predecessor. When original value is too small, `pre+1` is a lower bound. Choosing anything larger costs more now and cannot help later, because later cells must exceed an even larger predecessor. Therefore the greedy minimum at each row is part of a global optimum.

This argument can be stated inductively. After processing each prefix of a column, `pre` is the smallest possible final value of its last cell among all minimum-cost adjustments of that prefix. The next rule preserves that property by taking `max(cur,pre+1)`.

**Trace a decreasing column.** For `[3,1,3,0]`, adjusted values become 3, 4, 5, 6. Costs are zero, three, two, and six, totaling eleven. Each forced value is one above the previous adjusted value.

**Why original predecessor is insufficient.** At third row above, original second value is one, but it was raised to four. Comparing third value three only with original one would incorrectly leave it unchanged and violate the adjusted column. `pre` must carry modifications forward.

**No grid mutation is needed.** The method stores only each adjusted predecessor and total operations. Future decisions require the adjusted value, not a rewritten matrix, so original `grid` remains unchanged.

**Write the update as one formula.** The chosen adjusted value for current cell is

$$
\max(\texttt{cur},\texttt{pre}+1).
$$

The source expresses this with a branch to avoid adding zero cost explicitly. When adjustment is needed, cost is chosen value minus original value, exactly the number of unit increments.

**Why no decrement or cross-column tradeoff exists.** A large value cannot be lowered to help cells beneath it, so it becomes an unavoidable predecessor bound. Spending extra operations in another column cannot compensate because strictness constraints never compare different columns.

**Trace an already-high later value.** If adjusted predecessor is four and next original cell is ten, keeping ten costs zero. Greedy does not force consecutive values; it requires only strict increase. The following cell must then exceed ten, not five, because ten is the actual retained predecessor.

**Why `pre=-1` is safe.** Nonnegative constraint guarantees first `cur>=0>-1`. If negative inputs were allowed, a true negative-infinity sentinel or special first-row handling would be needed.

**Combine column totals.** Since operations on different cells add and columns share no ordering constraints, summing every greedy column cost gives the matrix-wide minimum.

## Complexity detail

For $m$ rows and $n$ columns, every cell is processed once, giving $O(mn)$ time.

Algorithmic scalar state is $O(1)$ beyond the iterator. In Python, each tuple yielded by `zip(*grid)` contains $m$ references, so strict peak temporary space is $O(m)$, not literally $O(1)$. The manifest uses the conventional view that column iteration is streaming and excludes this language-level tuple.

## Alternatives and edge cases

- **Mutate the grid:** Raise each cell in place; it gives the same cost but changes input unnecessarily.
- **Process rows first:** Column predecessors still require separate state per column, using $O(n)$ memory.
- **Single row:** Every column is already strictly increasing vacuously, so cost zero.
- **Single column:** The method becomes the basic one-dimensional greedy.
- **Equal consecutive values:** Lower one is kept, later one rises by one.
- **Large natural jump:** It is retained at zero cost; adjusted values need not be consecutive.
- **Strictly increasing column:** It costs zero.
- **Strongly decreasing column:** Adjustments accumulate through `pre`.
- **Zero values:** Initial zero stays unchanged; later zeros may need increases.
- **Large accumulated result:** Python integers avoid overflow.
- **Nonnegative guarantee:** It justifies sentinel negative one.
- **Column independence:** Costs can be summed without coordination.
- **No decrement operation:** A high predecessor is an unavoidable constraint.
- **Unit-cost accounting:** Raising by `d` requires exactly `d` operations.
- **Input preservation:** `zip` reads rows and no assignment touches `grid`.
- **Strict space accounting:** Column tuples use $O(m)$ transient references.
- **Annotation import:** `List` must be available.
