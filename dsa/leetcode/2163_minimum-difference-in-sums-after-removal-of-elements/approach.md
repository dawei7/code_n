## General

After removals, the first $n$ retained elements precede the second $n$ retained elements in original order. Therefore some boundary separates the two retained parts. If the boundary is after the first `i` elements, then $n\le i\le2n$:

- choose $n$ retained values for the first sum from prefix `nums[:i]`;
- choose $n$ retained values for the second sum from suffix `nums[i:]`.

To minimize first sum minus second sum at that boundary, independently choose the $n$ smallest prefix values and the $n$ largest suffix values.

**Maintain prefix n-smallest sums**

The first loop scans the first `2 * n` values. Heap `q1` stores negatives, turning Python’s min-heap into a max-heap of the selected original values.

Each value `x` is added to running sum `s` and pushed as `-x`. If the heap grows beyond $n$, `heappop(q1)` removes the most negative entry, corresponding to the largest original selected value. Subtracting `-heappop(q1)` removes that largest value from `s`.

After processing `i` values, once $i\ge n$, the heap contains exactly the $n$ smallest values from that prefix, and `pre[i]` stores their sum.

The greedy heap invariant is straightforward: whenever $n+1$ candidates are present, discarding their largest leaves the best $n$ for minimizing a sum.

**Maintain suffix n-largest sums**

The second loop scans backward. Heap `q2` is an ordinary min-heap holding selected suffix values.

Each `x` is added and pushed. If more than $n$ values are present, popping the smallest discards the least useful value for a maximum sum. Thus after processing suffix starting at one-based index `i`, `q2` contains its $n$ largest values and `suf[i]` stores their sum.

**Evaluate every legal boundary**

The final generator considers `i` from $n$ through $2n$, inclusive:

`pre[i] - suf[i + 1]`.

Here, `pre[i]` uses zero-based elements `0` through `i-1` for the first part. `suf[i + 1]` uses elements `i` through the end for the second part. These regions are disjoint and preserve the required order.

For a fixed boundary, using anything other than the $n$ smallest prefix values cannot reduce the first sum. Using anything other than the $n$ largest suffix values cannot increase the second sum. Hence this expression is the smallest difference achievable at that boundary.

Taking `min` over all boundaries gives the global answer.

**Why every removal pattern has a boundary**

Take any valid remaining subsequence of $2n$ elements. The original index of its $n$-th element lies before the original index of its $(n+1)$-st element. Place the boundary between them. Its first retained part is an $n$-element choice from the prefix, and its second retained part is an $n$-element choice from the suffix.

Conversely, any such two disjoint choices define $2n$ retained elements in order; all other $n$ elements are removed. Therefore checking all boundaries covers every legal result.

**Why negative differences are desirable**

The objective is the ordinary signed difference, not its absolute value. Making the first sum small and the second sum large can produce a negative answer, which is smaller and therefore preferable. The heap directions reflect this signed objective exactly.

## Complexity detail

Each of the two heap scans processes $O(n)$ values. Every push or pop on a heap of size at most $n+1$ costs $O(\log n)$, so total time is $O(n\log n)$. The final boundary scan is $O(n)$.

Arrays `pre` and `suf` each have length $3n+1$. The two heaps hold at most $n+1$ values. The slice `nums[: n * 2]` used by the first loop also creates an $O(n)$ temporary list. Peak auxiliary space is $O(n)$.

Input values are positive, but sums can be large; Python integers avoid overflow.

## Alternatives and edge cases

- **Store only prefix or suffix array:** The editorial stores prefix minima and computes suffix maxima on the fly, reducing constants while retaining $O(n)$ space.
- **Sort every prefix and suffix:** Repeated sorting would cost far more than maintaining fixed-size heaps.
- **Enumerate removals:** Choosing $n$ removals among $3n$ positions is combinatorial and infeasible.
- **Use smallest values on both sides:** The second sum is subtracted, so it should be maximized, not minimized.
- **Use largest values on both sides:** The first sum should instead be minimized.
- **n equals one:** Boundaries consider every possible removed single element, reproducing the direct three-choice behavior.
- **Boundary n:** The first part must use the first $n$ elements; the second selects the largest $n$ from the remaining $2n$.
- **Boundary 2n:** The second part must use the final $n$ elements; the first selects the smallest $n$ from the first $2n$.
- **Duplicate values:** Heaps retain occurrences independently, as required for array elements.
- **Already favorable ordering:** The method still computes the same optimal boundary without assuming sorted input.
- **Negative final answer:** It is valid and may be the minimum.
- **Heap sign conversion:** `q1` stores `-x` solely to expose the largest original value at the min-heap top.
- **Suffix min-heap:** Popping the smallest leaves the largest $n$ values.
- **Unused pre and suf entries:** Arrays are allocated broadly, but only indexes needed by legal boundaries are read.
- **Input preservation:** Heaps and slices are separate; `nums` is never sorted or changed.
