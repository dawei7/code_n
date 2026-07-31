## General

**Describe every plan by one boundary**

Consider a boundary immediately after index $i$. Remove every car to its right
from the right end, paying $n-i-1$. Within the prefix through $i$, illegal cars
may be removed directly, or an initial part of that prefix may be discarded
from the left. Every possible sequence of operations has an equivalent
description of this form: choose the rightmost car not removed from the right,
then account for all remaining removals on its prefix.

**Compress the best prefix plan**

Let `prefix_cost` be the minimum cost to clear all illegal cars through the
current index without using right-end removals. If the current car is `0`, it
requires no action and the state is unchanged. If it is `1`, there are two
complete choices:

- remove this car directly after applying the previous prefix plan, costing
  `prefix_cost + 2`; or
- remove the entire prefix from the left, costing `index + 1`.

Taking the smaller value preserves the best prefix plan. These choices are
exhaustive because a left-end removal that reaches the current car necessarily
discards the whole current prefix.

**Pair each prefix optimum with a right suffix**

At every index, combine `prefix_cost` with the cost `n - index - 1` of removing
the entire remaining suffix from the right. The minimum of these combined
costs covers every boundary. Initializing the answer to $n$ also represents
removing the whole train from one end.

The prefix recurrence is optimal by induction: it starts at zero before any
car, and for each illegal current car it compares the only two ways the car can
be cleared without a right-end operation. Combining that exact prefix optimum
with every possible right boundary therefore examines an optimal
representation of every legal removal plan, so the smallest recorded cost is
the global minimum.

## Complexity detail

The scan processes each of the $n$ characters once, so it takes $O(n)$ time.
Only the current prefix cost and best total are retained, giving $O(1)$
auxiliary space.

The benchmark defines `size` as the string length $n$. Its repeated mixed
pattern prevents all-zero shortcuts and supplies three legal tiers. A correct
method that enumerates every retained interval and computes its direct-removal
cost takes $O(n^2)$ time on the same inputs.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Precomputing the best left-clearing and
  right-clearing cost at every position also gives $O(n)$ time, but stores
  $O(n)$ values that the one-pass boundary scan does not need.
- **Enumerate the retained interval:** Trying every middle interval and
  charging two units for each illegal car inside it is a direct correctness
  oracle, but examining all interval boundaries takes $O(n^2)$ time even with
  prefix counts.
- An all-zero string returns zero because no removal is necessary.
- For an all-one string, removing every car from either end costs $n$, which is
  better than paying two units per direct removal.
- A single illegal car at an end costs one, while an isolated interior illegal
  car may cost two when crossing surrounding legal cars would be more
  expensive.
- Removing an end can intentionally discard legal cars; the algorithm compares
  that tradeoff at every boundary rather than treating zeros as immovable.
