## General
**Only the four values at each end can matter**

Suppose the array were sorted. Changing an interior value cannot reduce the current range while both the same minimum and maximum remain. Every useful move therefore eliminates one current extreme by moving it inside the eventual retained interval.

With three moves, there are exactly four distributions between the two ends: remove zero smallest and three largest values, one smallest and two largest, two smallest and one largest, or three smallest and zero largest. For distribution $i$, where $i$ smallest values are changed, the surviving endpoints are the value of rank $i$ from the bottom and rank $3-i$ from the top.

Consequently, the answer depends only on the four smallest and four largest values. Obtain those constant-size groups in one scan with bounded heaps, sort the four largest into ascending order, and pair corresponding positions. The four differences are precisely the four possible surviving ranges.

**Why no other edits can do better**

Take any solution using at most three changes and look at its final minimum and maximum among unchanged elements. Every original value outside that interval must have been changed. If $i$ of those values lie below the interval, at most $3-i$ can lie above it. Expanding the retained interval until it reaches the $i$-th smallest and the corresponding high extreme cannot increase the number of required changes, and its width is one of the four candidates considered.

Thus every feasible result is at least one candidate width, while each candidate is achievable by moving its excluded extremes anywhere inside the retained interval. Taking their minimum is exact. When $n \leq 4$, at most three changes can make every occurrence equal to the one value left unchanged, so the answer is zero.

## Complexity detail
Selecting four smallest and four largest elements with fixed-size heaps processes each of the $n$ inputs once. Heap operations cost $O(\log 4)=O(1)$, and comparing the four paired extremes is constant work, so total time is $O(n)$.

Only eight selected values and constant loop state are retained. Since the heap capacity does not grow with $n$, auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort the whole array:** sorting and checking the same four endpoint pairs is concise and correct in $O(n\log n)$ time, but it orders far more values than the answer needs.
- **Quadratic retained-interval enumeration:** examine every sorted pair and accept intervals with at most three outside values. This is correct but wastes $O(n^2)$ comparisons on only four feasible endpoint distributions.
- **Four or fewer elements:** return zero because three changes can make all values equal to one unchanged occurrence.
- **Exactly five elements:** four moves would be needed to force equality in general; the answer is the smallest gap between two values that can remain unchanged.
- **Duplicate extremes:** occurrences, not distinct values, consume moves; fixed-size selection naturally preserves duplicates.
- **Negative values:** ordering and subtraction work unchanged across zero.
- **Already equal:** every candidate width is zero.
- **Use fewer than three moves:** the phrase “at most” is covered because a candidate may already have the optimal range without requiring every allowed change.
- **Input preservation:** bounded selection need not reorder or mutate `nums`.
