## General

Each original value $x$ can become any integer in the interval $[x-k,x+k]$. The problem is therefore a maximum matching between these intervals and integer targets, with each target used at most once.

Sort `nums`. Both endpoints of the resulting intervals are then non-decreasing. There is always an optimal matching whose assigned targets also increase with this order: if an earlier interval receives a larger target than a later interval, swapping those two targets keeps both feasible because the earlier interval has no larger lower bound and the later interval has no smaller upper bound.

Maintain `previous`, the last target selected in this noncrossing assignment. For value $x$, the smallest integer that is both inside its interval and distinct from all earlier targets is

$$
\max(x-k,\texttt{previous}+1).
$$

Accept it when it is at most $x+k$; otherwise, skip this interval. Choosing the earliest feasible target is safe because replacing any feasible choice by this smaller one cannot reduce the space available to later intervals. If even this target exceeds the upper endpoint, no increasing target remains in the interval, so skipping cannot reduce the optimum. Induction across the sorted intervals proves that the greedy count is maximum.

## Complexity detail

Let $n$ be the number of elements. Sorting costs $O(n\log n)$ time, and the greedy scan costs $O(n)$, for $O(n\log n)$ total time. Python's sorting storage can use $O(n)$ auxiliary space.

The benchmark defines `size` as $n$ and uses 24, 48, and 96 values, spanning 4x. A four-value pattern with $k=n$ creates heavily overlapping intervals while leaving enough targets for every element. The accepted method assigns each interval in constant time after sorting. A correct slower baseline scans each integer range from its lower endpoint until it finds an unused target and fails only the scaling verdict.

## Alternatives and edge cases

- **Bipartite matching:** Explicitly connect elements to every integer target and run augmenting paths; this is correct only for tiny ranges and is infeasible when $k$ reaches $10^9$.
- **Scan for an unused integer:** A set plus linear probing from every interval's lower endpoint is correct but can take quadratic time on overlapping ranges.
- **Choose the original value first:** Preserving a value when possible can consume a scarce target needed by a later, tighter interval.
- **Zero adjustment:** When $k=0$, the result is exactly the number of distinct input values.
- **Equal values:** $m$ copies of $x$ can occupy at most $\min(m,2k+1)$ targets from their shared interval.
- **Negative targets:** Although input values are positive, subtracting up to $k$ may legally produce zero or negative results.
- **Huge coordinates:** Only endpoint arithmetic and sorting are needed; the algorithm never allocates coordinate-sized storage.
