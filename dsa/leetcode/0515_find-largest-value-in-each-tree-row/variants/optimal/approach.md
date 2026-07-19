## General
**Make queue boundaries coincide with tree rows**

Begin with the root in a queue. At the start of each outer iteration, capture the queue length; those entries are exactly the current depth. Remove precisely that many nodes while appending their children for the next iteration.

**Aggregate one maximum before advancing**

Initialize the row maximum from the first value actually removed, rather than from zero, so all-negative rows work correctly. Compare every remaining node on that row and append the final maximum only after the captured row count is exhausted.

**Why every output entry covers exactly one row**

Children are enqueued only while their parents' row is being consumed, so they cannot enter the current row's fixed iteration count. Conversely, every non-null child is appended once and appears in the next appropriate boundary. Each node therefore contributes to exactly one row maximum, and the outer loop appends those maxima in increasing depth order.

## Complexity detail
Each of `n` nodes is enqueued, inspected, and dequeued once, giving $O(n)$ time. The queue holds at most the tree's maximum width, which is $O(n)$ in the worst case; the returned list uses at most $O(n)$ entries.

## Alternatives and edge cases
- **Depth-first search with a depth-indexed result:** updates an existing maximum or appends the first value at a new depth in $O(n)$ time and $O(h)$ traversal space.
- **Repeated search by requested depth:** returns correct rows but can take $O(n^2)$ time on a chain.
- **Materialize complete rows first:** is easy to inspect but stores more intermediate values than the running maximum needs.
- **Empty tree:** returns an empty list.
- **All-negative row:** requires initialization from a node value, not zero.
- **Single node:** produces a one-element result.
- **Uneven branches:** depth, rather than parent position, determines the aggregation row.
