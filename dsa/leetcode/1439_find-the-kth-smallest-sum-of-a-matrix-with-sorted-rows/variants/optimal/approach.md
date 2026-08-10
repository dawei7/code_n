## General

**Merge one row of choices at a time**

Choosing one element from each row creates a sum. Instead of enumerating the full Cartesian product of all rows, the algorithm maintains only the smallest partial sums after each processed row.

`pre` is a sorted list containing up to the $k$ smallest sums obtainable by choosing one value from every row processed so far, with duplicates retained.

It begins as:

```python
pre = [0]
```

Before any rows are processed, there is exactly one empty choice with sum zero. Adding a value from the first row to this zero produces the one-row sums.

**Combine current partial sums with the next row**

For each row `cur`:

```python
pre = sorted(
    a + b
    for a in pre
    for b in cur[:k]
)[:k]
```

The nested generator forms every sum of one retained prior partial sum `a` and one considered current-row value `b`. Sorting places those new partial sums in nondecreasing order, and `[:k]` keeps only the first $k$.

Duplicates must remain. Different arrays of choices can have the same numeric sum, and the kth smallest is ranked with multiplicity. `sorted` returns a list rather than a set, so equal sums occupy separate positions.

**Why only the first `k` row values matter**

Every row is sorted. Consider a row value at position at least $k$. There are already $k$ row entries no larger than it. Pair each of those entries with the smallest value in `pre`. That creates $k$ combined sums no larger than pairing the later row value with any prior sum.

Therefore, a value beyond `cur[:k]` cannot change the numeric value of the first $k$ combined sums. It may tie them, but at least $k$ no-larger sums already exist, so the kth value remains unchanged.

When a row has fewer than $k$ columns, slicing simply returns the complete row.

**Why discarding prior sums after rank `k` is safe**

The same dominance argument works across iterations. Suppose a partial sum `a` was not retained because at least $k$ earlier partial sums are no larger. Pair those retained sums with the smallest value of every future row. They produce at least $k$ full sums no larger than any full sum extending `a` with the same minimum future choices.

Thus an omitted partial sum can never lower the kth final value. Keeping the top $k$ partial sums is sufficient induction state.

**Trace the first example**

For `mat = [[1,3,11],[2,4,6]]` and `k = 5`:

After the first row:

```text
pre = [1, 3, 11]
```

Combining with the second row generates:

```text
3, 5, 7
5, 7, 9
13, 15, 17
```

Sorting all nine values gives:

```text
[3, 5, 5, 7, 7, 9, 13, 15, 17]
```

The retained first five are `[3,5,5,7,7]`. Their final element is seven, the fifth smallest sum.

The duplicate five represents two distinct arrays, `[1,4]` and `[3,2]`. Retaining both is necessary for rank counting.

**Why `pre[-1]` is the answer**

After the final row, the problem guarantee says at least $k$ complete arrays exist. The truncation therefore leaves exactly $k$ sums. They are sorted, so index `-1` is the kth retained value.

At earlier stages, there may be fewer than $k$ combinations, and `pre` simply contains all of them. Later Cartesian products can grow the list until it reaches size $k$.

**Why the iterative invariant proves correctness**

The base `[0]` is the complete multiset of sums for zero rows. Assume `pre` contains the smallest up-to-$k$ partial sums for processed rows. Pairing with relevant current values generates every candidate capable of entering the next first $k$; the pruning arguments show omitted prior sums and later row values cannot affect that prefix.

Sorting and truncating therefore restores the invariant for one more row. After all rows, the invariant says `pre` contains the first $k$ full sums, so its last value is correct.

**Why positive values support pruning**

All matrix entries are positive. Future row additions preserve order between partial sums: if $a_1\le a_2$, then $a_1+c\le a_2+c$ for the same continuation $c$. This monotonicity underlies safely discarding larger partial sums.

## Complexity detail

Let $m$ be the number of rows, $n$ the columns per row, and $r=\min(n,k)$. After the first stages, `pre` has at most $k$ entries. For one row, the generator creates at most $kr$ sums. Materializing and sorting them costs $O(kr\log(kr))$ time. Across $m$ rows, the exact bound is:

$$
O\left(mkr\log(kr)\right).
$$

The sorted call materializes up to $kr$ integers before truncation, so peak auxiliary storage is $O(kr)$, plus the retained $O(k)$ list.

The manifest advertises $O(mn+mk\log k)$ time and $O(k)$ space. Those bounds require merging sorted sum lists with a min-heap and generating only the next $k$ pairs, instead of materializing every retained-prefix by row-value combination. The protected source uses full generator materialization and sorting, so the larger exact bounds apply.

## Alternatives and edge cases

- **Heap merge of two sorted sum lists:** Treat pair sums as a sorted grid and pop the next smallest while pushing neighbors. It produces only $k$ values and realizes the manifest's $O(k\log k)$-style merge.
- **Binary search on answer:** Count how many row-choice sums are at most a candidate threshold. Pruning can make it practical, but the counting recursion is more complex.
- **Enumerate every complete choice:** There can be $n^m$ arrays, which is infeasible.
- **Duplicate matrix values:** They represent distinct choices and must create duplicate sums; list sorting preserves them.
- **`k = 1`:** Only the minimum partial sum is retained, yielding the sum of every row's first value.
- **One row:** The result is that row's kth value, subject to the existence guarantee.
- **Fewer than `k` partial combinations early:** The algorithm keeps all of them and can expand on later rows.
- **Row longer than `k`:** Entries after the first `k` cannot affect the kth combined value.
- **Final existence guarantee:** It ensures `pre` has $k$ entries before `pre[-1]` is interpreted as the kth sum.
- **Sorted-row requirement:** The `cur[:k]` pruning argument relies on nondecreasing row order.
