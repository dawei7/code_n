## General
**Count each value's array membership**

Create one counter for every possible value from 1 through 100. Scan every
entry of every array and increment its value's counter. Strictly increasing
input means a value occurs at most once in one array, so a counter records the
number of different arrays containing that value without needing per-array
deduplication.

**Select values present everywhere**

Let $A$ be the number of input arrays. A value belongs to every array exactly
when its counter equals $A$. Visit the bounded value domain in increasing
order and emit precisely those values.

All emitted values appear in every array, and their increasing enumeration
matches their order in every strictly increasing input, so they form a common
subsequence. Any omitted value is absent from at least one array and cannot
belong to a common subsequence. Therefore including every qualifying value
produces the longest possible one.

## Complexity detail
The counting scan visits all $T$ entries once, and enumerating the fixed domain
costs $O(V)$, for $O(T+V)$ time. The frequency array has $V+1$ positions, so
the auxiliary space is $O(V)$. Here $V=100$ is bounded by the problem, though
the notation makes the counting method explicit.

## Alternatives and edge cases
- **Repeated set intersection:** Convert each array to a set and intersect all
  sets. This is also linear on average but requires sorting the final values
  unless order is restored from an input array.
- **Repeated linear membership searches:** For every surviving value, scan
  each next array to find it. This is correct but can take
  $O(AL^2)$ for $A$ arrays of length $L$.
- Strictly increasing inputs contain no duplicates, so raw frequency counts
  cannot be inflated within one array.
- If one array omits a value, that value must be excluded regardless of how
  many other arrays contain it.
- Disjoint arrays produce an empty result.
- If every array is identical, that entire array is the result.
- Values common only to a subset of the arrays do not qualify.
