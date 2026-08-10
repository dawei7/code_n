## General

**Count each row and keep the best pair**

The required output has two components:

- the row index;
- the number of ones in that row.

`ans = [0, 0]` stores the best pair found so far. It initially chooses row zero with count zero, which is valid even when every matrix entry is zero.

The loop visits rows in increasing index order. For each row, `sum(row)` gives its number of ones because entries are restricted to zero and one.

**Why summing a binary row counts ones**

Every zero contributes nothing and every one contributes one:

$$
\sum_{j=0}^{n-1}\texttt{row[j]}
=
|\{j:\texttt{row[j]}=1\}|.
$$

This equality depends on the binary-matrix guarantee. For arbitrary integers, a sum would not be a count.

Python evaluates `sum(row)` in one pass over that row without allocating a filtered list.

**Update only for a strict improvement**

The condition is:

`if ans[1] < cnt`.

When current count is greater, current row becomes the new best and `ans` changes to `[i, cnt]`.

When counts are equal, the condition is false. Because rows are visited from smallest index upward, the already stored row necessarily has a smaller index. Leaving it unchanged implements the required tie-break automatically.

Using `<=` instead would replace an earlier row on ties and incorrectly select the largest tied index.

**Trace a tie**

For `[[0,1],[1,0]]`:

- row zero has count one, greater than initialized zero, so answer becomes `[0,1]`;
- row one also has count one, but it is not strictly greater, so answer remains `[0,1]`.

This returns the earliest row among the maximum-count rows.

**Trace a later improvement**

For `[[0,0,0],[0,1,1]]`:

- row zero count is zero, so initialization remains `[0,0]`;
- row one count is two, a strict improvement, so answer becomes `[1,2]`.

No later comparison is needed after the loop ends because every row has been examined.

**All-zero matrix**

Every row's count is zero. No iteration satisfies `ans[1] < cnt`, and the result stays `[0,0]`.

That is correct: the maximum number of ones is zero, every row ties, and row zero is the smallest valid index.

This explains why initializing with row zero rather than a sentinel index such as `-1` is useful.

**Loop invariant**

Before processing row $i$, maintain:

> `ans[1]` is the maximum one-count among rows $0$ through $i-1$, and `ans[0]` is the smallest row index attaining that count.

Initially there is a small nuance: before row zero is processed, `[0,0]` already represents the correct eventual choice if row zero has zero ones. Since counts cannot be negative, it is a safe baseline.

For the current row:

- a larger count must replace the best;
- a smaller count cannot matter;
- an equal count must not replace the earlier index.

The update rule handles all three cases and preserves the invariant. After the final row, it proves the returned pair is correct.

**Why every cell must be read**

Without additional structure such as sorted rows, any unexamined cell could be a one that changes its row's count and possibly the winner.

The algorithm reads all $mn$ cells once. This matches the natural lower bound for arbitrary binary matrices.

**Input and output behavior**

`enumerate(mat)` supplies zero-based indices exactly as the contract expects. Rows are only read, and `sum` does not mutate them.

Whenever a new best is found, a new two-element list is assigned to `ans`. The final returned list is independent of the matrix storage.

**Why no separate tie comparison is needed**

An alternative implementation might compare candidate pairs by:

$$
(-\text{count},\text{index}).
$$

The ascending scan makes that machinery unnecessary. Encounter order already encodes the smallest-index preference, so strict count comparison is enough.

**Potential early exit**

A row cannot contain more than $n$ ones. If the algorithm ever finds count $n$, it has reached the maximum possible count and could return immediately because this is the first such row.

The exact solution does not use this optimization. It still remains linear and simpler.

## Complexity detail

For an $m\times n$ matrix, summing each of $m$ rows costs $O(n)$, for total time $O(mn)$.

The algorithm stores one count, one index, and a two-element result. Excluding the returned pair, auxiliary space is $O(1)$. The output itself is also constant size.

The input matrix is unchanged.

## Alternatives and edge cases

- **Count with nested loops:** Equivalent to `sum(row)` and useful if entries needed validation.
- **Compare tuples:** Store a key using negative count and index, but it adds abstraction without reducing work.
- **Early exit at `n` ones:** Safe because no row can do better and the first full-one row wins ties.
- **All rows tied:** Strict updates retain row zero.
- **All-zero matrix:** Returns `[0,0]`.
- **One row:** It is necessarily selected with its count.
- **One column:** The first row containing one wins; otherwise row zero.
- **Strict versus non-strict update:** Strict comparison is essential for the smallest-index tie-break.
- **Binary guarantee:** It is what makes row sum equal one-count.
- **Input preservation:** Rows are scanned but never changed.
