## General

Let $n$ be the number of tiles and $q$ the number of queries.

**Describe the circle by its bad edges**

Call circular edge $i$ bad when `colors[i] == colors[(i + 1) % n]`. An alternating group cannot cross a bad edge. Consecutive bad edges therefore partition the circle into maximal alternating runs. If two bad edges occur at positions $a$ and $b$ in circular order, their run length is the positive circular distance from $a$ to $b$; when there is one bad edge, the sole run has length $n$.

A run of length $L$ contains

$$
\max(0,L-s+1)
$$

groups of size $s$. When there are no bad edges, the entire circle alternates, and every one of the $n$ starting positions forms a valid group for every allowed $s<n$.

**Answer all run contributions from suffix aggregates**

Maintain the multiset of run lengths with two Fenwick trees indexed by length: one stores how many runs have each length and the other stores their total lengths. For a query size $s$, obtain the count $C$ and length sum $S$ of all runs with $L \ge s$ by subtracting prefixes through $s-1$. Their combined contribution is

$$
S-(s-1)C.
$$

This replaces a scan over all current runs with two logarithmic prefix queries.

**Update only the two affected circular edges**

Changing tile `index` can alter only the edge entering it and the edge leaving it. A second Fenwick tree stores a `1` at every bad-edge position. Prefix ranks plus order selection find the circular predecessor and successor of a breakpoint in $O(\log n)$ time.

Inserting a newly bad edge splits one run: remove the predecessor-to-successor length and add the two new lengths. Removing a bad edge merges its two neighboring runs: remove both old lengths and add their combined circular length. The special transitions between zero and one bad edge create or remove the single length-$n$ run. No-op color assignments require no structural change.

These split and merge operations preserve both the ordered breakpoint set and the exact run-length multiset after every update, so the suffix formula returns the current circular count.

## Complexity detail

Initialization scans $n$ edges and builds $O(n)$ Fenwick entries in $O(n\log n)$ time. Each count query uses a constant number of Fenwick prefixes, and each update changes at most two breakpoints with a constant number of Fenwick operations, so each query costs $O(\log n)$. Total time is $O((n+q)\log n)$ and the trees, colors, and breakpoint state use $O(n)$ space.

## Alternatives and edge cases

- **Enumerate every circular start:** Checking a requested size directly costs $O(ns)$ per count query and repeats comparisons after every update.
- **Rebuild all alternating runs after each update:** This answers a later count efficiently but pays $O(n)$ for even a no-op or local change.
- **Ordered set plus linear run scan:** Predecessor and successor updates are fast, but summing every eligible run still costs linear time per type-1 query.
- With no bad edges, every starting position is valid; this is possible only for an even-length binary circle.
- With exactly one bad edge, the maximal alternating run has length $n$, but a group cannot cross that one boundary.
- A corner does not exist in the circular model: edges `n - 1 -> 0` and `0 -> 1` are both affected when tile `0` changes.
- One update can create two bad edges, remove two, or exchange one bad edge for another.
- Assigning the current color is a no-op and must preserve every aggregate.
- Runs shorter than the requested size contribute zero.
- Query sizes stop at $n-1$, so the fully alternating special case always contributes exactly $n$.
