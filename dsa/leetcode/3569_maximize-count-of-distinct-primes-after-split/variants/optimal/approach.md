## General

For a prime value $p$ that currently occurs in the array, let $f_p$ and $\ell_p$ be its first and last occurrence indices. At any legal split, $p$ appears on at least one side and therefore contributes one to the score. It contributes a second time precisely when the split lies strictly after $f_p$ and at or before $\ell_p$.

Consequently, every answer is the number of distinct prime values currently present plus the greatest number of intervals

$$
[f_p,\ell_p-1]
$$

covering one of the zero-based split coordinates. Maintain the interval overlap counts in a lazy segment tree supporting inclusive range addition and a global maximum query. Before changing the occurrences of an affected prime, subtract its old interval; after the change, add its new interval. The segment-tree root then gives the largest possible number of primes counted on both sides.

A sieve determines primality for every possible value. For each prime that appears, keep its active occurrence indices in a set. A min-heap and a max-heap provide its first and last active indices. Deleted heap entries are removed lazily when they reach the top; each heap entry is inserted and removed at most once, so this cleanup is amortized.

Only the old value and the replacement value can change during a query. Updating their occurrence structures and their at most two overlap intervals preserves the interval representation for every prime. Adding the current number of present primes to the segment tree's maximum therefore evaluates exactly the best split after each persistent update.

## Complexity detail

Let $n$ be the array length, $q$ the number of updates, and $U$ the greatest value used. The sieve costs $O(U\log\log U)$. Initial occurrence construction is linear, and all interval initialization and query changes use $O(\log n)$ segment-tree work. Heap insertions and lazy deletions cost $O(\log(n+q))$ amortized, so total time is $O(U\log\log U+(n+q)\log(n+q))$.

The sieve uses $O(U)$ space. Active sets, segment-tree arrays, and all heap entries—including entries awaiting lazy deletion—use $O(n+q)$ additional space.

The benchmark sets $n=q=S$ and repeatedly toggles indexed values between primes and composites. The maintained structure processes each update logarithmically, while the calibrated slower alternative rebuilds all prime occurrence extremes and the best overlap by scanning the complete array after every update, requiring $O(S^2)$ time.

## Alternatives and edge cases

- **Recompute every answer:** Scanning the updated array to rebuild first and last occurrences is simple and correct, but costs $O(nq)$ over all queries.
- **Ordered occurrence tree per prime:** A balanced ordered set offers direct minimum and maximum access, but Python's standard library has no such container; the active-set plus lazy-heaps combination supplies the needed operations.
- **One occurrence of a prime:** Its first and last positions coincide, so it contributes only the universal base count and creates no overlap interval.
- **Prime on both sides:** The interval formulation deliberately counts that prime twice at covered splits.
- **Composite updates:** Composite values create no occurrence set and affect the score only by removing an old prime, if any.
- **Repeated assignment:** Assigning the value already stored at an index changes neither the heaps nor the segment tree.
- **Prime disappears or reappears:** The distinct-prime base count decreases when its active set becomes empty and increases when an insertion changes an empty set to non-empty.
- **Stale heap entries:** Membership in the active set distinguishes current indices from lazily retained deletions before either extreme is read.
