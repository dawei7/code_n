## General

**Turn inclusive intervals into boundary events.** Coordinates are restricted to `1` through `100`, so maintain a difference array over that fixed domain. For a car occupying `[start, end]`, add one at `start` and subtract one at `end + 1`. The subtraction after the endpoint is essential because `end` itself is covered.

**Recover coverage with a prefix sum.** Scan coordinates from `1` through `100`. After adding the current difference value to `active`, that variable equals the number of car intervals containing the current point: every interval that has started contributes one, and every interval whose inclusive range has ended was removed at the following coordinate. Increment the answer exactly when `active > 0`.

This prefix invariant proves correctness. A coordinate contributes once precisely when at least one interval contains it, regardless of how many cars overlap there. Coordinates with no active interval contribute nothing, so the final total is exactly the size of the union of all covered integer points.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $C=100$ be the fixed coordinate limit. Recording the interval events takes $O(n)$ time, and scanning the domain takes $O(C)$ time. Because $C$ is fixed by the contract, total time is $O(n)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Hash set of points:** Insert every integer in each inclusive range and return the set size. This is direct, but it performs work for every interval-point pair and stores the covered coordinates explicitly.
- **Sort and merge intervals:** Sorting by start coordinate and summing merged inclusive lengths works for an unbounded coordinate domain, but costs $O(n\log n)$ time here.
- **Boolean coverage array:** Mark each point in every interval. It also uses constant space under the fixed domain, though the difference array avoids repeatedly visiting points in heavily overlapping ranges.
- **Single-point car:** When `start == end`, the start event and the removal at `end + 1` count exactly one coordinate.
- **Shared endpoints:** Intervals such as `[1, 2]` and `[2, 3]` both cover `2`, but positive prefix coverage counts it once.
- **Maximum endpoint:** The array includes index `101` so an interval ending at `100` can place its removal event safely.
