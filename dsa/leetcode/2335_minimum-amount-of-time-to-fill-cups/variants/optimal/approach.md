## General

Let $S$ be the total number of requested cups and let $M$ be the largest of
the three type counts. Two independent lower bounds apply:

- at most two cups can be filled per second, requiring at least
  $\lceil S/2\rceil$ seconds;
- at most one cup of the dominant type can be filled per second, requiring at
  least $M$ seconds.

**The larger lower bound is always attainable**

If $M$ exceeds the sum of the other two counts, pair dominant-type cups with
every available other-type cup, then fill the remaining dominant cups alone.
This takes exactly $M$ seconds.

Otherwise, no type has more cups than both others combined. Repeatedly pairing
two currently nonempty different types distributes the work so that at most
one cup remains unpaired. The schedule therefore takes exactly
$\lceil S/2\rceil$ seconds.

These cases cover every triple, so the minimum time is

$$
\max\left(M,\left\lceil\frac{S}{2}\right\rceil\right).
$$

Integer ceiling division is `(S + 1) // 2`.

## Complexity detail

The input always contains exactly three counters. Computing their sum,
maximum, and the formula uses $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases

- **Priority-queue simulation:** Repeatedly filling the two largest nonempty
  types is correct, but it performs one iteration per second instead of using
  the closed form.
- **Repeated sorting:** Sorting three remaining counts after every second also
  simulates an optimal schedule but adds unnecessary state changes.
- **No cups:** Both lower bounds are zero, so the formula returns zero.
- **Only one nonzero type:** The dominant-count bound correctly requires one
  second per cup.
- **Odd balanced total:** Ceiling division accounts for the final unpaired
  cup.
