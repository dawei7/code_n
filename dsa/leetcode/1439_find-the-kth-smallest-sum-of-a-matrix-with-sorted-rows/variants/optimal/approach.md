## General
**Represent processed rows by sorted partial sums.** Begin with `sums = [0]`. After processing some prefix of rows, keep the smallest at most `k` sums obtainable from that prefix, in non-decreasing order. Merging the next row means finding the smallest pair sums `sums[i] + row[j]`.

**Why only k partial sums are needed.** Suppose a partial sum ranks after the first `k`. At least `k` retained partial sums are no larger. Adding the same smallest possible choices from every future row to those retained sums produces at least `k` final sums no larger than any final sum descended from the discarded one. Therefore a discarded partial sum can never contribute to the final `k`th position.

**View one merge as sorted sequences.** For a fixed partial sum `sums[i]`, the sequence

$$
\texttt{sums[i]}+\texttt{row[0]},\;
\texttt{sums[i]}+\texttt{row[1]},\;\ldots
$$

is sorted because the matrix row is sorted. The complete pair-sum multiset is the merge of one such sequence for every retained partial sum.

**Generate the k smallest pair sums with a heap.** Insert the first pair from every sequence into a min-heap as `(sum, i, 0)`. Repeatedly remove the smallest entry and append its sum to the new list. If it came from column `j` and `j + 1 < n`, push the next pair `(sums[i] + row[j + 1], i, j + 1)`. Stop after `k` pops or when the heap empties.

**Why the heap order is exact.** At every step, the heap contains the smallest not-yet-emitted value from each pair-sum sequence. Any uninserted value lies later in its sequence and is no smaller than that sequence's heap representative. The global heap minimum is consequently the smallest remaining pair sum. Repeating the argument emits the merged multiset in sorted order, including duplicate sums from different choices.

**Carry the invariant across all rows.** Replace `sums` with the emitted list after each row. The truncation argument preserves every candidate relevant to final rank `k`, and the heap merge orders those candidates exactly. After the last row, `sums[k - 1]` is therefore the requested one-based value.

## Complexity detail
Reading the matrix accounts for $O(mn)$ input work. Each of the $m$ row merges keeps a heap and result list of at most $k$ entries, performs at most $k$ pops and pushes, and costs $O(k\log k)$ time. The total is $O(mn+mk\log k)$ time and $O(k)$ auxiliary space.

## Alternatives and edge cases
- **Materialize every cross product:** Combining every retained sum with every row value and sorting can take $O(mkn\log(kn))$ time and $O(kn)$ temporary space.
- **Enumerate all row choices:** The full Cartesian product has $n^m$ combinations and is infeasible.
- **Binary search the answer:** Count sums no greater than a candidate with pruned DFS; this can be effective but requires careful counting bounds and value-range searches.
- **Duplicate values or sums:** Keep every occurrence because rank counts choices with multiplicity.
- **One row:** The answer is simply `mat[0][k - 1]`.
- **First rank:** Choosing the first element from every sorted row gives the minimum sum.
- **Fewer than k intermediate combinations:** Retain all of them; the number of combinations grows as more rows are merged.
- **Heap seeding:** Seed one sequence per retained partial sum, not every pair, to preserve the $O(k)$ memory bound.
