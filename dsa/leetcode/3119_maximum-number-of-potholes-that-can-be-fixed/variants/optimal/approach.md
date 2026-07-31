## General

**Each pothole block offers one efficient operation.** Split `road` at smooth positions and record the lengths of its maximal `x` blocks. If $k>0$ potholes are repaired from one block, doing so in one operation costs $k+1$. Splitting those same repairs across several operations only adds overhead, so an optimal plan uses at most one operation per block. That operation may repair the entire block or any consecutive part of it.

**Pay overhead on the largest capacities first.** Every used block costs one budget unit beyond the number of potholes repaired. Suppose a plan repairs potholes in a shorter block while a longer block is unused or not yet filled. Move those repairs into the longer block. The number repaired and total price do not increase; if this empties the shorter operation, the plan even saves its overhead. Repeating this exchange produces an equally good or cheaper plan that fills blocks in nonincreasing length order, with at most the last selected block only partially repaired.

Sort the block lengths descending. For each block, one budget unit is reserved for its operation, so at most `budget - 1` potholes can be taken. Repair the smaller of that amount and the block length, subtract the repair count plus its one-unit overhead, and continue only while at least two budget units remain. The exchange argument proves that no different choice of blocks can repair more potholes for the same budget, while the partial final operation uses every remaining unit that can contribute to the answer.

## Complexity detail

Let $n$ be the length of `road` and $r$ the number of maximal pothole blocks. Splitting and measuring the blocks takes $O(n)$ time. Sorting their lengths costs $O(r\log r)$, and the greedy scan costs $O(r)$, for total time $O(n+r\log r)$. The length list occupies $O(r)$ auxiliary space.

## Alternatives and edge cases

- **Budget dynamic programming:** Treat each block as choices from zero through its length. This is correct but can require pseudo-polynomial time in `budget`, approaching $O(r\cdot\texttt{budget})$ even when every block has length one.
- **Road-order greedy:** Repairing blocks from left to right can waste an overhead unit on a short block while a longer block could absorb the same repairs in one operation.
- **Repair every block partially:** Spreading repairs across more blocks pays more one-unit overheads and can never improve the count.
- **Counting sort by run length:** Since the run lengths sum to at most $n$, buckets can avoid comparison sorting and achieve $O(n)$ time with $O(n)$ space; sorting the at most $r$ lengths is simpler and meets the required bound.
- **No potholes:** The run list is empty and the answer is zero regardless of budget.
- **Budget one:** No operation can repair even one pothole because its minimum price is two.
- **Partial block:** Repairing fewer than all potholes in a run is allowed; the final selected run may consume exactly the remaining `budget - 1` units.
- **Excess budget:** Once every run is repaired, unused budget does not affect the answer.
- **Equal lengths:** Their relative order is irrelevant because they offer identical capacity for the same overhead.
