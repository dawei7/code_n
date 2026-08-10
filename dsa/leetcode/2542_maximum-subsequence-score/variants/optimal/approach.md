## General

**Treat each selected `nums2` value as a candidate minimum**

The score is:

$$
\left(\sum \text{selected }\texttt{nums1}\right)
\cdot
\min(\text{selected }\texttt{nums2}).
$$

If a particular chosen index supplies the minimum multiplier `a`, every other chosen index must have `nums2>=a`. Among those eligible indices, maximize the `nums1` sum.

Sorting paired values by `nums2` descending lets the scan consider candidate minima from large to small while all eligible larger multipliers are already available.

**Preserve index pairing while sorting**

`zip(nums2,nums1)` creates pairs `(a,b)` from the same original index. Sorting these pairs in reverse order arranges larger `nums2` first.

The arrays need not be mutated, and their index relationship is preserved inside each tuple.

For equal `nums2`, reverse tuple ordering places larger `nums1` first. Tie order does not change correctness because the same multiplier applies across that tied group.

**Interpret the current scan item**

At pair `(a,b)`, all previously scanned pairs have first component at least `a`. If the current index is designated as one occurrence attaining the selected minimum, the other `k-1` indices may come from earlier eligible pairs.

To maximize the sum for this candidate, use current `b` plus the largest `k-1` `nums1` values seen earlier.

The heap maintains exactly the information needed for that choice.

**Heap invariant**

Before processing an item, min-heap `q` contains at most `k-1` of the largest `nums1` values among earlier pairs, and `s` is their sum.

Push current `b` and add it to `s`. If heap size becomes `k`, it now represents a valid selection containing current index and the best retained earlier candidates.

The score candidate is `s*a`.

Then pop the smallest heap value and subtract it from `s`. This leaves the largest `k-1` values among all pairs processed so far, reestablishing the invariant for the next candidate minimum.

**Why the current item must be included in its candidate**

Simply taking the top `k` `nums1` values among all processed items could exclude the current index. Then the actual minimum `nums2` might be larger than `a`, and that set belongs to an earlier candidate already considered.

Requiring current inclusion gives every selection a canonical moment: consider the last selected index in descending `nums2` order. Its `nums2` is the selection minimum, and the other selected indices appeared earlier.

The source's push-score-pop pattern models exactly this canonical choice.

**Why keeping the largest `k-1` earlier values is optimal**

For fixed multiplier `a` and required current value `b`, the multiplier does not depend on which eligible earlier indices are chosen. Maximizing the score is therefore equivalent to maximizing their `nums1` sum.

If a retained earlier value is smaller than an unretained one, exchanging them increases or preserves the sum without lowering any `nums2` below `a`. Hence the top `k-1` values are optimal.

**Trace the first sample**

Pairs `(nums2,nums1)` sorted descending are:

`(4,2),(3,3),(2,1),(1,3)`.

With `k=3`:

- after multiplier 4 and 3 items, fewer than three values exist;
- at multiplier 2, heap values sum to $2+3+1=6$, giving score 12;
- after popping the smallest one, retained values are 2 and 3;
- at multiplier 1, adding 3 gives sum 8 and score 8.

Maximum is 12.

**Why the sweep covers every size-`k` selection**

Every size-`k` selection has a last item in sorted order. At that iteration, its multiplier equals the selection's minimum `nums2`. The heap's earlier choices have sum at least as large as the selection's other `k-1` values, so the candidate score is at least that selection's score.

Every evaluated heap candidate is itself a valid set of `k` original paired indices with minimum at least `a` and current value exactly `a` or tied, so its computed product is attainable. The maximum is therefore exact.

## Complexity detail

Creating and sorting `n` pairs costs $O(n\log n)$ time and $O(n)$ storage.

Each pair is pushed once, and after heap size reaches `k` one value is popped. Heap size is at most `k`, so these operations cost $O(n\log k)$ total. Sorting dominates at $O(n\log n)$.

The sorted tuple list uses $O(n)$ space and the heap uses $O(k)$, for $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate subsequences:** $\binom nk$ choices are infeasible.
- **Sort ascending:** Possible with a different scan invariant, but descending order exposes eligible multipliers naturally.
- **`k=1`:** Each current item alone yields `nums1[i]*nums2[i]`.
- **Equal multipliers:** Tuple tie order does not lose any selection.
- **Zero `nums1` or `nums2`:** They are valid and heap arithmetic handles them.
- **Push before scoring:** Current index must belong to its canonical candidate.
- **Pop after scoring:** Retain only the largest `k-1` values for future minima.
- **Minimum multiplier:** It is supplied by the last selected item in sorted order.
- **Large product:** Use 64-bit arithmetic in fixed-width languages.
- **Input pairing:** Never sort arrays independently.
