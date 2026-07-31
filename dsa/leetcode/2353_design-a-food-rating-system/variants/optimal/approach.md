## General

Maintain two authoritative maps: each food's cuisine and each food's current
rating. For every cuisine, also maintain a min-heap of pairs
`(-rating, food)`. Negating the rating puts greater ratings first, while the
food name naturally resolves equal ratings in lexicographically ascending
order.

**Update without searching the heap**

Changing a rating updates the authoritative rating map and pushes a new pair
into the food's cuisine heap. The former pair is left in place. Finding and
removing it eagerly would require a linear heap search, so the method instead
invalidates old entries lazily.

**Clean only when a query needs the top**

For `highestRated(cuisine)`, inspect the heap minimum. If its stored rating
equals the food's current rating, the entry is live and its ordering makes the
food the required answer. Otherwise the entry is stale; pop it and continue.
Every current food state has been pushed into its cuisine heap, so after all
stale leaders are removed, the first live pair has the greatest current rating
and the smallest name among ties.

Each obsolete entry can be popped only once. Although one query may perform
several cleanups, their total across the entire trace is bounded by the number
of rating changes.

## Complexity detail

Let $n$ be the initial number of foods and $q$ the number of later operations.
Initialization performs $n$ heap insertions. Each update performs one
$O(\log(n+q))$ insertion, and queries have amortized
$O(\log(n+q))$ time because every stale pop is charged to an earlier update.
The whole trace therefore takes $O((n+q)\log(n+q))$ time. Maps and heap entries
use $O(n+q)$ space.

## Alternatives and edge cases

- **Ordered set per cuisine:** A balanced tree can eagerly erase the old pair
  and insert the new one with the same asymptotic bounds, but Python has no
  built-in ordered set.
- **Scan every cuisine member:** Maps alone make updates constant time, but
  every query then scans all foods of that cuisine and a long trace becomes
  quadratic.
- **Rating decrease:** The old high-rated heap pair is discarded when it
  reaches the top, exposing the correct next food.
- **Lexicographic ties:** Heap pairs order the food name ascending after the
  negated ratings compare equal.
- **Repeated updates:** Several stale entries for one food are harmless; each
  is eventually removed at most once.
- **One-food cuisine:** Its sole food remains the answer after any valid
  rating change.
