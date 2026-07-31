## General

For an assignment to finish within $d$ days, a worker with daily capacity $w$ can accept exactly the jobs whose workload is at most $dw$. This threshold grows monotonically with worker capacity.

Sort jobs and workers in ascending order and pair equal ranks. Consider any crossed assignment where workloads $a\le b$ are paired with capacities $x\le y$ as $a$ with $y$ and $b$ with $x$. If that assignment finishes within $d$ days, then $b\le dx$, which also gives $a\le dx$, while $b\le dx\le dy$. Swapping to $a$ with $x$ and $b$ with $y$ therefore remains feasible within the same $d$. Repeatedly removing crossings proves that an optimal assignment exists in sorted order.

For each sorted pair, compute the integer ceiling `(job + worker - 1) // worker`. Because all workers operate concurrently, the full schedule ends when its slowest pair ends, so the answer is the maximum of these durations.

## Complexity detail

Let $n$ be the common number of jobs and workers. Sorting both arrays takes $O(n\log n)$ time, and the paired scan takes $O(n)$ time. The app-local implementation creates sorted copies, which use $O(n)$ auxiliary space and preserve the caller's input lists. The accepted native form sorts in place.

## Alternatives and edge cases

- **Binary search on days:** A candidate duration can be checked after sorting, but the direct sorted pairing already reveals the exact maximum and avoids an extra logarithmic search.
- **Input-order pairing:** Array positions do not prescribe assignments; using them can make a fast worker cover a small job while a slow worker receives an unnecessarily large one.
- **Enumerating assignments:** Trying permutations is factorial and becomes infeasible far below the $10^5$ limit.
- **Partial final day:** Completion time is an integer number of days, so every ratio must be rounded upward rather than truncated.
- **Single pair:** The same ceiling formula directly gives the answer when $n=1$.
