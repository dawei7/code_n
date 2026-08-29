## General

**Each row is consumed from largest to smallest**

In every operation, one greatest remaining value is removed from each row. Therefore, the sequence of values removed from a particular row is simply that row's values in nonincreasing order.

If a row is sorted in nondecreasing order, its removal sequence is the sorted row read from right to left. Since all rows have the same number of columns, the values removed in one round occupy the same sorted column across every row.

The answer for that round is the maximum among those aligned values.

**Sort rows to align equal-numbered removals**

The solution sorts every `row` in place. Suppose a row becomes

$$
r_0\le r_1\le\cdots\le r_{n-1}.
$$

The first deletion removes $r_{n-1}$, the second removes $r_{n-2}$, and the final deletion removes $r_0$.

After every row is sorted this way, a column contains values with the same rank inside their respective rows. The last column contains every row maximum, the next-to-last contains every row's second-largest value, and so forth.

Thus the contribution of operational round $t$ is the maximum of one aligned sorted column.

**Why iterating columns in ascending order is still correct**

`zip(*grid)` produces columns from left to right: first all row minima, then the next values, and finally all row maxima. The physical deletion process handles those columns in the reverse order.

However, the final answer is a sum. Reversing the order of the round contributions does not change their sum. Therefore, it is valid to process sorted columns from smallest rank to largest rank even though deletion happens from largest to smallest.

The generator computes `max(col)` for every transposed column and `sum` adds those maxima.

**Trace the first example**

Sorting the rows of

`[[1,2,4],[3,3,1]]`

gives

`[[1,2,4],[1,3,3]]`.

The aligned columns are:

- `(1,1)`, whose maximum is 1;
- `(2,3)`, whose maximum is 3;
- `(4,3)`, whose maximum is 4.

Their sum is $1+3+4=8$.

Read in reverse, these are exactly the operation contributions 4, 3, and 1 described by the problem.

**Duplicate greatest values need no special handling**

When a row contains several equal maximum values, the rule permits deleting any one of them. Sorting places equal values next to each other. Removing one copy now and another in a later round produces the same ranked sequence regardless of which identical occurrence was notionally removed first.

Since only values matter and not original cell identities, sorting loses no relevant information.

**Why aligned ranks are enough**

Take any round number counted from the end. Every row has had the same number of elements deleted because each operation removes exactly one per row. Its greatest remaining value is therefore the element with the corresponding rank in its original sorted row.

The algorithm's column at that rank contains exactly those row-specific values. Taking its maximum implements the instruction to add the maximum among values deleted in that round.

This correspondence holds for every one of the `n` rounds. Summing all aligned-column maxima consequently equals the full operational answer.

**Understand `zip(*grid)`**

The star operator passes each row as a separate argument to `zip`. Because every row has length `n`, `zip` yields exactly `n` tuples, each containing one value from every row at the same column index.

There is no truncation concern under the rectangular-matrix contract. The tuples are consumed lazily by the generator expression.

**Input mutation**

`row.sort()` changes the order of values inside every input row. The challenge only asks for the numeric answer, so this is acceptable. If the caller needed the original matrix afterward, the implementation would need to sort copies instead.

All values are positive, although the rank-alignment argument would also work for arbitrary comparable integers.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Sorting one row takes $O(n\log n)$ time, so all row sorts cost $O(mn\log n)$. Transposing lazily and taking maxima examines all $mn$ values once, adding $O(mn)$. Sorting dominates.

Python's Timsort may use $O(n)$ temporary storage for one row in the worst case. A tuple emitted by `zip` contains $m$ references. Since columns are consumed one at a time, peak auxiliary space is $O(n+m)$ in the exact implementation, not necessarily the manifest's language-independent $O(\log n)$ sort-stack claim.

The matrix itself is reused and mutated; no full transposed matrix is materialized.

## Alternatives and edge cases

- **Repeated row maxima:** Simulate each round with `max` and deletion. It is simpler conceptually but can cost $O(mn^2)$.
- **Max-heaps per row:** Heapify negated values and pop once per round for $O(mn\log n)$ time with extra storage.
- **Single row:** Each round contributes its one deleted value, so the answer is the row sum.
- **Single column:** One round removes every entry and contributes the column maximum.
- **Duplicate values:** Their identities are irrelevant; sorting preserves the required multiset of removal values.
- **Ascending column iteration:** It reverses round order only, not the final sum.
- **Rectangular guarantee:** All rows have equal length, so `zip` yields every rank.
- **Positive values:** The result is positive, but no special initialization is needed because `max` sees a non-empty column.
- **Mutation:** Sorting occurs directly inside `grid`.
- **No explicit deletion:** Rank alignment simulates all rounds without shrinking rows.
