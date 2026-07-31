## General

**Turn the changing growth factor into fixed positions.** The first lock is broken while $X=1$, the second while $X=2$, and in general the lock placed at position $j$ needs

$$
\left\lceil \frac{\texttt{strength[i]}}{j} \right\rceil
$$

minutes. Resetting the energy after a break makes the time for one position independent of every earlier choice. The task is therefore to assign each lock to one distinct position from $1$ through $n$ while minimizing the sum of these costs.

**Solve the resulting assignment problem.** Regard locks as rows and break positions as columns of an $n \times n$ cost matrix. Entry $(i,j)$ is the ceiling above. A perfect matching selects exactly one position for every lock and exactly one lock for every position, so perfect matchings correspond one-to-one with valid breaking orders and have exactly the same total time.

The Hungarian algorithm builds a minimum-cost matching one row at a time. Row and column potentials represent the cost already accounted for. During an augmentation, `minimum_slack[j]` records the cheapest reduced-cost edge that can reach an unused column $j$. Subtracting the smallest slack creates at least one new zero reduced-cost edge without making any reduced cost negative. Following the predecessor columns then augments the matching once an unmatched column is reached.

The maintained potentials give a dual lower bound, and every matched edge is tight after each augmentation. When all rows are matched, the matching cost equals that lower bound, so the assignment—and therefore the lock-breaking order—is optimal. Costs are calculated when inspected rather than stored as a full matrix.

## Complexity detail

Let $n$ be the number of locks. Each of $n$ augmentations can visit $O(n)$ columns, and each visit scans or updates $O(n)$ entries, for $O(n^3)$ time. The potentials, matching, predecessor, slack, and visited arrays each have length $n+1$, so the auxiliary space is $O(n)$.

The benchmark defines `size` as $n$. Its three legal tiers span 3 to 14 locks. The reference retains cubic scaling, while a correct subset dynamic program considers every set of already broken locks and every remaining choice, taking $O(n2^n)$ time and $O(2^n)$ space.

## Alternatives and edge cases

- **Subset dynamic programming:** `dp[mask]` can store the best time after breaking exactly the locks in `mask`; it is correct and simple, but its $O(n2^n)$ time is unsuitable for $n=80$.
- **Sort by strength:** Assigning weak locks first is not generally optimal because a stronger lock may benefit more from an earlier increase in $X$; for `[1, 3, 4]`, ascending order costs 5 minutes while the optimum costs 4.
- **Greedy choice by immediate time:** Choosing the currently cheapest lock ignores how each decision changes the rate available to all remaining locks and has no exchange property guaranteeing an optimum.
- **Repeated strengths:** Equal-strength locks remain separate rows; exchanging them leaves the cost unchanged and the matching handles them without special treatment.
- **One lock:** Its only position has factor 1, so the returned time is exactly its strength.
- **Ceiling division:** A lock may be broken only after a whole number of minutes, so its position cost is `(strength[i] + j - 1) // j`, not floor division alone.
